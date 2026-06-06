import streamlit as st


# =========================================================
# ARCHiTool GLOBAL STYLE SYSTEM
# Professional SaaS / AEC platform interface
# =========================================================


def apply_global_style():
    primary = st.session_state.get("primary_color", "#1e3a8a")
    dark = st.session_state.get("dark_mode", False)

    if dark:
        bg = "#020617"
        bg_2 = "#0f172a"
        card = "#0f172a"
        card_2 = "#111827"
        text = "#f8fafc"
        muted = "#94a3b8"
        border = "#1e293b"
        soft = "#111827"
        nav = "rgba(2, 6, 23, 0.94)"
        input_bg = "#111827"
        shadow = "rgba(0,0,0,0.35)"
    else:
        bg = "#f8fafc"
        bg_2 = "#ffffff"
        card = "#ffffff"
        card_2 = "#f8fafc"
        text = "#0f172a"
        muted = "#64748b"
        border = "#e2e8f0"
        soft = "#eef2ff"
        nav = "rgba(255,255,255,0.94)"
        input_bg = "#f1f5f9"
        shadow = "rgba(15,23,42,0.10)"

    st.markdown(f"""
    <style>

    /* =====================================================
       GLOBAL APP
    ===================================================== */

    .stApp {{
        background:
            radial-gradient(circle at top left, rgba(30,58,138,0.08), transparent 26%),
            radial-gradient(circle at top right, rgba(14,165,233,0.06), transparent 28%),
            linear-gradient(180deg, {bg} 0%, {bg_2} 100%);
        color: {text};
        font-family: "Inter", "Segoe UI", Arial, sans-serif;
    }}

    .block-container {{
        max-width: 1480px;
        padding-top: 1rem;
        padding-bottom: 0;
    }}

    h1, h2, h3, h4, h5, h6, p, label, span {{
        color: {text};
    }}

    a {{
        text-decoration: none !important;
    }}

    hr {{
        border: none;
        border-top: 1px solid {border};
        margin: 2rem 0;
    }}

    /* Hide default Streamlit footer/header noise */
    footer {{
        visibility: hidden;
    }}

    #MainMenu {{
        visibility: hidden;
    }}

    /* =====================================================
       SIDEBAR
    ===================================================== */

    section[data-testid="stSidebar"] {{
        background:
            linear-gradient(180deg, #0f172a 0%, #020617 100%);
        border-right: 1px solid rgba(255,255,255,0.08);
    }}

    section[data-testid="stSidebar"] * {{
        color: white !important;
    }}

    .side-brand {{
        display: flex;
        gap: 12px;
        align-items: center;
        margin-bottom: 30px;
        padding-top: 8px;
    }}

    .side-logo {{
        width: 46px;
        height: 46px;
        border-radius: 15px;
        background: linear-gradient(135deg, #ffffff, #dbeafe);
        color: #0f172a !important;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 950;
        font-size: 25px;
        box-shadow: 0 12px 30px rgba(255,255,255,0.12);
    }}

    .side-title {{
        font-size: 23px;
        font-weight: 950;
        letter-spacing: -0.8px;
    }}

    .side-subtitle {{
        font-size: 11px;
        color: #94a3b8 !important;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        font-weight: 800;
    }}

    .side-section-title {{
        margin-top: 26px;
        margin-bottom: 10px;
        font-size: 12px;
        color: #94a3b8 !important;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        font-weight: 950;
    }}

    .side-link {{
        display: block;
        padding: 12px 14px;
        border-radius: 14px;
        color: #e2e8f0 !important;
        font-weight: 850;
        margin-bottom: 6px;
        transition: all 0.18s ease;
    }}

    .side-link:hover {{
        background: rgba(255,255,255,0.11);
        transform: translateX(3px);
    }}

    .side-status {{
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 16px;
        padding: 14px;
        display: flex;
        gap: 10px;
        align-items: center;
        font-size: 14px;
        font-weight: 850;
    }}

    .side-status span {{
        width: 10px;
        height: 10px;
        background: #22c55e;
        border-radius: 50%;
        display: inline-block;
        box-shadow: 0 0 0 4px rgba(34,197,94,0.15);
    }}

    .side-mini-card {{
        margin-top: 14px;
        background: rgba(255,255,255,0.07);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 16px;
        padding: 14px;
    }}

    .side-mini-card strong {{
        font-size: 13px;
        color: #cbd5e1 !important;
    }}

    .side-mini-card p {{
        margin: 5px 0 0 0;
        color: white !important;
        font-weight: 900;
    }}

    /* =====================================================
       TOP NAVIGATION / HOVER DROPDOWN
    ===================================================== */

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
        box-shadow: 0 18px 45px {shadow};
    }}

    .arch-logo-link {{
        display: block;
    }}

    .arch-logo {{
        display: flex;
        align-items: center;
        gap: 13px;
    }}

    .arch-logo-mark {{
        width: 46px;
        height: 46px;
        border-radius: 15px;
        background: linear-gradient(135deg, {primary}, #0f172a);
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 950;
        font-size: 25px;
        box-shadow: 0 12px 28px rgba(30,58,138,0.35);
    }}

    .arch-logo-title {{
        font-size: 24px;
        font-weight: 950;
        letter-spacing: -0.9px;
        color: {text};
    }}

    .arch-logo-subtitle {{
        font-size: 11px;
        color: {muted};
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1.3px;
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
        font-weight: 900;
        color: {text};
        border-radius: 14px;
        cursor: default;
        transition: all 0.2s ease;
        white-space: nowrap;
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
        background: {card};
        border: 1px solid {border};
        border-radius: 18px;
        padding: 10px;
        box-shadow: 0 24px 55px rgba(15,23,42,0.18);
        z-index: 9999;
    }}

    .mega-small {{
        min-width: 220px;
    }}

    .mega-medium {{
        min-width: 270px;
    }}

    .arch-menu-item:hover .arch-dropdown {{
        opacity: 1;
        visibility: visible;
        transform: translateY(0);
    }}

    .arch-dropdown a {{
        display: block;
        color: {text};
        padding: 12px 13px;
        border-radius: 12px;
        font-size: 14px;
        font-weight: 800;
        transition: all 0.18s ease;
    }}

    .arch-dropdown a:hover {{
        background: {soft};
        color: {primary};
        transform: translateX(3px);
    }}

    .arch-login-btn {{
        display: inline-block;
        background: {primary};
        color: white !important;
        padding: 11px 20px;
        border-radius: 999px;
        font-size: 14px;
        font-weight: 950;
        box-shadow: 0 12px 26px rgba(30,58,138,0.28);
        transition: all 0.18s ease;
    }}

    .arch-login-btn:hover {{
        transform: translateY(-2px);
        box-shadow: 0 18px 34px rgba(30,58,138,0.36);
    }}

    /* =====================================================
       HERO
    ===================================================== */

    .hero-platform {{
        background:
            linear-gradient(120deg, rgba(15,23,42,0.96), rgba(30,58,138,0.94)),
            radial-gradient(circle at top right, rgba(255,255,255,0.18), transparent 36%);
        color: white;
        padding: 78px 68px;
        border-radius: 42px;
        box-shadow: 0 32px 85px rgba(15,23,42,0.30);
        margin-bottom: 36px;
        position: relative;
        overflow: hidden;
    }}

    .hero-platform::before {{
        content: "";
        position: absolute;
        left: -120px;
        top: -140px;
        width: 380px;
        height: 380px;
        border-radius: 50%;
        background: rgba(255,255,255,0.055);
    }}

    .hero-platform::after {{
        content: "";
        position: absolute;
        right: -100px;
        bottom: -120px;
        width: 360px;
        height: 360px;
        border-radius: 50%;
        background: rgba(255,255,255,0.075);
    }}

    .hero-badge {{
        display: inline-block;
        background: rgba(255,255,255,0.13);
        border: 1px solid rgba(255,255,255,0.22);
        color: white;
        padding: 9px 15px;
        border-radius: 999px;
        font-size: 13px;
        font-weight: 950;
        letter-spacing: 1px;
        margin-bottom: 20px;
        position: relative;
        z-index: 2;
    }}

    .hero-platform h1 {{
        color: white;
        font-size: 62px;
        max-width: 930px;
        line-height: 1.03;
        letter-spacing: -2px;
        margin-bottom: 20px;
        position: relative;
        z-index: 2;
    }}

    .hero-platform p {{
        color: #dbeafe;
        font-size: 19px;
        line-height: 1.68;
        max-width: 820px;
        position: relative;
        z-index: 2;
    }}

    .hero-actions {{
        margin-top: 30px;
        display: flex;
        gap: 15px;
        flex-wrap: wrap;
        position: relative;
        z-index: 2;
    }}

    .hero-primary, .hero-secondary {{
        display: inline-block;
        padding: 14px 22px;
        border-radius: 16px;
        font-weight: 950;
        transition: all 0.18s ease;
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

    .hero-primary:hover,
    .hero-secondary:hover {{
        transform: translateY(-3px);
    }}

    /* =====================================================
       SECTIONS
    ===================================================== */

    .section-title {{
        font-size: 36px;
        font-weight: 950;
        margin-top: 40px;
        margin-bottom: 10px;
        letter-spacing: -1px;
    }}

    .section-subtitle {{
        color: {muted};
        font-size: 17px;
        line-height: 1.65;
        max-width: 880px;
        margin-bottom: 25px;
    }}

    /* =====================================================
       MODULE CARDS
    ===================================================== */

    .module-card-link {{
        display: block;
    }}

    .module-card {{
        background: {card};
        border: 1px solid {border};
        border-left: 7px solid {primary};
        border-radius: 30px;
        padding: 29px;
        min-height: 245px;
        margin-bottom: 22px;
        box-shadow: 0 16px 42px {shadow};
        transition: all 0.23s ease;
        position: relative;
        overflow: hidden;
    }}

    .module-card::after {{
        content: "";
        position: absolute;
        right: -80px;
        bottom: -90px;
        width: 180px;
        height: 180px;
        border-radius: 50%;
        background: rgba(30,58,138,0.06);
    }}

    .module-card:hover {{
        transform: translateY(-7px);
        box-shadow: 0 30px 75px rgba(15,23,42,0.17);
    }}

    .module-card-top {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        position: relative;
        z-index: 2;
    }}

    .module-icon {{
        font-size: 34px;
    }}

    .module-card h3 {{
        font-size: 25px;
        margin-top: 18px;
        margin-bottom: 10px;
        font-weight: 950;
        color: {text};
        position: relative;
        z-index: 2;
    }}

    .module-card p {{
        color: {muted};
        font-size: 15.5px;
        line-height: 1.65;
        position: relative;
        z-index: 2;
    }}

    .module-arrow {{
        margin-top: 18px;
        color: {primary};
        font-weight: 950;
        font-size: 14px;
        position: relative;
        z-index: 2;
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

    /* =====================================================
       METRICS
    ===================================================== */

    div[data-testid="stMetric"] {{
        background: {card};
        border: 1px solid {border};
        border-left: 7px solid {primary};
        padding: 23px;
        border-radius: 26px;
        box-shadow: 0 14px 36px {shadow};
    }}

    div[data-testid="stMetricValue"] {{
        font-weight: 950;
        letter-spacing: -0.7px;
    }}

    /* =====================================================
       FEATURE STRIP
    ===================================================== */

    .feature-strip {{
        background: {card};
        border: 1px solid {border};
        border-radius: 34px;
        padding: 36px;
        margin: 36px 0;
        box-shadow: 0 16px 42px {shadow};
    }}

    .feature-strip h3 {{
        font-size: 31px;
        font-weight: 950;
        margin-bottom: 10px;
    }}

    .feature-strip p {{
        color: {muted};
        line-height: 1.65;
        font-size: 16px;
    }}

    .feature-list {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 14px;
        margin-top: 22px;
    }}

    .feature-item {{
        background: rgba(30,58,138,0.08);
        border: 1px solid rgba(30,58,138,0.08);
        border-radius: 18px;
        padding: 16px;
        font-weight: 900;
        color: {text};
    }}

    /* =====================================================
       INFO PANEL / BANNER
    ===================================================== */

    .info-panel {{
        background: {card};
        border: 1px solid {border};
        border-radius: 26px;
        padding: 24px;
        display: flex;
        gap: 18px;
        align-items: flex-start;
        box-shadow: 0 14px 36px {shadow};
        margin: 20px 0;
    }}

    .info-panel-icon {{
        width: 46px;
        height: 46px;
        border-radius: 14px;
        background: {soft};
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
    }}

    .info-panel h3 {{
        margin: 0 0 8px 0;
        font-weight: 950;
    }}

    .info-panel p {{
        margin: 0;
        color: {muted};
        line-height: 1.6;
    }}

    .premium-banner {{
        background: linear-gradient(135deg, {primary}, #0f172a);
        color: white;
        border-radius: 30px;
        padding: 34px;
        margin: 28px 0;
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 24px;
        box-shadow: 0 24px 60px rgba(15,23,42,0.24);
    }}

    .premium-banner h2 {{
        color: white;
        margin-bottom: 8px;
    }}

    .premium-banner p {{
        color: #dbeafe;
        margin: 0;
    }}

    .banner-button {{
        background: white;
        color: {primary} !important;
        padding: 13px 22px;
        border-radius: 15px;
        font-weight: 950;
        white-space: nowrap;
    }}

    /* =====================================================
       STREAMLIT INPUTS / BUTTONS
    ===================================================== */

    .stTextInput input,
    .stNumberInput input,
    .stTextArea textarea,
    .stDateInput input,
    .stSelectbox div[data-baseweb="select"] {{
        background-color: {input_bg} !important;
        border-radius: 14px !important;
        border: 1px solid {border} !important;
    }}

    .stButton > button {{
        background: {primary};
        color: white;
        border: none;
        border-radius: 15px;
        padding: 0.7rem 1.15rem;
        font-weight: 900;
        transition: all 0.18s ease;
    }}

    .stButton > button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 12px 24px rgba(30,58,138,0.28);
    }}

    .stDownloadButton > button {{
        background: {primary};
        color: white;
        border: none;
        border-radius: 15px;
        font-weight: 900;
    }}

    /* =====================================================
       FOOTER
    ===================================================== */

    .arch-footer {{
        margin-top: 76px;
        background: #0f172a;
        color: white;
        border-radius: 42px 42px 0 0;
        overflow: hidden;
        box-shadow: 0 -20px 60px rgba(15,23,42,0.18);
    }}

    .footer-main {{
        padding: 54px;
        display: grid;
        grid-template-columns: 2fr 1fr 1fr 1fr;
        gap: 38px;
    }}

    .footer-main h2, .footer-main h4 {{
        color: white;
        margin-bottom: 14px;
    }}

    .footer-main p {{
        color: #cbd5e1;
        line-height: 1.65;
    }}

    .footer-main a {{
        display: block;
        color: #cbd5e1 !important;
        margin-bottom: 9px;
        font-size: 14px;
        font-weight: 750;
    }}

    .footer-main a:hover {{
        color: white !important;
    }}

    .footer-bottom {{
        background: #020617;
        color: #94a3b8;
        padding: 18px 54px;
        display: flex;
        justify-content: space-between;
        font-size: 13px;
        font-weight: 800;
    }}

    /* =====================================================
       RESPONSIVE
    ===================================================== */

    @media (max-width: 1200px) {{
        .arch-menu {{
            display: none;
        }}

        .hero-platform {{
            padding: 56px 38px;
        }}

        .hero-platform h1 {{
            font-size: 46px;
        }}

        .feature-list {{
            grid-template-columns: repeat(2, 1fr);
        }}

        .footer-main {{
            grid-template-columns: 1fr 1fr;
        }}
    }}

    @media (max-width: 760px) {{
        .arch-topbar {{
            flex-direction: column;
            align-items: flex-start;
            gap: 16px;
        }}

        .hero-platform {{
            padding: 42px 28px;
            border-radius: 30px;
        }}

        .hero-platform h1 {{
            font-size: 35px;
        }}

        .hero-platform p {{
            font-size: 16px;
        }}

        .feature-list {{
            grid-template-columns: 1fr;
        }}

        .footer-main {{
            grid-template-columns: 1fr;
            padding: 36px;
        }}

        .footer-bottom {{
            flex-direction: column;
            gap: 8px;
            padding: 18px 36px;
        }}

        .premium-banner {{
            flex-direction: column;
            align-items: flex-start;
        }}
    }}

    </style>
    """, unsafe_allow_html=True)