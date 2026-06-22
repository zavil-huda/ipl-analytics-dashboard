import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))


import streamlit as st

from ipl_dashboard.data_loader import load_matches
from ipl_dashboard.components.sidebar import render_sidebar
from ipl_dashboard.components.kpi_cards import render_kpi_cards

from ipl_dashboard.components.charts import (
    render_top_teams_chart,
    render_top_players_chart,
    render_toss_impact_chart,
    render_matches_per_season_chart,
)


# ==================================================
# PAGE
# ==================================================

st.set_page_config(
    page_title="IPL Analytics Dashboard",
    page_icon="🏏",
    layout="wide",
)


# ==================================================
# STYLE
# ==================================================

st.markdown(
"""
<style>

.stApp{

background:
radial-gradient(
circle at top,
#07152f 0%,
#020617 45%,
#01040b 100%
);

color:white;

}

.block-container{

max-width:1500px;

padding-top:30px;

padding-left:40px;

padding-right:40px;

}


section[data-testid="stSidebar"]{

background:

linear-gradient(
180deg,
#07111f,
#04101d
);

border-right:
1px solid rgba(255,255,255,.06);

}


.hero{

background:

linear-gradient(
135deg,
rgba(24,38,79,.95),
rgba(5,10,20,.95)
);

padding:42px;

border-radius:34px;

margin-bottom:22px;

border:

1px solid rgba(255,255,255,.08);

box-shadow:

0 20px 60px rgba(0,0,0,.35);

}


.hero h1{

font-size:

clamp(
44px,
4vw,
72px
);

margin:0;

line-height:1.05;

}


.hero p{

margin-top:14px;

font-size:18px;

opacity:.75;

}


hr{

display:none;

}


.stTabs [data-baseweb="tab"]{

font-size:15px;

}


footer{

visibility:hidden;

}



@media(max-width:1200px){

.block-container{

padding-left:18px;

padding-right:18px;

}

.hero{

padding:30px;

}

.hero h1{

font-size:48px;

}

}

</style>
""",
unsafe_allow_html=True,
)


# ==================================================
# HERO
# ==================================================

st.markdown(
"""
<div class='hero'>

<h1>
🏏 IPL Analytics Dashboard
</h1>

<p>
Interactive Cricket Intelligence Platform
</p>

</div>
""",
unsafe_allow_html=True,
)


# ==================================================
# LOAD
# ==================================================

try:

    matches = load_matches()

except Exception as e:

    st.error(f"Error loading data: {e}")

    st.stop()


# ==================================================
# FILTER
# ==================================================

filters = render_sidebar(matches)

season = filters["season"]

if season != "All":

    filtered = (
        matches[
            matches["season"]
            ==
            season
        ]
        .copy()
    )

else:

    filtered = matches.copy()


# ==================================================
# KPI
# ==================================================

render_kpi_cards(
    filtered
)


st.markdown("<br>", unsafe_allow_html=True)


# ==================================================
# TABS
# ==================================================

tab1, tab2 = st.tabs([
"📊 Analytics",
"📈 Trends"
])


with tab1:

    col1, col2 = st.columns(2)

    with col1:

        render_top_teams_chart(
            filtered
        )

    with col2:

        render_top_players_chart(
            filtered
        )


with tab2:

    col3, col4 = st.columns(2)

    with col3:

        render_toss_impact_chart(
            filtered
        )

    with col4:

        render_matches_per_season_chart(
            matches
            if season == "All"
            else filtered
        )


# ==================================================
# FOOTER
# ==================================================

st.markdown(
"""

Built & Designed by Zavil Huda Quraishi
padding-bottom:10st.markdown(
"""

<br><br>

<div
style='
text-align:center;
opacity:.7;
padding-bottom:10px;
margin-top:-40px;
'>

Built & Designed by Zavil Huda Quraishi

<br><br>

Data • Design • Intelligence

</div>

""",
unsafe_allow_html=True,
)px;
margin-top:-40px;padding-bottom:10px;
margin-top:-40px;
<br><br>

Data • Design • Intelligence<br><br>

<div
style='
text-align:center;
opacity:.7;
padding-bottom:30px;
'>

Built with ❤️

<br>

Python • Pandas • Plotly • Streamlit

</div>

""",
unsafe_allow_html=True,
)
