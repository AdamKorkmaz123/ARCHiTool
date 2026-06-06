import streamlit as st


# =========================================================
# ARCHiTool GLOBAL STYLE SYSTEM
# Tüm tasarım ayarlarını aşağıdaki bölümden değiştirebilirsin.
# =========================================================


def apply_global_style():

    # =====================================================
    # 1) ANA RENKLER
    # =====================================================

    # Ana marka rengi
    # Seçenekler:
    # Mavi: "#1e3a8a", "#2563eb", "#0f172a"
    # Kırmızı: "#8A1E20", "#b91c1c", "#dc2626"
    # Yeşil: "#0f766e", "#166534", "#15803d"
    # Siyah/Gri: "#111827", "#1f2937", "#374151"
    DEFAULT_PRIMARY = "#1e3a8a"

    # Açık tema renkleri
    LIGHT_BG = "#f8fafc"          # seçenek: "#ffffff", "#f8fafc", "#f1f5f9", "#eef2ff"
    LIGHT_BG_2 = "#ffffff"        # seçenek: "#ffffff", "#f8fafc", "#f1f5f9"
    LIGHT_CARD = "#ffffff"        # seçenek: "#ffffff", "#f8fafc", "#f1f5f9"
    LIGHT_TEXT = "#0f172a"        # seçenek: "#0f172a", "#111827", "#1f2937"
    LIGHT_MUTED = "#64748b"       # seçenek: "#64748b", "#6b7280", "#475569"
    LIGHT_BORDER = "#e2e8f0"      # seçenek: "#e2e8f0", "#d1d5db", "#cbd5e1"
    LIGHT_SOFT = "#eef2ff"        # hover rengi seçenek: "#eef2ff", "#f1f5f9", "#e0f2fe"
    LIGHT_INPUT = "#f1f5f9"

    # Koyu tema renkleri
    DARK_BG = "#020617"           # seçenek: "#020617", "#0f172a", "#111827"
    DARK_BG_2 = "#0f172a"
    DARK_CARD = "#0f172a"
    DARK_TEXT = "#f8fafc"
    DARK_MUTED = "#94a3b8"
    DARK_BORDER = "#1e293b"
    DARK_SOFT = "#111827"
    DARK_INPUT = "#111827"

    # Footer / Sidebar
    SIDEBAR_BG_1 = "#0f172a"
    SIDEBAR_BG_2 = "#020617"
    FOOTER_BG = "#0f172a"
    FOOTER_BG_2 = "#020617"

    # Durum renkleri
    SUCCESS_BG = "#dcfce7"
    SUCCESS_TEXT = "#166534"
    WARNING_BG = "#fef3c7"
    WARNING_TEXT = "#92400e"
    ONLINE_GREEN = "#22c55e"

    # =====================================================
    # 2) FONT AYARLARI
    # =====================================================

    # Font seçenekleri:
    # "Inter", "Segoe UI", Arial, sans-serif
    # "Arial", sans-serif
    # "Helvetica", Arial, sans-serif
    # "Roboto", "Segoe UI", sans-serif
    FONT_FAMILY = '"Inter", "Segoe UI", Arial, sans-serif'

    FONT_WEIGHT_NORMAL = "500"
    FONT_WEIGHT_MEDIUM = "700"
    FONT_WEIGHT_BOLD = "900"
    FONT_WEIGHT_EXTRA = "950"

    HERO_TITLE_SIZE = "62px"      # seçenek: "48px", "56px", "62px", "72px"
    SECTION_TITLE_SIZE = "36px"   # seçenek: "28px", "32px", "36px", "42px"
    CARD_TITLE_SIZE = "25px"      # seçenek: "21px", "23px", "25px", "28px"
    BODY_TEXT_SIZE = "16px"
    MENU_TEXT_SIZE = "14px"

    # =====================================================
    # 3) GEOMETRİ / BOYUTLAR
    # =====================================================

    PAGE_MAX_WIDTH = "1480px"     # seçenek: "1200px", "1320px", "1480px", "1600px"

    TOPBAR_PADDING = "14px 22px"  # seçenek: "10px 18px", "14px 22px", "18px 28px"
    TOPBAR_RADIUS = "24px"        # seçenek: "12px", "18px", "24px", "32px"
    TOPBAR_MARGIN_BOTTOM = "30px"

    LOGO_SIZE = "46px"            # seçenek: "38px", "46px", "54px"
    LOGO_RADIUS = "15px"

    HERO_PADDING = "78px 68px"    # seçenek: "56px 44px", "78px 68px", "96px 80px"
    HERO_RADIUS = "42px"          # seçenek: "20px", "30px", "42px", "56px"
    HERO_MARGIN_BOTTOM = "36px"

    CARD_PADDING = "29px"         # seçenek: "20px", "24px", "29px", "36px"
    CARD_RADIUS = "30px"          # seçenek: "16px", "22px", "30px", "40px"
    CARD_MIN_HEIGHT = "245px"     # seçenek: "190px", "220px", "245px", "280px"
    CARD_LEFT_BORDER = "7px"      # seçenek: "3px", "5px", "7px", "10px"

    METRIC_RADIUS = "26px"
    INPUT_RADIUS = "14px"
    BUTTON_RADIUS = "15px"
    FOOTER_RADIUS = "42px 42px 0 0"

    # =====================================================
    # 4) GÖLGE / EFEKT AYARLARI
    # =====================================================

    LIGHT_SHADOW = "rgba(15,23,42,0.10)"
    DARK_SHADOW = "rgba(0,0,0,0.35)"

    TOPBAR_SHADOW = "0 18px 45px"
    CARD_SHADOW = "0 16px 42px"
    CARD_HOVER_SHADOW = "0 30px 75px rgba(15,23,42,0.17)"
    HERO_SHADOW = "0 32px 85px rgba(15,23,42,0.30)"
    FOOTER_SHADOW = "0 -20px 60px rgba(15,23,42,0.18)"

    HOVER_LIFT = "-7px"           # kart yukarı kalkma efekti
    BUTTON_HOVER_LIFT = "-2px"

    # =====================================================
    # 5) AKTİF TEMA SEÇİMİ
    # =====================================================

    primary = st.session_state.get("primary_color", DEFAULT_PRIMARY)
    dark = st.session_state.get("dark_mode", False)

    if dark:
        bg = DARK_BG
        bg_2 = DARK_BG_2
        card = DARK_CARD
        text = DARK_TEXT
        muted = DARK_MUTED
        border = DARK_BORDER
        soft = DARK_SOFT
        nav = "rgba(2, 6, 23, 0.94)"
        input_bg = DARK_INPUT
        shadow = DARK_SHADOW
    else:
        bg = LIGHT_BG
        bg_2 = LIGHT_BG_2
        card = LIGHT_CARD
        text = LIGHT_TEXT
        muted = LIGHT_MUTED
        border = LIGHT_BORDER
        soft = LIGHT_SOFT
        nav = "rgba(255,255,255,0.94)"
        input_bg = LIGHT_INPUT
        shadow = LIGHT_SHADOW

    # =====================================================
    # CSS
    # =====================================================

    st.markdown(f"""
    <style>

    .stApp {{
        background:
            radial-gradient(circle at top left, rgba(30,58,138,0.08), transparent 26%),
            radial-gradient(circle at top right, rgba(14,165,233,0.06), transparent 28%),
            linear-gradient(180deg, {bg} 0%, {bg_2} 100%);
        color: {text};
        font-family: {FONT_FAMILY};
    }}

    .block-container {{
        max-width: {PAGE_MAX_WIDTH};
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

    footer {{
        visibility: hidden;
    }}

    #MainMenu {{
        visibility: hidden;
    }}

    section[data-testid="stSidebar"] {{
        background: linear-gradient(180deg, {SIDEBAR_BG_1} 0%, {SIDEBAR_BG_2} 100%);
        border-right: 1px solid rgba(255,255,255,0.08);
    }}

    section[data-testid="stSidebar"] * {{
        color: white !important;
    }}

    .arch-topbar {{
        position: sticky;
        top: 0;
        z-index: 999;
        background: {nav};
        backdrop-filter: blur(18px);
        border: 1px solid {border};
        border-radius: {TOPBAR_RADIUS};
        padding: {TOPBAR_PADDING};
        margin-bottom: {TOPBAR_MARGIN_BOTTOM};
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: {TOPBAR_SHADOW} {shadow};
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
        width: {LOGO_SIZE};
        height: {LOGO_SIZE};
        border-radius: {LOGO_RADIUS};
        background: linear-gradient(135deg, {primary}, #0f172a);
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: {FONT_WEIGHT_EXTRA};
        font-size: 25px;
        box-shadow: 0 12px 28px rgba(30,58,138,0.35);
    }}

    .arch-logo-title {{
        font-size: 24px;
        font-weight: {FONT_WEIGHT_EXTRA};
        letter-spacing: -0.9px;
        color: {text};
    }}

    .arch-logo-subtitle {{
        font-size: 11px;
        color: {muted};
        font-weight: {FONT_WEIGHT_MEDIUM};
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
        font-size: {MENU_TEXT_SIZE};
        font-weight: {FONT_WEIGHT_BOLD};
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
        font-weight: {FONT_WEIGHT_MEDIUM};
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
        font-weight: {FONT_WEIGHT_EXTRA};
        box-shadow: 0 12px 26px rgba(30,58,138,0.28);
        transition: all 0.18s ease;
    }}

    .arch-login-btn:hover {{
        transform: translateY({BUTTON_HOVER_LIFT});
        box-shadow: 0 18px 34px rgba(30,58,138,0.36);
    }}

    .hero-platform {{
        background:
            linear-gradient(120deg, rgba(15,23,42,0.96), rgba(30,58,138,0.94)),
            radial-gradient(circle at top right, rgba(255,255,255,0.18), transparent 36%);
        color: white;
        padding: {HERO_PADDING};
        border-radius: {HERO_RADIUS};
        box-shadow: {HERO_SHADOW};
        margin-bottom: {HERO_MARGIN_BOTTOM};
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
        font-weight: {FONT_WEIGHT_EXTRA};
        letter-spacing: 1px;
        margin-bottom: 20px;
        position: relative;
        z-index: 2;
    }}

    .hero-platform h1 {{
        color: white;
        font-size: {HERO_TITLE_SIZE};
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

    .hero-primary,
    .hero-secondary {{
        display: inline-block;
        padding: 14px 22px;
        border-radius: 16px;
        font-weight: {FONT_WEIGHT_EXTRA};
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

    .section-title {{
        font-size: {SECTION_TITLE_SIZE};
        font-weight: {FONT_WEIGHT_EXTRA};
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

    .module-card-link {{
        display: block;
    }}

    .module-card {{
        background: {card};
        border: 1px solid {border};
        border-left: {CARD_LEFT_BORDER} solid {primary};
        border-radius: {CARD_RADIUS};
        padding: {CARD_PADDING};
        min-height: {CARD_MIN_HEIGHT};
        margin-bottom: 22px;
        box-shadow: {CARD_SHADOW} {shadow};
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
        transform: translateY({HOVER_LIFT});
        box-shadow: {CARD_HOVER_SHADOW};
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
        font-size: {CARD_TITLE_SIZE};
        margin-top: 18px;
        margin-bottom: 10px;
        font-weight: {FONT_WEIGHT_EXTRA};
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
        font-weight: {FONT_WEIGHT_EXTRA};
        font-size: 14px;
        position: relative;
        z-index: 2;
    }}

    .status-active,
    .status-soon {{
        display: inline-block;
        padding: 6px 12px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: {FONT_WEIGHT_EXTRA};
    }}

    .status-active {{
        background: {SUCCESS_BG};
        color: {SUCCESS_TEXT};
    }}

    .status-soon {{
        background: {WARNING_BG};
        color: {WARNING_TEXT};
    }}

    div[data-testid="stMetric"] {{
        background: {card};
        border: 1px solid {border};
        border-left: {CARD_LEFT_BORDER} solid {primary};
        padding: 23px;
        border-radius: {METRIC_RADIUS};
        box-shadow: 0 14px 36px {shadow};
    }}

    div[data-testid="stMetricValue"] {{
        font-weight: {FONT_WEIGHT_EXTRA};
        letter-spacing: -0.7px;
    }}

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
        font-weight: {FONT_WEIGHT_EXTRA};
        margin-bottom: 10px;
    }}

    .feature-strip p {{
        color: {muted};
        line-height: 1.65;
        font-size: {BODY_TEXT_SIZE};
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
        font-weight: {FONT_WEIGHT_BOLD};
        color: {text};
    }}

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
        font-weight: {FONT_WEIGHT_EXTRA};
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
        border-radius: {BUTTON_RADIUS};
        font-weight: {FONT_WEIGHT_EXTRA};
        white-space: nowrap;
    }}

    .stTextInput input,
    .stNumberInput input,
    .stTextArea textarea,
    .stDateInput input,
    .stSelectbox div[data-baseweb="select"] {{
        background-color: {input_bg} !important;
        border-radius: {INPUT_RADIUS} !important;
        border: 1px solid {border} !important;
    }}

    .stButton > button {{
        background: {primary};
        color: white;
        border: none;
        border-radius: {BUTTON_RADIUS};
        padding: 0.7rem 1.15rem;
        font-weight: {FONT_WEIGHT_BOLD};
        transition: all 0.18s ease;
    }}

    .stButton > button:hover {{
        transform: translateY({BUTTON_HOVER_LIFT});
        box-shadow: 0 12px 24px rgba(30,58,138,0.28);
    }}

    .stDownloadButton > button {{
        background: {primary};
        color: white;
        border: none;
        border-radius: {BUTTON_RADIUS};
        font-weight: {FONT_WEIGHT_BOLD};
    }}

    .arch-footer {{
        margin-top: 76px;
        background: {FOOTER_BG};
        color: white;
        border-radius: {FOOTER_RADIUS};
        overflow: hidden;
        box-shadow: {FOOTER_SHADOW};
    }}

    .footer-main {{
        padding: 54px;
        display: grid;
        grid-template-columns: 2fr 1fr 1fr 1fr;
        gap: 38px;
    }}

    .footer-main h2,
    .footer-main h4 {{
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
        font-weight: {FONT_WEIGHT_MEDIUM};
    }}

    .footer-main a:hover {{
        color: white !important;
    }}

    .footer-bottom {{
        background: {FOOTER_BG_2};
        color: #94a3b8;
        padding: 18px 54px;
        display: flex;
        justify-content: space-between;
        font-size: 13px;
        font-weight: {FONT_WEIGHT_MEDIUM};
    }}

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