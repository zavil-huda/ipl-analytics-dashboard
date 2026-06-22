import streamlit as st

from ipl_dashboard.metrics import (
    get_total_matches,
    get_total_seasons,
    get_most_successful_team,
    get_top_player,
)


def card(title, value, icon, glow):

    html = f"""
<div style="
position:relative;
background:linear-gradient(145deg,#111827,#091221);
border:1px solid rgba(255,255,255,.06);
border-radius:24px;
padding:24px;
height:170px;
overflow:hidden;
box-shadow:0 12px 40px rgba(0,0,0,.35);
">

<div style="
position:absolute;
top:-40px;
right:-40px;
width:140px;
height:140px;
background:{glow};
filter:blur(70px);
opacity:.45;
border-radius:50%;
">
</div>

<div style="
font-size:30px;
position:relative;
z-index:2;
">
{icon}
</div>

<div style="
margin-top:18px;
color:#8fa4c7;
font-size:13px;
letter-spacing:1px;
text-transform:uppercase;
position:relative;
z-index:2;
">
{title}
</div>

<div style="
margin-top:10px;
font-size:36px;
font-weight:800;
color:white;
position:relative;
z-index:2;
word-wrap:break-word;
">
{value}
</div>

</div>
"""

    st.markdown(
        html,
        unsafe_allow_html=True,
    )


def render_kpi_cards(matches):

    total_matches = get_total_matches(matches)
    total_seasons = get_total_seasons(matches)
    team = get_most_successful_team(matches)
    player = get_top_player(matches)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        card(
            "Total Matches",
            total_matches,
            "🏏",
            "#2563eb"
        )

    with c2:
        card(
            "Total Seasons",
            total_seasons,
            "📈",
            "#7c3aed"
        )

    with c3:
        card(
            "Top Team",
            team,
            "🏆",
            "#06b6d4"
        )

    with c4:
        card(
            "Top Player",
            player,
            "⭐",
            "#f97316"
        )