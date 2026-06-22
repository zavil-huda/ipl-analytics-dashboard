import streamlit as st

from ipl_dashboard.metrics import (
    get_total_matches,
    get_total_seasons,
    get_most_successful_team,
    get_top_player,
)


def _short(value, limit=18):

    value = str(value)

    if len(value) <= limit:
        return value

    return value[:limit] + "..."


def card(icon, title, value):

    st.markdown(
        f"""
<div class="metric-card">

<div class="metric-icon">
{icon}
</div>

<div class="metric-title">
{title}
</div>

<div class="metric-value">
{value}
</div>

</div>
""",
        unsafe_allow_html=True,
    )


def render_kpi_cards(matches):

    st.markdown(
        """
<style>

.metric-card{

background:
linear-gradient(
145deg,
rgba(15,23,42,.98),
rgba(4,10,22,.96)
);

border:
1px solid rgba(255,255,255,.06);

border-radius:24px;

padding:22px;

min-height:170px;

display:flex;

flex-direction:column;

justify-content:center;

overflow:hidden;

}

.metric-icon{

font-size:32px;

margin-bottom:16px;

}

.metric-title{

font-size:13px;

letter-spacing:1px;

text-transform:uppercase;

color:#93a3b8;

}

.metric-value{

margin-top:12px;

font-size:
clamp(
22px,
2vw,
36px
);

font-weight:800;

line-height:1.15;

overflow-wrap:anywhere;

word-break:break-word;

}

</style>
""",
        unsafe_allow_html=True,
    )

    total_matches = get_total_matches(matches)

    total_seasons = get_total_seasons(matches)

    team = _short(
        get_most_successful_team(matches)
    )

    player = _short(
        get_top_player(matches)
    )

    row1 = st.columns(2)

    with row1[0]:

        card(
            "🏏",
            "Total Matches",
            total_matches
        )

    with row1[1]:

        card(
            "📈",
            "Total Seasons",
            total_seasons
        )

    row2 = st.columns(2)

    with row2[0]:

        card(
            "🏆",
            "Top Team",
            team
        )

    with row2[1]:

        card(
            "⭐",
            "Top Player",
            player
        )