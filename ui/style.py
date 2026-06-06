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
        nav_bg = "rgba(2, 6, 23, 0.92)"
    else:
        bg = "#f8fafc"
        card = "#ffffff"
        text = "#0f172a"
        muted = "#64748b"
        border = "#e2e8f0"
        sidebar = "#0f172a"
        nav_bg = "rgba(255, 255, 255, 0.92)"

    st.markdown(f"""
    <style>

    .stApp {{
        background: {bg};
        color: {text};
    }}

    .block-container {{
        padding-top: 1.2rem;
        max-width: 1400px;
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

    .top-nav {{
        position: sticky;
        top: 0;
        z-index: 100;
        background: {nav_bg};
        backdrop-filter: blur(14px);
        border: 1px solid {border};
        border-radius: 22px;
        padding: 16px 24px;
        margin-bottom: 28px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0 10px 35px rgba(15, 23, 42, 0.08);
    }}

    .brand {{
        display: flex;
        align-items: center;
        gap: 12px;
        font-weight: 900;
        font-size: 24px;
        color: {text};
    }}

    .brand-icon {{
        font-size: 30px;
    }}

    .brand-text {{
        letter-spacing: -0.5px;
    }}

    .nav-links {{
        display: flex;
        gap: 22px;
        font-weight: 700;
        font-size: 14px;
        color: {muted};
    }}

    .nav-links span {{
        cursor: default;
        white-space: nowrap;
    }}

    .nav-action {{
        display: flex;
        align-items: center;
    }}

    .login-pill {{
        background: {primary};
        color: white;
        padding: 9px 18px;
        border-radius: 999px;
        font-weight: 800;
        font-size: 14px;
    }}

    .hero-platform {{
        background:
            linear-gradient(135deg, rgba(30, 58, 138, 0.92) 0%, rgba(15, 23, 42, 0.96) 100%),
            radial-gradient(circle at top right, rgba(255,255,255,0.18), transparent 40%);
        color: white;
        padding: 70px 60px;
        border-radius: 36px;
        margin-bottom: 36px;
        box-shadow: 0 24px 60px rgba(15, 23, 42, 0.25);
        position: relative;
        overflow: hidden;
    }}

    .hero-platform h1 {{
        color: white;
        font-size: 56px;
        line-height: 1.05;
        margin-bottom: 18px;
        max-width: 900px;
        letter-spacing: -1.5px;
    }}

    .hero-platform p {{
        color: #e2e8f0;
        font-size: 19px;
        max-width: 760px;
        line-height: 1.65;
    }}

    .hero-badge {{
        display: inline-block;
        background: rgba(255,255,255,0.14);
        color: white;
        padding: 8px 14px;
        border: 1px solid rgba(255,255,255,0.25);
        border-radius: 999px;
        font-size: 14px;
        font-weight: 800;
        margin-bottom: 18px;
    }}

    .hero-actions {{
        margin-top: 28px;
        display: flex;
        gap: 14px;
        flex-wrap: wrap;
    }}

    .hero-primary {{
        background: white;
        color: {primary};
        padding: 13px 22px;
        border-radius: 14px;
        font-weight: 900;
        display: inline-block;
    }}

    .hero-secondary {{
        background: rgba(255,255,255,0.12);
        color: white;
        border: 1px solid rgba(255,255,255,0.35);
        padding: 13px 22px;
        border-radius: 14px;
        font-weight: 800;
        display: inline-block;
    }}

    .section-title {{
        font-size: 34px;
        font-weight: 900;
        margin-top: 34px;
        margin-bottom: 12px;
        letter-spacing: -0.7px;
    }}

    .section-subtitle {{
        color: {muted};
        font-size: 17px;
        margin-bottom: 24px;
        max-width: 850px;
    }}

    .module-card {{
        background: {card};
        border: 1px solid {border};
        border-left: 7px solid {primary};
        padding: 28px;
        border-radius: 28px;
        margin-bottom: 18px;
        box-shadow: 0 14px 36px rgba(15, 23, 42, 0.08);
        min-height: 210px;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }}

    .module-card:hover {{
        transform: translateY(-4px);
        box-shadow: 0 22px 50px rgba(15, 23, 42, 0.14);
    }}

    .module-card h3 {{
        margin-top: 16px;
        margin-bottom: 10px;
        font-size: 23px;
        font-weight: 900;
    }}

    .module-card p {{
        color: {muted};
        font-size: 15.5px;
        line-height: 1.55;
    }}

    .status-active {{
        display: inline-block;
        background: #dcfce7;
        color: #166534;
        padding: 5px 12px;
        border-radius: 999px;
        font-size: 13px;
        font-weight: 800;
    }}

    .status-soon {{
        display: inline-block;
        background: #fef3c7;
        color: #92400e;
        padding: 5px 12px;
        border-radius: 999px;
        font-size: 13px;
        font-weight: 800;
    }}

    .feature-strip {{
        background: {card};
        border: 1px solid {border};
        border-radius: 28px;
        padding: 30px;
        margin: 30px 0;
        box-shadow: 0 14px 36px rgba(15, 23, 42, 0.07);
    }}

    .feature-strip h3 {{
        font-size: 28px;
        font-weight: 900;
    }}

    .feature-list {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 14px;
        margin-top: 18px;
    }}

    .feature-item {{
        background: rgba(30, 58, 138, 0.08);
        border-radius: 16px;
        padding: 14px;
        font-weight: 800;
        color: {text};
    }}

    div[data-testid="stMetric"] {{
        background: {card};
        padding: 22px;
        border-radius: 24px;
        border-left: 7px solid {primary};
        box-shadow: 0 12px 32px rgba(15, 23, 42, 0.08);
    }}

    .stButton > button {{
        background: {primary};
        color: white;
        border-radius: 14px;
        border: none;
        padding: 0.65rem 1.05rem;
        font-weight: 800;
    }}

    .stDownloadButton > button {{
        background: {primary};
        color: white;
        border-radius: 14px;
        border: none;
        font-weight: 800;
    }}

    .footer {{
        margin-top: 70px;
        background: #0f172a;
        color: white;
        border-radius: 34px 34px 0 0;
        padding: 46px;
        display: grid;
        grid-template-columns: 2fr 1fr 1fr 1fr;
        gap: 30px;
    }}

    .footer h3, .footer h4 {{
        color: white;
        margin-bottom: 12px;
    }}

    .footer p {{
        color: #cbd5e1;
        margin: 5px 0;
        font-size: 14px;
    }}

    .footer-bottom {{
        background: #020617;
        color: #94a3b8;
        padding: 16px 30px;
        border-radius: 0 0 24px 24px;
        font-size: 13px;
        margin-bottom: 20px;
    }}

    @media (max-width: 900px) {{
        .nav-links {{
            display: none;
        }}

        .hero-platform {{
            padding: 42px 28px;
        }}

        .hero-platform h1 {{
            font-size: 36px;
        }}

        .feature-list {{
            grid-template-columns: 1fr;
        }}

        .footer {{
            grid-template-columns: 1fr;
        }}
    }}

    </style>
    """, unsafe_allow_html=True)