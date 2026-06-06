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
        soft = "#111827"
        nav = "rgba(2, 6, 23, 0.92)"
    else:
        bg = "#f8fafc"
        card = "#ffffff"
        text = "#0f172a"
        muted = "#64748b"
        border = "#e2e8f0"
        soft = "#eef2ff"
        nav = "rgba(255,255,255,0.94)"

    st.markdown(f"""
    <style>

    .stApp {{
        background:
            radial-gradient(circle at top left, rgba(30,58,138,0.08), transparent 28%),
            linear-gradient(180deg, {bg} 0%, #ffffff 100%);
        color: {text};
    }}

    .block-container {{
        max-width: 1480px;
        padding-top: 1rem;
        padding-bottom: 0;
    }}

    section[data-testid="stSidebar"] {{
        background: #0f172a;
        border-right: 1px solid rgba(255,255,255,0.08);
    }}

    section[data-testid="stSidebar"] * {{
        color: white !important;
    }}

    h1, h2, h3, h4, h5, h6, p, label {{
        color: {text};
    }}

    a {{
        text-decoration: none !important;
    }}

    /* TOP NAVIGATION */

    .arch-topbar {{
        position: sticky;
        top: 0;
        z-index: 999;
        background: {nav};
        backdrop-filter: blur(18px);
        border: 1px solid {border};
        border-radius: 24px;
        padding: 14px 22px;
        margin-bottom: 30px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0 18px 45px rgba(15,23,42,0.10);
    }}

    .arch-logo {{
        display: flex;
        align-items: center;
        gap: 13px;
    }}

    .arch-logo-mark {{
        width: 44px;
        height: 44px;
        border-radius: 14px;
        background: linear-gradient(135deg, {primary}, #0f172a);
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 900;
        font-size: 24px;
        box-shadow: 0 10px 25px rgba(30,58,138,0.35);
    }}

    .arch-logo-title {{
        font-size: 23px;
        font-weight: 950;
        letter-spacing: -0.8px;
        color: {text};
    }}

    .arch-logo-subtitle {{
        font-size: 11px;
        color: {muted};
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.2px;
    }}

    .arch-menu {{
        display: flex;
        align-items: center;
        gap: 8px;
    }}

    .arch-menu-item {{
        position: relative;
        padding: 13px 14px;
        font-size: 14px;
        font-weight: 850;
        color: {text};
        border-radius: 14px;
        cursor: default;
        transition: all 0.2s ease;
    }}

    .arch-menu-item:hover {{
        background: {soft};
        color: {primary};
    }}

    .arch-dropdown {{
        opacity: 0;
        visibility: hidden;
        transform: translateY(12px);
        transition: all 0.22s ease;
        position: absolute;
        top: 46px;
        left: 0;
        min-width: 230px;
        background: {card};
        border: 1px solid {border};
        border-radius: 18px;
        padding: 10px;
        box-shadow: 0 24px 55px rgba(15,23,42,0.18);
        z-index: 9999;
    }}

    .arch-menu-item:hover .arch-dropdown {{
        opacity: 1;
        visibility: visible;
        transform: translateY(0);
    }}

    .arch-dropdown a {{
        display: block;
        color: {text};
        padding: 11px 13px;
        border-radius: 12px;
        font-size: 14px;
        font-weight: 750;
    }}

    .arch-dropdown a:hover {{
        background: {soft};
        color: {primary};
    }}

    .arch-login-btn {{
        display: inline-block;
        background: {primary};
        color: white !important;
        padding: 11px 19px;
        border-radius: 999px;
        font-size: 14px;
        font-weight: 900;
        box-shadow: 0 10px 24px rgba(30,58,138,0.28);
    }}

    /* SIDEBAR */

    .side-brand {{
        display: flex;
        gap: 12px;
        align-items: center;
        margin-bottom: 28px;
    }}

    .side-logo {{
        width: 42px;
        height: 42px;
        border-radius: 14px;
        background: white;
        color: #0f172a !important;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 950;
        font-size: 24px;
    }}

    .side-title {{
        font-size: 22px;
        font-weight: 950;
    }}

    .side-subtitle {{
        font-size: 11px;
        color: #94a3b8 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}

    .side-section-title {{
        margin-top: 25px;
        margin-bottom: 10px;
        font-size: 12px;
        color: #94a3b8 !important;
        text-transform: uppercase;
        letter-spacing: 1.4px;
        font-weight: 900;
    }}

    .side-link {{
        display: block;
        padding: 11px 13px;
        border-radius: 13px;
        color: #e2e8f0 !important;
        font-weight: 800;
        margin-bottom: 5px;
    }}

    .side-link:hover {{
        background: rgba(255,255,255,0.10);
    }}

    .side-status {{
        background: rgba(255,255,255,0.08);
        border-radius: 14px;
        padding: 13px;
        display: flex;
        gap: 9px;
        align-items: center;
        font-size: 14px;
        font-weight: 800;
    }}

    .side-status span {{
        width: 10px;
        height: 10px;
        background: #22c55e;
        border-radius: 50%;
        display: inline-block;
    }}

    /* HERO */

    .hero-platform {{
        background:
            linear-gradient(120deg, rgba(15,23,42,0.95), rgba(30,58,138,0.94)),
            radial-gradient(circle at top right, rgba(255,255,255,0.18), transparent 36%);
        color: white;
        padding: 76px 66px;
        border-radius: 40px;
        box-shadow: 0 30px 80px rgba(15,23,42,0.28);
        margin-bottom: 34px;
        position: relative;
        overflow: hidden;
    }}

    .hero-platform::after {{
        content: "";
        position: absolute;
        right: -100px;
        bottom: -120px;
        width: 360px;
        height: 360px;
        border-radius: 50%;
        background: rgba(255,255,255,0.08);
    }}

    .hero-badge {{
        display: inline-block;
        background: rgba(255,255,255,0.13);
        border: 1px solid rgba(255,255,255,0.22);
        color: white;
        padding: 9px 15px;
        border-radius: 999px;
        font-size: 13px;
        font-weight: 900;
        letter-spacing: 1px;
        margin-bottom: 20px;
    }}

    .hero-platform h1 {{
        color: white;
        font-size: 60px;
        max-width: 900px;
        line-height: 1.03;
        letter-spacing: -1.8px;
        margin-bottom: 20px;
    }}

    .hero-platform p {{
        color: #dbeafe;
        font-size: 19px;
        line-height: 1.68;
        max-width: 790px;
    }}

    .hero-actions {{
        margin-top: 30px;
        display: flex;
        gap: 15px;
        flex-wrap: wrap;
    }}

    .hero-primary, .hero-secondary {{
        display: inline-block;
        padding: 14px 22px;
        border-radius: 16px;
        font-weight: 950;
    }}

    .hero-primary {{
        background: white;
        color: {primary};
    }}

    .hero-secondary {{
        background: rgba(255,255,255,0.12);
        color: white;
        border: 1px solid rgba(255,255,255,0.30);
    }}

    /* SECTIONS */

    .section-title {{
        font-size: 35px;
        font-weight: 950;
        margin-top: 38px;
        margin-bottom: 10px;
        letter-spacing: -1px;
    }}

    .section-subtitle {{
        color: {muted};
        font-size: 17px;
        line-height: 1.6;
        max-width: 850px;
        margin-bottom: 24px;
    }}

    /* MODULE CARDS */

    .module-card-link {{
        display: block;
    }}

    .module-card {{
        background: {card};
        border: 1px solid {border};
        border-left: 7px solid {primary};
        border-radius: 30px;
        padding: 28px;
        min-height: 235px;
        margin-bottom: 20px;
        box-shadow: 0 16px 42px rgba(15,23,42,0.09);
        transition: all 0.23s ease;
    }}

    .module-card:hover {{
        transform: translateY(-6px);
        box-shadow: 0 28px 70px rgba(15,23,42,0.16);
    }}

    .module-card-top {{
        display: flex;
        justify-content: space-between;
        align-items: center;
    }}

    .module-icon {{
        font-size: 32px;
    }}

    .module-card h3 {{
        font-size: 24px;
        margin-top: 18px;
        margin-bottom: 10px;
        font-weight: 950;
        color: {text};
    }}

    .module-card p {{
        color: {muted};
        font-size: 15.5px;
        line-height: 1.62;
    }}

    .module-arrow {{
        margin-top: 18px;
        color: {primary};
        font-weight: 950;
        font-size: 14px;
    }}

    .status-active, .status-soon {{
        display: inline-block;
        padding: 6px 12px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 950;
    }}

    .status-active {{
        background: #dcfce7;
        color: #166534;
    }}

    .status-soon {{
        background: #fef3c7;
        color: #92400e;
    }}

    /* METRICS */

    div[data-testid="stMetric"] {{
        background: {card};
        border: 1px solid {border};
        border-left: 7px solid {primary};
        padding: 23px;
        border-radius: 26px;
        box-shadow: 0 14px 36px rgba(15,23,42,0.08);
    }}

    /* FEATURE STRIP */

    .feature-strip {{
        background: {card};
        border: 1px solid {border};
        border-radius: 34px;
        padding: 34px;
        margin: 34px 0;
        box-shadow: 0 16px 42px rgba(15,23,42,0.08);
    }}

    .feature-strip h3 {{
        font-size: 30px;
        font-weight: 950;
    }}

    .feature-list {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 14px;
        margin-top: 20px;
    }}

    .feature-item {{
        background: rgba(30,58,138,0.08);
        border-radius: 18px;
        padding: 16px;
        font-weight: 900;
        color: {text};
    }}

    /* BUTTONS */

    .stButton > button {{
        background: {primary};
        color: white;
        border: none;
        border-radius: 15px;
        padding: 0.7rem 1.15rem;
        font-weight: 900;
    }}

    .stDownloadButton > button {{
        background: {primary};
        color: white;
        border: none;
        border-radius: 15px;
        font-weight: 900;
    }}

    /* FOOTER */

    .arch-footer {{
        margin-top: 70px;
        background: #0f172a;
        color: white;
        border-radius: 40px 40px 0 0;
        overflow: hidden;
    }}

    .footer-main {{
        padding: 52px;
        display: grid;
        grid-template-columns: 2fr 1fr 1fr 1fr;
        gap: 36px;
    }}

    .footer-main h2, .footer-main h4 {{
        color: white;
        margin-bottom: 14px;
    }}

    .footer-main p {{
        color: #cbd5e1;
        line-height: 1.6;
    }}

    .footer-main a {{
        display: block;
        color: #cbd5e1 !important;
        margin-bottom: 8px;
        font-size: 14px;
        font-weight: 700;
    }}

    .footer-main a:hover {{
        color: white !important;
    }}

    .footer-bottom {{
        background: #020617;
        color: #94a3b8;
        padding: 18px 52px;
        display: flex;
        justify-content: space-between;
        font-size: 13px;
        font-weight: 700;
    }}

    @media (max-width: 1100px) {{
        .arch-menu {{
            display: none;
        }}

        .hero-platform {{
            padding: 48px 32px;
        }}

        .hero-platform h1 {{
            font-size: 40px;
        }}

        .feature-list {{
            grid-template-columns: 1fr 1fr;
        }}

        .footer-main {{
            grid-template-columns: 1fr 1fr;
        }}
    }}

    @media (max-width: 700px) {{
        .feature-list {{
            grid-template-columns: 1fr;
        }}

        .footer-main {{
            grid-template-columns: 1fr;
        }}

        .footer-bottom {{
            flex-direction: column;
            gap: 8px;
        }}
    }}

    </style>
    """, unsafe_allow_html=True)