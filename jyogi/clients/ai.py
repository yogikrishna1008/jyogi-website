"""
AI client — OpenAI wrapper with rate limiting and abuse protection.
"""
import os, time
import streamlit as st
from openai import OpenAI
from jyogi.config import MODEL_ID, AI_TEMPERATURE, AI_MAX_TOKENS

# ── Rate limiting: max AI calls per session ────────────────────────────────
MAX_CALLS_PER_SESSION = 20   # a real user won't need more than this


@st.cache_resource
def get_client() -> OpenAI:
    api_key = st.secrets.get("OPENAI_API_KEY", None)
    if not api_key:
        api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Missing OPENAI_API_KEY.\n"
            "Add it to .streamlit/secrets.toml  →  OPENAI_API_KEY = \"sk-...\""
        )
    return OpenAI(api_key=api_key)


def _check_rate_limit() -> bool:
    """Returns True if allowed, False if rate limited."""
    if "ai_call_count" not in st.session_state:
        st.session_state["ai_call_count"] = 0
        st.session_state["ai_first_call"] = time.time()

    # Reset counter every hour
    elapsed = time.time() - st.session_state["ai_first_call"]
    if elapsed > 3600:
        st.session_state["ai_call_count"] = 0
        st.session_state["ai_first_call"] = time.time()

    if st.session_state["ai_call_count"] >= MAX_CALLS_PER_SESSION:
        return False

    st.session_state["ai_call_count"] += 1
    return True


def chat(
    system_prompt: str,
    user_message: str,
    temperature: float | None = None,
    max_tokens: int | None = None,
) -> str:
    # Rate limit check
    if not _check_rate_limit():
        return "⚠️ Too many requests in this session. Please refresh and try again."

    # Input size guard — prevent prompt injection via huge inputs
    if len(user_message) > 4000:
        user_message = user_message[:4000] + "\n[truncated]"

    try:
        client = get_client()
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
        return f"⚠️ AI Error: {exc}"
