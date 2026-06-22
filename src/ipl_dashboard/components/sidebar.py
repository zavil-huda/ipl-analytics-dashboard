import streamlit as st


def render_sidebar(matches):

    st.sidebar.markdown(
        """
<style>

section[data-testid="stSidebar"]{

background:
linear-gradient(
180deg,
#020817,
#071225
);

border-right:
1px solid rgba(255,255,255,.06);

}

.sidebar-title{

font-size:28px;

font-weight:700;

margin-bottom:18px;

}

.sidebar-caption{

font-size:13px;

opacity:.7;

margin-bottom:24px;

}

div[data-baseweb="select"]{

border-radius:14px;

}

</style>
""",
        unsafe_allow_html=True,
    )

    st.sidebar.markdown(
        """
<div class='sidebar-title'>
⚙️ Filters
</div>

<div class='sidebar-caption'>
Explore IPL seasons
</div>
""",
        unsafe_allow_html=True,
    )

    seasons = sorted(
        matches["season"]
        .dropna()
        .astype(int)
        .unique()
        .tolist()
    )

    selected = st.sidebar.selectbox(
        "Season",
        ["All"] + seasons,
        index=0,
    )

    st.sidebar.markdown("---")

    total = len(matches)

    st.sidebar.caption(
        f"Loaded {total:,} records"
    )

    return {
        "season": selected
    }
