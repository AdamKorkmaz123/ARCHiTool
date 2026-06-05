import streamlit as st


def apply_global_style():
    primary = st.session_state.get("primary_color", "#1e3a8a")
    dark = st.session_state.get("dark_mode", False)

    if dark:
        bg = "#020617"
        card = "#0f172a"
        text = "#f8fafc"
        sidebar = "#020617"
    else:
        bg = "#f8fafc"
        card = "#ffffff"
        text = "#0f172a"
        sidebar = "#0f172a"

    st.markdown(f"""
    <style>
    .stApp {{
        background: {bg};
        color: {text};
    }}

    section[data-testid="stSidebar"] {{
        background: {sidebar};
    }}

    section[data-testid="stSidebar"] * {{
        color: white !important;
    }}

    h1, h2, h3, h4, h5, h6, p, label {{
        color: {text};
    }}

    div[data-testid="stMetric"] {{
        background: {card};
        padding: 20px;
        border-radius: 18px;
        border-left: 6px solid {primary};
        box-shadow: 0 8px 25px rgba(15, 23, 42, 0.08);
    }}

    .stButton > button {{
        background: {primary};
        color: white;
        border-radius: 10px;
        border: none;
        padding: 0.55rem 1rem;
    }}

    .stDownloadButton > button {{
        background: {primary};
        color: white;
        border-radius: 10px;
        border: none;
    }}

    .hero-card {{
        background: linear-gradient(135deg, {primary} 0%, #0f172a 100%);
        color: white;
        padding: 40px;
        border-radius: 28px;
        margin-bottom: 35px;
    }}

    .main-card {{
        background: {card};
        padding: 28px;
        border-radius: 22px;
        box-shadow: 0 12px 35px rgba(15, 23, 42, 0.08);
        margin-bottom: 28px;
    }}
    </style>
    """, unsafe_allow_html=True)