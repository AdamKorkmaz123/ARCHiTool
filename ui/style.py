import streamlit as st


def apply_global_style():
    primary = st.session_state.get("primary_color", "#1e3a8a")
    dark = st.session_state.get("dark_mode", False)

    if dark:
        bg = "#020617"
        card = "#0f172a"
        text = "#f8fafc"
        muted = "#94a3b8"
        border = "#1e293b"
        sidebar = "#020617"
    else:
        bg = "#f8fafc"
        card = "#ffffff"
        text = "#0f172a"
        muted = "#64748b"
        border = "#e2e8f0"
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

    .hero-card {{
        background: linear-gradient(135deg, {primary} 0%, #0f172a 100%);
        color: white;
        padding: 48px;
        border-radius: 32px;
        margin-bottom: 30px;
        box-shadow: 0 18px 45px rgba(15, 23, 42, 0.20);
    }}

    .hero-card h1 {{
        font-size: 48px;
        margin-bottom: 10px;
        color: white;
    }}

    .hero-card p {{
        font-size: 18px;
        color: #e2e8f0;
    }}

    .module-card {{
        background: {card};
        border: 1px solid {border};
        border-left: 6px solid {primary};
        padding: 24px;
        border-radius: 24px;
        margin-bottom: 18px;
        box-shadow: 0 10px 30px rgba(15, 23, 42, 0.08);
        min-height: 170px;
    }}

    .module-card h3 {{
        margin-bottom: 8px;
    }}

    .module-card p {{
        color: {muted};
        font-size: 15px;
    }}

    .status-active {{
        display: inline-block;
        background: #dcfce7;
        color: #166534;
        padding: 4px 10px;
        border-radius: 999px;
        font-size: 13px;
        font-weight: 600;
    }}

    .status-soon {{
        display: inline-block;
        background: #fef3c7;
        color: #92400e;
        padding: 4px 10px;
        border-radius: 999px;
        font-size: 13px;
        font-weight: 600;
    }}

    .section-title {{
        font-size: 30px;
        font-weight: 800;
        margin-top: 30px;
        margin-bottom: 16px;
    }}

    div[data-testid="stMetric"] {{
        background: {card};
        padding: 20px;
        border-radius: 20px;
        border-left: 6px solid {primary};
        box-shadow: 0 8px 25px rgba(15, 23, 42, 0.08);
    }}

    .stButton > button {{
        background: {primary};
        color: white;
        border-radius: 12px;
        border: none;
        padding: 0.6rem 1rem;
        font-weight: 600;
    }}

    .stDownloadButton > button {{
        background: {primary};
        color: white;
        border-radius: 12px;
        border: none;
    }}

    .top-note {{
        background: {card};
        border: 1px solid {border};
        padding: 18px;
        border-radius: 18px;
        color: {muted};
        margin-bottom: 24px;
    }}
    </style>
    """, unsafe_allow_html=True)