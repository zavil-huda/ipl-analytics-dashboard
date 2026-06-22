import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))


import streamlit as st

from ipl_dashboard.data_loader import load_matches

from ipl_dashboard.components.sidebar import (
    render_sidebar,
)

from ipl_dashboard.components.kpi_cards import (
    render_kpi_cards,
)

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
    initial_sidebar_state="expanded",
)


# ==================================================
# STYLE
# ==================================================

st.markdown(
"""
<style>

.stApp{

background:

linear-gradient(
180deg,
#010814,
#020d1f,
#010814
);

}


.block-container{

max-width:1500px;

padding-top:2rem;

padding-bottom:4rem;

}


.hero{

padding:42px;

border-radius:32px;

background:

linear-gradient(
135deg,
rgba(17,24,39,.96),
rgba(4,8,18,.98)
);

border:

1px solid rgba(255,255,255,.06);

margin-bottom:28px;

}


.hero h1{

margin:0;

font-size:

clamp(
40px,
5vw,
72px
);

line-height:1.05;

}


.hero p{

margin-top:14px;

font-size:18px;

opacity:.82;

}


div[data-testid="stTabs"]{

margin-top:16px;

}


footer{

visibility:hidden;

}


@media(max-width:1100px){

.block-container{

padding-left:18px;

padding-right:18px;

}

.hero{

padding:28px;

}

}

</style>
""",
unsafe_allow_html=True,
)


# ==================================================
# LOAD DATA
# ==================================================

try:

    matches = load_matches()

except Exception as e:

    st.error(
        f"Data load failed: {e}"
    )

    st.stop()


# ==================================================
# SIDEBAR
# ==================================================

filters = render_sidebar(
    matches
)

selected_season = filters[
    "season"
]


# ==================================================
# FILTER
# ==================================================

if selected_season != "All":

    filtered = (

        matches[
            matches[
                "season"
            ]
            ==
            selected_season
        ]

        .copy()

    )

else:

    filtered = matches.copy()


# ==================================================
# HERO
# ==================================================

st.markdown(
"""
<div class="hero">

<h1>
🏏 IPL Analytics Dashboard
</h1>

<p>

Explore IPL history through
interactive analytics.

</p>

</div>
""",
unsafe_allow_html=True,
)


# ==================================================
# KPI
# ==================================================

render_kpi_cards(
    filtered
)

st.markdown(
"<br>",
unsafe_allow_html=True
)


# ==================================================
# ANALYTICS
# ==================================================

tab1, tab2 = st.tabs(
[
"📊 Analytics",
"📈 Insights"
]
)


# ==================================================
# TAB 1
# ==================================================

with tab1:

    left, right = st.columns(
        2
    )

    with left:

        render_top_teams_chart(
            filtered
        )

    with right:

        render_top_players_chart(
            filtered
        )


# ==================================================
# TAB 2
# ==================================================

with tab2:

    left, right = st.columns(
        2
    )

    with left:

        render_toss_impact_chart(
            filtered
        )

    with right:

        render_matches_per_season_chart(
            filtered
        )


# ==================================================
# FOOTER
# ==================================================

st.markdown(
"""
<div style="
text-align:center;
opacity:0.78;
margin-top:-90px;
padding-bottom:8px;
">

<div style="
font-size:20px;
font-weight:600;
color:#f2f2f2;
">
Built & Designed by Zavil Huda Quraishi
</div>

<br>

<div style="
font-size:13px;
color:#9ea6b2;
">
Data • Design • Intelligence
</div>

</div>
""",
unsafe_allow_html=True,
)