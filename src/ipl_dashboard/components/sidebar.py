import streamlit as st


def render_sidebar(matches):
    st.sidebar.title("Filters")

    season_options = ["All"] + sorted(matches["season"].dropna().unique().tolist())

    selected_season = st.sidebar.selectbox(
        "Select Season",
        season_options,
    )

    return {
        "season": selected_season,
    }