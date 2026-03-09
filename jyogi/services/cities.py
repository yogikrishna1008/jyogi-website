import streamlit as st

CITY_COORDS_DEFAULT = {
    "Jabalpur": (23.16, 79.95),
    "Rourkela": (22.26, 84.85),
    "Mumbai": (19.07, 72.87),
    "Delhi": (28.70, 77.10),
    "Bangalore": (12.97, 77.59),
    "Chennai": (13.08, 80.27),
    "Kolkata": (22.57, 88.36),
    "Hyderabad": (17.38, 78.48),
    "Pune": (18.52, 73.85),
    "Ahmedabad": (23.02, 72.57),
    "Jaipur": (26.91, 75.78),
}

def init_city_state():
    if "CITY_COORDS_CUSTOM" not in st.session_state:
        st.session_state["CITY_COORDS_CUSTOM"] = {}

def get_city_coords() -> dict:
    init_city_state()
    return {**CITY_COORDS_DEFAULT, **st.session_state["CITY_COORDS_CUSTOM"]}

def save_custom_city(name: str, lat: float, lon: float):
    init_city_state()
    name = (name or "").strip()
    if not name:
        raise ValueError("City name required.")
    if not (-90 <= lat <= 90):
        raise ValueError("Latitude must be between -90 and 90.")
    if not (-180 <= lon <= 180):
        raise ValueError("Longitude must be between -180 and 180.")
    st.session_state["CITY_COORDS_CUSTOM"][name] = (float(lat), float(lon))
