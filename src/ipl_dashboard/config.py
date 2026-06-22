from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "Data"
RAW_DATA_DIR = DATA_DIR / "Raw"
PROCESSED_DATA_DIR = DATA_DIR / "Processed"

MATCHES_CLEAN_PATH = PROCESSED_DATA_DIR / "matches_clean.csv"

APP_TITLE = "IPL Analytics Dashboard"
PAGE_ICON = "🏏"