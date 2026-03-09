import streamlit as st
from geopy.geocoders import Nominatim

from jyogi.config import GEOCODE_TTL_SECONDS


@st.cache_data(show_spinner=False, ttl=GEOCODE_TTL_SECONDS)
def geocode_city(query: str) -> dict | None:
    q = (query or "").strip()
    if not q:
        return None
    try:
        geolocator = Nominatim(user_agent="jyogi_app_v2")
        loc = geolocator.geocode(q, timeout=5)
        if not loc:
            return None
        return {"lat": loc.latitude, "lon": loc.longitude, "address": loc.address}
    except Exception:
        return None
