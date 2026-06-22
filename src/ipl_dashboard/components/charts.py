import streamlit as st
import plotly.express as px


# =====================================
# COMMON STYLE
# =====================================

def style_chart(fig):

    fig.update_layout(

        template="plotly_dark",

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        height=430,

        margin=dict(
            l=20,
            r=20,
            t=40,
            b=20
        ),

        font=dict(
            size=12
        ),

        coloraxis_showscale=False,

        xaxis=dict(
            automargin=True,
            showgrid=False
        ),

        yaxis=dict(
            automargin=True,
            gridcolor="rgba(255,255,255,.06)"
        ),
    )

    fig.update_traces(
        cliponaxis=False
    )

    return fig


# =====================================
# TOP TEAMS
# =====================================

def render_top_teams_chart(matches):

    st.subheader(
        "🏆 Top Teams"
    )

    data = (
        matches["winner"]
        .dropna()
        .value_counts()
        .head(10)
        .sort_values()
        .reset_index()
    )

    data.columns = [
        "Team",
        "Wins"
    ]

    fig = px.bar(

        data,

        x="Wins",

        y="Team",

        orientation="h",

        text="Wins",

        color="Wins",

        color_continuous_scale="Blues",
    )

    fig.update_traces(
        textposition="inside"
    )

    style_chart(fig)

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={
            "displayModeBar": False
        }
    )


# =====================================
# TOP PLAYERS
# =====================================

def render_top_players_chart(matches):

    st.subheader(
        "⭐ Top Players"
    )

    data = (
        matches["player_of_match"]
        .dropna()
        .value_counts()
        .head(10)
        .sort_values()
        .reset_index()
    )

    data.columns = [
        "Player",
        "Awards"
    ]

    fig = px.bar(

        data,

        x="Awards",

        y="Player",

        orientation="h",

        text="Awards",

        color="Awards",

        color_continuous_scale="Oranges",
    )

    fig.update_traces(
        textposition="inside"
    )

    style_chart(fig)

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={
            "displayModeBar": False
        }
    )


# =====================================
# TOSS IMPACT
# =====================================

def render_toss_impact_chart(matches):

    st.subheader(
        "🪙 Toss Impact"
    )

    df = matches.dropna(
        subset=[
            "winner",
            "toss_winner"
        ]
    )

    result = (
        (
            df["winner"]
            ==
            df["toss_winner"]
        )
        .value_counts()
        .reset_index()
    )

    result.columns = [
        "Result",
        "Matches"
    ]

    result["Result"] = result[
        "Result"
    ].map({

        True:
        "Won Toss",

        False:
        "Lost Toss"

    })

    fig = px.pie(

        result,

        names="Result",

        values="Matches",

        hole=.55,

        color="Result",

        color_discrete_map={

            "Won Toss":
            "#22c55e",

            "Lost Toss":
            "#ef4444"
        }
    )

    fig.update_layout(

        template="plotly_dark",

        height=430,

        showlegend=True,

        paper_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )


# =====================================
# MATCH TRENDS
# =====================================

def render_matches_per_season_chart(matches):

    st.subheader(
        "📈 Match Trends"
    )

    chart = (

        matches

        .groupby(
            "season"
        )

        .size()

        .reset_index(
            name="Matches"
        )
    )

    fig = px.line(

        chart,

        x="season",

        y="Matches",

        markers=True
    )

    fig.update_traces(
        line_width=4
    )

    fig.update_layout(

        template="plotly_dark",

        height=430,

        paper_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )