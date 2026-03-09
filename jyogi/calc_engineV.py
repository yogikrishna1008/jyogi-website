import pytz
import swisseph as swe
from datetime import datetime, timezone, timedelta

IST = pytz.timezone("Asia/Kolkata")

# --- 1. SETUP ---
swe.set_sid_mode(swe.SIDM_LAHIRI)

ZODIAC_DATA = [
    ("Aries", "Mesha"), ("Taurus", "Vrishabha"), ("Gemini", "Mithuna"),
    ("Cancer", "Karka"), ("Leo", "Simha"), ("Virgo", "Kanya"),
    ("Libra", "Tula"), ("Scorpio", "Vrischika"), ("Sagittarius", "Dhanu"),
    ("Capricorn", "Makara"), ("Aquarius", "Kumbha"), ("Pisces", "Meena")
]

PLANET_SANSKRIT = {
    "Sun": "Surya", "Moon": "Chandra", "Mars": "Mangala",
    "Mercury": "Budha", "Jupiter": "Brihaspati", "Venus": "Shukra",
    "Saturn": "Shani", "Rahu": "Rahu", "Ketu": "Ketu"
}

def _jd_from_utc(dt_utc: datetime) -> float:
    return swe.julday(
        dt_utc.year, dt_utc.month, dt_utc.day,
        dt_utc.hour + dt_utc.minute/60.0 + dt_utc.second/3600.0
    )

def _sign_index(lon_deg: float) -> int:
    return int(lon_deg // 30) % 12

def calculate_sadhe_sati(moon_long_deg: float) -> dict:
    """
    Sadhe Sati is active when transit Saturn is:
    - 12th from Moon (Rising)
    - same sign as Moon (Peak)
    - 2nd from Moon (Setting)
    All computed in sidereal Lahiri.
    """
    swe.set_sid_mode(swe.SIDM_LAHIRI)
    now_utc = datetime.now(timezone.utc)

    jd_now = _jd_from_utc(now_utc)
    saturn_lon = swe.calc_ut(jd_now, swe.SATURN, swe.FLG_SIDEREAL | swe.FLG_MOSEPH)[0][0]

    moon_idx = _sign_index(moon_long_deg)
    sat_idx  = _sign_index(saturn_lon)

    twelfth = (moon_idx - 1) % 12
    first   = moon_idx
    second  = (moon_idx + 1) % 12

    if sat_idx == twelfth:
        phase, active = "Rising (12th from Moon)", True
    elif sat_idx == first:
        phase, active = "Peak (over Moon sign)", True
    elif sat_idx == second:
        phase, active = "Setting (2nd from Moon)", True
    else:
        phase, active = None, False

    return {
        "active": active,
        "phase": phase,
        "moon_sign": ZODIAC_DATA[moon_idx][0],
        "saturn_sign": ZODIAC_DATA[sat_idx][0],
        "expected_signs": {
            "rising": ZODIAC_DATA[twelfth][0],
            "peak": ZODIAC_DATA[first][0],
            "setting": ZODIAC_DATA[second][0],
        },
        "saturn_longitude": float(saturn_lon),
        "calculated_at_utc": now_utc.isoformat(),
    }

# --- 2. DASHA LOGIC (Vimshottari — correct Vedic calculation) ---

# 120-year Vimshottari cycle: lord → years
DASHA_YEARS = {
    "Ketu": 7, "Venus": 20, "Sun": 6, "Moon": 10, "Mars": 7,
    "Rahu": 18, "Jupiter": 16, "Saturn": 19, "Mercury": 17,
}

# Fixed sequence of 9 dashas (total = 120 years)
DASHA_SEQUENCE = [
    "Ketu", "Venus", "Sun", "Moon", "Mars",
    "Rahu", "Jupiter", "Saturn", "Mercury",
]

# 27 nakshatras → their ruling dasha lord (fixed Vedic table)
# Ashwini=Ketu, Bharani=Venus, Krittika=Sun, Rohini=Moon, Mrigashira=Mars,
# Ardra=Rahu, Punarvasu=Jupiter, Pushya=Saturn, Ashlesha=Mercury,
# Magha=Ketu, Purva Phalguni=Venus, Uttara Phalguni=Sun, Hasta=Moon,
# Chitra=Mars, Swati=Rahu, Vishakha=Jupiter, Anuradha=Saturn, Jyeshtha=Mercury,
# Mula=Ketu, Purva Ashadha=Venus, Uttara Ashadha=Sun, Shravana=Moon,
# Dhanishtha=Mars, Shatabhisha=Rahu, Purva Bhadrapada=Jupiter,
# Uttara Bhadrapada=Saturn, Revati=Mercury
NAKSHATRA_LORD = [
    "Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury",  # 0-8
    "Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury",  # 9-17
    "Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury",  # 18-26
]

# Total Vimshottari cycle in days (120 years × 365.25)
TOTAL_DAYS = 120 * 365.25


def calculate_current_dasha(moon_long_deg: float, birth_date_str: str) -> str:
    """
    Correct Vimshottari Mahadasha calculation.
    1. Find Moon's nakshatra (each nakshatra = 13°20' = 800')
    2. Get the ruling lord of that nakshatra
    3. Calculate balance of that dasha at birth
    4. Walk forward through dashas until today
    """
    # Each nakshatra spans exactly 13°20' = 13.3333°
    NAKSHATRA_SPAN = 800 / 60.0  # 13.3333...°

    nakshatra_index = int(moon_long_deg / NAKSHATRA_SPAN)  # 0-26
    nakshatra_index = min(nakshatra_index, 26)             # safety clamp

    # How far through this nakshatra is the Moon (0.0 → 1.0)
    degrees_into = moon_long_deg - (nakshatra_index * NAKSHATRA_SPAN)
    fraction_elapsed = degrees_into / NAKSHATRA_SPAN       # 0.0 = start, 1.0 = end
    fraction_remaining = 1.0 - fraction_elapsed

    # Starting dasha lord at birth
    start_lord = NAKSHATRA_LORD[nakshatra_index]
    start_idx  = DASHA_SEQUENCE.index(start_lord)
    start_years = DASHA_YEARS[start_lord]

    # Balance of starting dasha remaining at birth (in days)
    balance_days = fraction_remaining * start_years * 365.25

    birth_date   = datetime.strptime(birth_date_str, "%Y-%m-%d")
    current_date = datetime.now()

    dasha_end = birth_date + timedelta(days=balance_days)
    current_idx = start_idx

    # If we're still in the birth dasha
    if dasha_end > current_date:
        return f"{start_lord} Mahadasha (ends {dasha_end.strftime('%b %Y')})"

    # Walk through subsequent dashas
    while dasha_end <= current_date:
        current_idx = (current_idx + 1) % 9
        lord  = DASHA_SEQUENCE[current_idx]
        years = DASHA_YEARS[lord]
        dasha_end += timedelta(days=years * 365.25)

    lord = DASHA_SEQUENCE[current_idx]
    return f"{lord} Mahadasha (ends {dasha_end.strftime('%b %Y')})"


def get_full_dasha_timeline(moon_long_deg: float, birth_date_str: str) -> list[dict]:
    """Return full list of all dashas with start/end dates — for display."""
    NAKSHATRA_SPAN = 800 / 60.0

    nakshatra_index   = min(int(moon_long_deg / NAKSHATRA_SPAN), 26)
    fraction_elapsed  = (moon_long_deg - nakshatra_index * NAKSHATRA_SPAN) / NAKSHATRA_SPAN
    fraction_remaining = 1.0 - fraction_elapsed

    start_lord  = NAKSHATRA_LORD[nakshatra_index]
    start_idx   = DASHA_SEQUENCE.index(start_lord)
    start_years = DASHA_YEARS[start_lord]
    balance_days = fraction_remaining * start_years * 365.25

    birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
    timeline   = []
    current_start = birth_date
    current_end   = birth_date + timedelta(days=balance_days)

    # First (partial) dasha
    timeline.append({
        "lord":  start_lord,
        "start": current_start.strftime("%b %Y"),
        "end":   current_end.strftime("%b %Y"),
        "years": f"{balance_days/365.25:.1f} yrs (balance)",
    })

    idx = start_idx
    # Remaining full dashas to cover 120 years total
    for _ in range(8):
        idx = (idx + 1) % 9
        lord  = DASHA_SEQUENCE[idx]
        years = DASHA_YEARS[lord]
        next_end = current_end + timedelta(days=years * 365.25)
        timeline.append({
            "lord":  lord,
            "start": current_end.strftime("%b %Y"),
            "end":   next_end.strftime("%b %Y"),
            "years": f"{years} yrs",
        })
        current_end = next_end

    return timeline

# --- 3. MAIN CALCULATOR ---
def get_julian_day(date_str: str, time_str: str) -> float:
    dt_local = IST.localize(datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M"))
    dt_utc = dt_local.astimezone(pytz.utc)
    return _jd_from_utc(dt_utc)

def calculate_vedic_chart(date_str: str, time_str: str, lat: float, lon: float) -> dict:
    jd = get_julian_day(date_str, time_str)
    swe.set_topo(lat, lon, 0)

    chart_data: dict = {}
    moon_long_deg = 0.0

    planets = {
        "Sun": swe.SUN, "Moon": swe.MOON, "Mars": swe.MARS,
        "Mercury": swe.MERCURY, "Jupiter": swe.JUPITER,
        "Venus": swe.VENUS, "Saturn": swe.SATURN, "Rahu": swe.MEAN_NODE
    }

    for name, p_id in planets.items():
        res = swe.calc_ut(jd, p_id, swe.FLG_SIDEREAL)
        longitude = res[0][0]

        if name == "Moon":
            moon_long_deg = longitude

        sign_index = int(longitude / 30) % 12
        degree = longitude % 30
        sign_eng, sign_sans = ZODIAC_DATA[sign_index]
        planet_sans = PLANET_SANSKRIT[name]
        chart_data[f"{name} ({planet_sans})"] = f"{sign_eng} / {sign_sans} ({degree:.2f}°)"

    # Ascendant
    _cusps, ascmc = swe.houses(jd, lat, lon, b'P')
    asc_sidereal = (ascmc[0] - swe.get_ayanamsa_ut(jd)) % 360
    asc_idx = int(asc_sidereal / 30) % 12
    sign_eng, sign_sans = ZODIAC_DATA[asc_idx]
    chart_data["Ascendant"] = f"{sign_eng} / {sign_sans} ({asc_sidereal%30:.2f}°)"

    chart_data["Current_Dasha"]   = calculate_current_dasha(moon_long_deg, date_str)
    chart_data["Dasha_Timeline"]  = get_full_dasha_timeline(moon_long_deg, date_str)
    chart_data["sadhe_sati"]      = calculate_sadhe_sati(moon_long_deg)

    return chart_data
