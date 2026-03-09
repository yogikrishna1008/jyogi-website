"""
Jyogi AI — FastAPI Backend
--------------------------
Wraps the existing jyogi/ package with a clean REST API.
Deploy to Railway.app (or any cloud that can run Python).

Your existing jyogi/ folder is UNCHANGED — this file is the only new code.

Endpoints:
  POST /api/geocode   — city name → lat/lon
  POST /api/chart     — birth details → full Vedic chart + PDF
  POST /api/tarot     — spread id + question → AI tarot reading
  GET  /api/pdf/{id}  — download a generated PDF by session id
  GET  /health        — health check (for Railway uptime monitor)
"""

from __future__ import annotations

import os
import uuid
import time
import tempfile
import logging
from collections import defaultdict
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

# ── Logging ────────────────────────────────────────────────────────────────
logging.basicConfig(level=logging.INFO, format="%(asctime)s  %(levelname)s  %(message)s")
log = logging.getLogger("jyogi_api")

# ── PDF temp store: session_id → filepath ─────────────────────────────────
pdf_store: dict[str, str] = {}

# ── In-memory rate limiter (replaces Streamlit session_state) ─────────────
# Key: client IP — Value: (call_count, window_start_time)
_rate_state: dict[str, tuple[int, float]] = defaultdict(lambda: (0, time.time()))
MAX_CALLS_PER_HOUR = 20


def check_rate_limit(client_ip: str) -> bool:
    """Return True if request is allowed, False if rate-limited."""
    count, window_start = _rate_state[client_ip]
    now = time.time()
    if now - window_start > 3600:                   # reset window every hour
        _rate_state[client_ip] = (1, now)
        return True
    if count >= MAX_CALLS_PER_HOUR:
        return False
    _rate_state[client_ip] = (count + 1, window_start)
    return True


# ── Monkey-patch: replace Streamlit AI client with plain OpenAI ────────────
# The jyogi/clients/ai.py uses st.cache_resource and st.session_state.
# We replace it here so the rest of the package works without Streamlit.
import openai as _openai
from jyogi.config import MODEL_ID, AI_TEMPERATURE, AI_MAX_TOKENS, ASTRO_PROMPT, TAROT_PROMPT  # noqa: E402


def _get_openai_client() -> _openai.OpenAI:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY environment variable not set.\n"
            "Add it to Railway → Variables → OPENAI_API_KEY=sk-..."
        )
    return _openai.OpenAI(api_key=api_key)


def _patched_chat(
    system_prompt: str,
    user_message: str,
    temperature: float | None = None,
    max_tokens: int | None = None,
) -> str:
    """Drop-in replacement for jyogi.clients.ai.chat — no Streamlit dependency."""
    if len(user_message) > 4000:
        user_message = user_message[:4000] + "\n[truncated]"
    try:
        client = _get_openai_client()
        r = client.chat.completions.create(
            model=MODEL_ID,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user",   "content": user_message},
            ],
            temperature=AI_TEMPERATURE if temperature is None else temperature,
            max_tokens=AI_MAX_TOKENS   if max_tokens is None else max_tokens,
        )
        return r.choices[0].message.content or ""
    except Exception as exc:
        log.error("OpenAI error: %s", exc)
        return f"⚠️ AI Error: {exc}"


# Patch before any pipeline import touches the old client
import jyogi.clients.ai as _ai_module  # noqa: E402
_ai_module.chat = _patched_chat
_ai_module.get_client = _get_openai_client

# Now safe to import pipelines
from jyogi.pipelines.astrology import generate_astrology_report  # noqa: E402
from jyogi.pipelines.tarot import generate_tarot_report          # noqa: E402
from jyogi.reports.pdf_writer import save_reading_to_pdf         # noqa: E402
from geopy.geocoders import Nominatim                             # noqa: E402


# ── Geocoder (plain, no Streamlit cache) ──────────────────────────────────
_geocoder = Nominatim(user_agent="jyogi_api_v1")
_geocache: dict[str, dict] = {}


def geocode_city(query: str) -> dict | None:
    q = (query or "").strip()
    if not q:
        return None
    if q in _geocache:
        return _geocache[q]
    try:
        loc = _geocoder.geocode(q, timeout=8)
        if not loc:
            return None
        result = {"lat": loc.latitude, "lon": loc.longitude, "address": loc.address}
        _geocache[q] = result
        return result
    except Exception as exc:
        log.warning("Geocode error for '%s': %s", q, exc)
        return None


# ── FastAPI app ────────────────────────────────────────────────────────────
@asynccontextmanager
async def lifespan(app: FastAPI):
    log.info("🪐 Jyogi API starting up")
    yield
    log.info("Jyogi API shutting down — clearing %d PDFs", len(pdf_store))
    for path in pdf_store.values():
        try:
            Path(path).unlink(missing_ok=True)
        except Exception:
            pass


app = FastAPI(
    title="Jyogi AI API",
    description="Vedic Astrology · Tarot · Sacred Crystals — Backend API",
    version="1.0.0",
    lifespan=lifespan,
)

# ── CORS ──────────────────────────────────────────────────────────────────
# Replace "jyogi.netlify.app" with your actual Netlify URL or custom domain.
ALLOWED_ORIGINS = [
    "https://kaleidoscopic-gingersnap-448bbf.netlify.app",
    "https://jyogi-api.onrender.com",
    "http://localhost:3000",
    "http://127.0.0.1:5500",
    "null",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


# ── Request / Response models ──────────────────────────────────────────────

class GeocodeRequest(BaseModel):
    city: str = Field(..., min_length=2, max_length=100, description="City name to geocode")


class GeocodeResponse(BaseModel):
    lat: float
    lon: float
    address: str


class ChartRequest(BaseModel):
    name: str          = Field(..., min_length=1, max_length=80)
    dob:  str          = Field(..., description="YYYY-MM-DD")
    time: str          = Field("12:00",    description="HH:MM (24h)")
    city: str          = Field(..., min_length=2, max_length=100)
    question: Optional[str] = Field(None, max_length=500)


class ChartResponse(BaseModel):
    name:        str
    lp_num:      int
    lp_title:    str
    chart_text:  str
    lagna_text:  str
    dasha_text:  str
    ss_text:     str
    qa_text:     str
    pdf_id:      Optional[str]
    sections:    list[dict]


class TarotRequest(BaseModel):
    spread_id:   str          = Field("1", description="Spread key from tarot_deck.spreads")
    question:    Optional[str] = Field(None, max_length=400)
    client_name: Optional[str] = Field(None, max_length=80)


class TarotResponse(BaseModel):
    spread_name:  str
    card_summary: str
    affirmations: str
    ai_answer:    str
    pdf_id:       Optional[str]
    sections:     list[dict]


# ── Health ─────────────────────────────────────────────────────────────────

@app.get("/health", tags=["System"])
def health():
    return {"status": "ok", "service": "Jyogi AI API", "version": "1.0.0"}


# ── Geocode ────────────────────────────────────────────────────────────────

@app.post("/api/geocode", response_model=GeocodeResponse, tags=["Utilities"])
def api_geocode(body: GeocodeRequest, request: Request):
    client_ip = request.client.host if request.client else "unknown"
    if not check_rate_limit(client_ip):
        raise HTTPException(429, "Too many requests. Please try again later.")

    result = geocode_city(body.city)
    if not result:
        raise HTTPException(404, f"City not found: {body.city!r}. Try a major nearby city.")

    log.info("Geocoded '%s' → %.4f, %.4f", body.city, result["lat"], result["lon"])
    return GeocodeResponse(**result)


# ── Vedic Chart ────────────────────────────────────────────────────────────

@app.post("/api/chart", response_model=ChartResponse, tags=["Astrology"])
def api_chart(body: ChartRequest, request: Request):
    client_ip = request.client.host if request.client else "unknown"
    if not check_rate_limit(client_ip):
        raise HTTPException(429, "Too many requests. Please try again later.")

    # 1. Geocode city
    geo = geocode_city(body.city)
    if not geo:
        raise HTTPException(404, f"City not found: {body.city!r}")

    log.info("Chart request — %s, %s, %s, city=%s", body.name, body.dob, body.time, body.city)

    # 2. Generate report (Swiss Ephemeris + optional AI Q&A)
    try:
        report = generate_astrology_report(
            name     = body.name,
            date_str = body.dob,
            time_str = body.time,
            lat      = geo["lat"],
            lon      = geo["lon"],
            user_q   = body.question or "",
        )
    except Exception as exc:
        log.error("Chart generation error: %s", exc)
        raise HTTPException(500, f"Chart calculation failed: {exc}")

    # 3. Generate PDF and store temporarily
    pdf_id = None
    try:
        tmp = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False)
        tmp.close()
        title = f"Jyogi Vedic Report — {body.name}"
        ok = save_reading_to_pdf(tmp.name, report["sections"], title=title)
        if ok:
            pdf_id = str(uuid.uuid4())
            pdf_store[pdf_id] = tmp.name
            log.info("PDF saved → id=%s", pdf_id)
    except Exception as exc:
        log.warning("PDF generation failed (non-fatal): %s", exc)

    # 4. Build clean response
    lp_data = report.get("lp_data", {}) or {}
    sections_out = [
        {"heading": heading, "text": text}
        for heading, text in (report.get("sections") or [])
    ]

    return ChartResponse(
        name       = body.name,
        lp_num     = report.get("lp_num", 0),
        lp_title   = lp_data.get("title", ""),
        chart_text = report.get("chart_text", ""),
        lagna_text = report.get("lagna_text", ""),
        dasha_text = report.get("dasha_text", ""),
        ss_text    = report.get("ss_text", ""),
        qa_text    = report.get("qa_text", ""),
        pdf_id     = pdf_id,
        sections   = sections_out,
    )


# ── Tarot ──────────────────────────────────────────────────────────────────

@app.post("/api/tarot", response_model=TarotResponse, tags=["Tarot"])
def api_tarot(body: TarotRequest, request: Request):
    client_ip = request.client.host if request.client else "unknown"
    if not check_rate_limit(client_ip):
        raise HTTPException(429, "Too many requests. Please try again later.")

    log.info("Tarot request — spread=%s, q=%s", body.spread_id, body.question)

    try:
        result = generate_tarot_report(
            spread_id   = body.spread_id,
            user_q      = body.question or "",
            client_name = body.client_name or "",
        )
    except Exception as exc:
        log.error("Tarot generation error: %s", exc)
        raise HTTPException(500, f"Tarot reading failed: {exc}")

    # Generate PDF
    pdf_id = None
    try:
        tmp = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False)
        tmp.close()
        title = f"Jyogi Tarot Reading — {body.client_name or 'Your Reading'}"
        ok = save_reading_to_pdf(tmp.name, result["sections"], title=title)
        if ok:
            pdf_id = str(uuid.uuid4())
            pdf_store[pdf_id] = tmp.name
    except Exception as exc:
        log.warning("Tarot PDF generation failed (non-fatal): %s", exc)

    sections_out = [
        {"heading": heading, "text": text}
        for heading, text in (result.get("sections") or [])
    ]

    spread_info = result.get("spread_info", {}) or {}

    return TarotResponse(
        spread_name  = spread_info.get("name", body.spread_id),
        card_summary = result.get("card_summary", ""),
        affirmations = result.get("affirmations", ""),
        ai_answer    = result.get("ai_answer", ""),
        pdf_id       = pdf_id,
        sections     = sections_out,
    )


# ── PDF Download ───────────────────────────────────────────────────────────

@app.get("/api/pdf/{pdf_id}", tags=["Utilities"])
def api_pdf_download(pdf_id: str):
    path = pdf_store.get(pdf_id)
    if not path or not Path(path).exists():
        raise HTTPException(404, "PDF not found or expired. Please generate a new reading.")
    return FileResponse(
        path        = path,
        media_type  = "application/pdf",
        filename    = "jyogi_reading.pdf",
    )
