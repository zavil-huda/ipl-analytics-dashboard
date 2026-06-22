import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR)) 

import pandas as pd
import streamlit as st

from ipl_dashboard.config import MATCHES_CLEAN_PATH


@st.cache_data
def load_matches():
    return pd.read_csv(MATCHES_CLEAN_PATH)