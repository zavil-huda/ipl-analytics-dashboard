import streamlit as st
import plotly.express as px


# =========================
# COMMON
# =========================

def apply_style(fig):

    fig.update_layout(

        template="plotly_dark",

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        margin=dict(
            l=10,
            r=10,
            t=20,
            b=10
        ),

        height=440,

        showlegend=False,

        font=dict(
            size=13
        ),

        hoverlabel=dict(
            bgcolor="#0f172a"
        ),

        xaxis=dict(
            showgrid=False,
            zeroline=False
        ),

        yaxis=dict(
            gridcolor=
            "rgba(255,255,255,.05)"
        )
    )

    return fig


# =========================
# TEAMS
# =========================

def render_top_teams_chart(matches):

    st.subheader(
        "🏆 Top Teams"
    )

    df = (
        matches["winner"]
        .dropna()
        .value_counts()
        .head(10)
        .reset_index()
    )

    df.columns = [
        "Team",
        "Wins"
    ]

    fig = px.bar(

        df,

        x="Wins",

        y="Team",

        orientation="h",

        text="Wins",

        color="Wins",

        color_continuous_scale="Blues"

    )

    apply_style(fig)

    fig.update_traces(
        textposition="outside"
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={
            "displayModeBar":
            False
        }
    )


# =========================
# PLAYERS
# =========================

def render_top_players_chart(matches):

    st.subheader(
        "⭐ Top Players"
    )

    df = (
        matches[
            "player_of_match"
        ]
        .dropna()
        .value_counts()
        .head(10)
        .reset_index()
    )

    df.columns = [
        "Player",
        "Awards"
    ]

    fig = px.bar(

        df,

        x="Awards",

        y="Player",

        orientation="h",

        text="Awards",

        color="Awards",

        color_continuous_scale=
        "Oranges"

    )

    apply_style(fig)

    fig.update_traces(
        textposition="outside"
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={
            "displayModeBar":
            False
        }
    )


# =========================
# TOSS
# =========================

def render_toss_impact_chart(matches):

    st.subheader(
        "🪙 Toss Impact"
    )

    temp = (
        matches
        .dropna(
            subset=[
                "winner",
                "toss_winner"
            ]
        )
    )

    temp[
        "Outcome"
    ] = (
        temp[
            "winner"
        ]
        ==
        temp[
            "toss_winner"
        ]
    )

    pie = (
        temp[
            "Outcome"
        ]
        .value_counts()
        .reset_index()
    )

    pie.columns = [
        "Result",
        "Matches"
    ]

    pie[
        "Result"
    ] = (
        pie[
            "Result"
        ]
        .map({

            True:
            "Won Toss",

            False:
            "Lost After Toss"

        })
    )

    fig = px.pie(

        pie,

        values=
        "Matches",

        names=
        "Result",

        hole=.72,

        color=
        "Result",

        color_discrete_map={

            "Won Toss":
            "#10b981",

            "Lost After Toss":
            "#ef4444"

        }
    )

    fig.update_traces(
        textinfo=
        "percent"
    )

    fig.update_layout(

        template=
        "plotly_dark",

        paper_bgcolor=
        "rgba(0,0,0,0)",

        height=440
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={
            "displayModeBar":
            False
        }
    )


# =========================
# MATCH TREND
# =========================

def render_matches_per_season_chart(matches):

    st.subheader(
        "📈 Match Trends"
    )

    if (
        matches[
            "season"
        ]
        .nunique()
        <=
        1
    ):

        st.info(
            "Select ALL"
        )

        return

    trend = (

        matches

        .groupby(
            "season"
        )

        .size()

        .reset_index(
            name=
            "Matches"
        )
    )

    fig = px.area(

        trend,

        x=
        "season",

        y=
        "Matches",

        markers=
        True
    )

    fig.update_layout(

        template=
        "plotly_dark",

        paper_bgcolor=
        "rgba(0,0,0,0)",

        plot_bgcolor=
        "rgba(0,0,0,0)",

        height=
        440
    )

    st.plotly_chart(

        fig,

        use_container_width=
        True,

        config={
            "displayModeBar":
            False
        }
    )