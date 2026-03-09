from __future__ import annotations

from jyogi import calc_engine
from jyogi.engines import rules_engine
from jyogi.engines.interpretations import interpret_lagna, interpret_dasha, interpret_sadhe_sati
from jyogi.clients.ai import chat
from jyogi.config import ASTRO_PROMPT
from jyogi import numerology


def _chart_text(chart: dict) -> str:
    skip = {"sadhe_sati", "Current_Dasha", "Dasha_Timeline"}
    return "\n".join([f"{k}: {v}" for k, v in chart.items() if k not in skip])


def generate_astrology_report(
    name: str,
    date_str: str,
    time_str: str,
    lat: float,
    lon: float,
    user_q: str = "",
) -> dict:
    # ── 1. Calculate chart (Swiss Ephemeris — 100% accurate) ────────────────
    chart    = calc_engine.calculate_vedic_chart(date_str, time_str, lat, lon)
    chart_text = _chart_text(chart)
    analysis   = rules_engine.analyze_chart(chart)

    # ── 2. Numerology (pure calculation) ────────────────────────────────────
    lp_num  = numerology.calculate_life_path(date_str)
    lp_data = numerology.get_detailed_report(lp_num)

    # ── 3. Lagna — PURE CALCULATION (no AI) ─────────────────────────────────
    lagna       = analysis.get("lagna", {}) or {}
    lagna_text  = interpret_lagna(
        lagna_sign = lagna.get("sign", ""),
        lord       = lagna.get("lord", ""),
        lord_sign  = lagna.get("lord_sign", ""),
    )

    # ── 4. Mahadasha — PURE CALCULATION (no AI) ─────────────────────────────
    dasha      = analysis.get("dasha", {}) or {}
    dasha_text = interpret_dasha(
        lord         = dasha.get("current", ""),
        end_date_str = dasha.get("end_date", ""),
    )

    # ── 5. Sadhe Sati — PURE CALCULATION (no AI) ────────────────────────────
    sadhe    = chart.get("sadhe_sati", {}) or {}
    ss_text  = interpret_sadhe_sati(sadhe)

    # ── 6. User question — AI only for free-form question answer ────────────
    # This is the ONE place AI is still used — to interpret the user's
    # specific question against the calculated chart. No personal data sent.
    qa_text = ""
    if user_q and user_q.strip():
        qa_prompt = (
            f"Question: {user_q}\n\n"
            f"Sidereal birth chart positions:\n{chart_text}\n\n"
            "Answer using Vedic astrology: give 3 clear, actionable insights and 1 remedy."
        )
        qa_text = chat(ASTRO_PROMPT, qa_prompt, temperature=0.5, max_tokens=450)

    # ── 7. PDF sections ──────────────────────────────────────────────────────
    sections = [
        ("Numerology", (
            f"Life Path Number: {lp_num} — {lp_data.get('title', '-')}\n"
            f"Lucky Gem   : {lp_data.get('lucky_gem', '-')}\n"
            f"Lucky Colour: {lp_data.get('lucky_color', '-')}"
        )),
        ("Birth Chart (Sidereal Lahiri)", chart_text),
        ("Lagna & Personality",           lagna_text),
        ("Current Mahadasha",             dasha_text),
        ("Saturn Transit — Sadhe Sati",   ss_text),
    ]
    if qa_text:
        sections.append(("Your Question", qa_text))

    return {
        "lp_num":     lp_num,
        "lp_data":    lp_data,
        "chart":      chart,
        "chart_text": chart_text,
        "analysis":   analysis,
        "lagna_text": lagna_text,
        "dasha_text": dasha_text,
        "ss_text":    ss_text,
        "qa_text":    qa_text,
        "sections":   sections,
    }
