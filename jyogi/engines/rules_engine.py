# Minimal rules engine so the template runs.
# Replace with your advanced engine if you have one.

LAGNA_LORD = {
    "Aries": "Mars",
    "Taurus": "Venus",
    "Gemini": "Mercury",
    "Cancer": "Moon",
    "Leo": "Sun",
    "Virgo": "Mercury",
    "Libra": "Venus",
    "Scorpio": "Mars",
    "Sagittarius": "Jupiter",
    "Capricorn": "Saturn",
    "Aquarius": "Saturn",
    "Pisces": "Jupiter",
}

def _extract_sign(value: str) -> str:
    # Expected: "Aries / Mesha (xx.xx°)" -> "Aries"
    if not value:
        return "-"
    return value.split("/")[0].strip()

def analyze_chart(chart: dict) -> dict:
    asc = _extract_sign(chart.get("Ascendant", ""))
    lord = LAGNA_LORD.get(asc, "-")

    lord_sign = "-"
    # Find the planet entry like "Mars (Mangala)"
    for k, v in chart.items():
        if k.startswith(lord + " "):
            lord_sign = _extract_sign(v)
            break

    # Current dasha string: "Saturn Mahadasha (ends YYYY-MM-DD)"
    d = chart.get("Current_Dasha", "")
    current = d.split(" Mahadasha")[0].strip() if "Mahadasha" in d else "-"
    end_date = "-"
    if "ends" in d:
        end_date = d.split("ends", 1)[1].strip(" )")

    return {
        "lagna": {
            "sign": asc,
            "lord": lord,
            "lord_sign": lord_sign,
            "lord_house": "-",
        },
        "dasha": {
            "current":  current,
            "end_date": end_date,
            "timeline": chart.get("Dasha_Timeline", []),
        },
    }
