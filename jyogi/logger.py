"""
Jyogi — Data Logger
Stores all user readings + manual client records in jyogi_data.xlsx
4 sheets:
  - Readings   : auto-logged every time someone does a reading
  - Clients    : your CRM — add/edit clients manually
  - Orders     : crystal bracelet orders
  - Notes      : your private notes per client

The Excel file can be downloaded from Admin panel, edited locally,
and re-uploaded to sync changes back to the web app.
"""
import os
from datetime import datetime

import pandas as pd

DATA_FILE = "jyogi_data.xlsx"

# ── Column schemas ──────────────────────────────────────────────────────────
SCHEMAS = {
    "Readings": [
        "Timestamp", "Type", "Client Name",
        "Birth Date", "Birth Time", "Birth Location",
        "Spread", "Question", "Session ID",
    ],
    "Clients": [
        "Name", "Phone", "Email", "City",
        "Date of Birth", "Time of Birth", "Birth Place",
        "Readings Done", "Last Reading", "Notes", "Added On",
    ],
    "Orders": [
        "Date", "Client Name", "Phone",
        "Item", "Amount (₹)", "Payment Status", "Delivery Status", "Notes",
    ],
    "Notes": [
        "Date", "Client Name", "Note", "Follow Up Date", "Done",
    ],
}


# ── Init ────────────────────────────────────────────────────────────────────
def init_db():
    """Create jyogi_data.xlsx with all sheets if it doesn't exist."""
    if os.path.exists(DATA_FILE):
        return
    with pd.ExcelWriter(DATA_FILE, engine="openpyxl") as writer:
        for sheet, cols in SCHEMAS.items():
            pd.DataFrame(columns=cols).to_excel(writer, sheet_name=sheet, index=False)


def _read_all() -> dict[str, pd.DataFrame]:
    """Read all sheets into a dict of DataFrames."""
    init_db()
    try:
        return pd.read_excel(DATA_FILE, sheet_name=None, dtype=str)
    except Exception:
        return {s: pd.DataFrame(columns=c) for s, c in SCHEMAS.items()}


def _write_all(sheets: dict[str, pd.DataFrame]):
    """Write all sheets back to Excel."""
    with pd.ExcelWriter(DATA_FILE, engine="openpyxl") as writer:
        for sheet, df in sheets.items():
            # Preserve column order from schema
            cols = SCHEMAS.get(sheet, list(df.columns))
            for c in cols:
                if c not in df.columns:
                    df[c] = ""
            df[cols].to_excel(writer, sheet_name=sheet, index=False)


# ── Auto-logging (called by pipelines) ──────────────────────────────────────
def log_astrology(client_name, birth_date, birth_time, birth_location,
                  question, session_id=""):
    init_db()
    sheets = _read_all()
    new_row = {
        "Timestamp":      datetime.now().strftime("%Y-%m-%d %H:%M"),
        "Type":           "Vedic Astrology",
        "Client Name":    client_name.strip(),
        "Birth Date":     birth_date,
        "Birth Time":     birth_time,
        "Birth Location": birth_location,
        "Spread":         "",
        "Question":       question.strip(),
        "Session ID":     session_id,
    }
    df = sheets.get("Readings", pd.DataFrame(columns=SCHEMAS["Readings"]))
    sheets["Readings"] = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    _write_all(sheets)


def log_tarot(client_name, spread_name, cards_count, question, session_id=""):
    init_db()
    sheets = _read_all()
    new_row = {
        "Timestamp":      datetime.now().strftime("%Y-%m-%d %H:%M"),
        "Type":           "Tarot",
        "Client Name":    client_name.strip(),
        "Birth Date":     "",
        "Birth Time":     "",
        "Birth Location": "",
        "Spread":         f"{spread_name} ({cards_count} cards)",
        "Question":       question.strip(),
        "Session ID":     session_id,
    }
    df = sheets.get("Readings", pd.DataFrame(columns=SCHEMAS["Readings"]))
    sheets["Readings"] = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    _write_all(sheets)


# ── CRUD helpers (used by admin panel) ──────────────────────────────────────
def get_sheet(sheet: str) -> pd.DataFrame:
    init_db()
    sheets = _read_all()
    df = sheets.get(sheet, pd.DataFrame(columns=SCHEMAS.get(sheet, [])))
    return df.fillna("")


def add_row(sheet: str, row: dict):
    sheets = _read_all()
    df = sheets.get(sheet, pd.DataFrame(columns=SCHEMAS.get(sheet, [])))
    sheets[sheet] = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    _write_all(sheets)


def delete_row(sheet: str, idx: int):
    sheets = _read_all()
    df = sheets.get(sheet, pd.DataFrame())
    if 0 <= idx < len(df):
        sheets[sheet] = df.drop(df.index[idx]).reset_index(drop=True)
        _write_all(sheets)


def replace_sheet(sheet: str, df: pd.DataFrame):
    """Replace an entire sheet — used when uploading edited Excel."""
    sheets = _read_all()
    sheets[sheet] = df.fillna("")
    _write_all(sheets)


def get_stats() -> dict:
    readings = get_sheet("Readings")
    clients  = get_sheet("Clients")
    orders   = get_sheet("Orders")
    astro    = readings[readings["Type"] == "Vedic Astrology"] if "Type" in readings else pd.DataFrame()
    tarot    = readings[readings["Type"] == "Tarot"] if "Type" in readings else pd.DataFrame()
    return {
        "total_readings":  len(readings),
        "astro_count":     len(astro),
        "tarot_count":     len(tarot),
        "total_clients":   len(clients),
        "total_orders":    len(orders),
        "recent_readings": readings.tail(5).iloc[::-1].to_dict("records") if len(readings) else [],
    }


def load_excel_bytes() -> bytes:
    """Return the raw Excel file bytes for download."""
    init_db()
    with open(DATA_FILE, "rb") as f:
        return f.read()


def import_excel(file_bytes: bytes):
    """Replace entire database from uploaded Excel file."""
    import io
    try:
        xl = pd.read_excel(io.BytesIO(file_bytes), sheet_name=None, dtype=str)
        with pd.ExcelWriter(DATA_FILE, engine="openpyxl") as writer:
            for sheet, df in xl.items():
                df.fillna("").to_excel(writer, sheet_name=sheet, index=False)
        return True, "✅ Data imported successfully."
    except Exception as e:
        return False, f"❌ Import failed: {e}"
