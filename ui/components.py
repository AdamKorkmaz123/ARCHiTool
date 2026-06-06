import streamlit as st


# =========================================================
# ARCHiTool UI COMPONENTS
# Professional reusable UI blocks for the platform
# =========================================================


def top_navigation():
    st.markdown("""
    <div class="arch-topbar">

        <a href="/" class="arch-logo-link">
            <div class="arch-logo">
                <div class="arch-logo-mark">A</div>
                <div>
                    <div class="arch-logo-title">ARCHiTool</div>
                    <div class="arch-logo-subtitle">Architecture Intelligence Platform</div>
                </div>
            </div>
        </a>

        <div class="arch-menu">

            <div class="arch-menu-item">
                Plattform
                <div class="arch-dropdown mega-small">
                    <a href="/">🏠 Dashboard</a>
                    <a href="/Projekte">📂 Projekte</a>
                    <a href="/Einstellungen">⚙️ Einstellungen</a>
                    <a href="/Login">👤 Benutzerkonto</a>
                </div>
            </div>

            <div class="arch-menu-item">
                HOAI
                <div class="arch-dropdown mega-medium">
                    <a href="/HOAI_Center">🏛️ HOAI Center</a>
                    <a href="/HOAI_Rechner">🧮 HOAI Rechner</a>
                    <a href="/HOAI_Center">📚 HOAI Wissen</a>
                    <a href="/HOAI_Center">📄 Honorarangebot</a>
                    <a href="/HOAI_Center">📊 LPH Analyse</a>
                </div>
            </div>

            <div class="arch-menu-item">
                Projektplanung
                <div class="arch-dropdown mega-medium">
                    <a href="/Projektplanung">📅 Bauablaufplan</a>
                    <a href="/Projektplanung">📌 Meilensteine</a>
                    <a href="/Projektplanung">📈 Gantt Planung</a>
                    <a href="/Projektplanung">🧱 Projektphasen</a>
                    <a href="/Projektplanung">👥 Ressourcen</a>
                </div>
            </div>

            <div class="arch-menu-item">
                Ausschreibung / LV
                <div class="arch-dropdown mega-medium">
                    <a href="/Ausschreibung_LV">📋 LV Generator</a>
                    <a href="/Ausschreibung_LV">🧾 Positionen</a>
                    <a href="/Ausschreibung_LV">📚 Standardtexte</a>
                    <a href="/Ausschreibung_LV">💶 Kostengruppen</a>
                    <a href="/Ausschreibung_LV">🤖 AI Texte</a>
                </div>
            </div>

            <div class="arch-menu-item">
                Bauleitung
                <div class="arch-dropdown mega-medium">
                    <a href="/Bauleitung">👷 Bauleitung</a>
                    <a href="/Bauleitung">📒 Bautagebuch</a>
                    <a href="/Bauleitung">⚠️ Mängelmanagement</a>
                    <a href="/Bauleitung">📸 Fotodokumentation</a>
                    <a href="/Bauleitung">📄 Bauberichte</a>
                </div>
            </div>

            <div class="arch-menu-item">
                Kosten
                <div class="arch-dropdown mega-medium">
                    <a href="/Kostenmanagement">💶 Kostenmanagement</a>
                    <a href="/Kostenmanagement">📊 DIN 276</a>
                    <a href="/Kostenmanagement">📈 Kostenschätzung</a>
                    <a href="/Kostenmanagement">📉 Kostenkontrolle</a>
                    <a href="/Kostenmanagement">📑 Kostenfeststellung</a>
                </div>
            </div>

        </div>

        <div class="arch-top-actions">
            <a href="/Login" class="arch-login-btn">Login</a>
        </div>

    </div>
    """, unsafe_allow_html=True)


def sidebar_navigation():
    st.sidebar.markdown("""
    <div class="side-brand">
        <div class="side-logo">A</div>
        <div>
            <div class="side-title">ARCHiTool</div>
            <div class="side-subtitle">AEC Platform</div>
        </div>
    </div>

    <div class="side-section-title">Navigation</div>

    <a class="side-link" href="/">🏠 Dashboard</a>
    <a class="side-link" href="/HOAI_Center">🏛️ HOAI Center</a>
    <a class="side-link" href="/HOAI_Rechner">🧮 HOAI Rechner</a>
    <a class="side-link" href="/Projektplanung">📅 Projektplanung</a>
    <a class="side-link" href="/Ausschreibung_LV">📋 Ausschreibung / LV</a>
    <a class="side-link" href="/Bauleitung">👷 Bauleitung</a>
    <a class="side-link" href="/Kostenmanagement">💶 Kostenmanagement</a>
    <a class="side-link" href="/Projekte">📂 Projekte</a>
    <a class="side-link" href="/Einstellungen">⚙️ Einstellungen</a>
    <a class="side-link" href="/Login">👤 Login</a>

    <div class="side-section-title">Systemstatus</div>

    <div class="side-status">
        <span></span>
        Online MVP
    </div>

    <div class="side-mini-card">
        <strong>Aktives Modul</strong>
        <p>HOAI Center</p>
    </div>
    """, unsafe_allow_html=True)


def hero_section(
    badge="AEC SOFTWARE · HOAI · PROJEKTPLANUNG · LV · BAULEITUNG",
    title="Die digitale Arbeitsplattform für moderne Architektur- und Ingenieurbüros",
    text="ARCHiTool bündelt HOAI-Honorarberechnung, Projektplanung, Ausschreibung, LV-Erstellung, Bauleitung, Kostenmanagement und AI-gestützte Werkzeuge in einer professionellen webbasierten Umgebung.",
    primary_label="🏛️ HOAI Center öffnen",
    primary_link="/HOAI_Center",
    secondary_label="📋 Plattform entdecken",
    secondary_link="/Dashboard",
):
    st.markdown(f"""
    <div class="hero-platform">
        <div class="hero-badge">{badge}</div>
        <h1>{title}</h1>
        <p>{text}</p>
        <div class="hero-actions">
            <a href="{primary_link}" class="hero-primary">{primary_label}</a>
            <a href="{secondary_link}" class="hero-secondary">{secondary_label}</a>
        </div>
    </div>
    """, unsafe_allow_html=True)


def section_header(title, subtitle=None):
    subtitle_html = ""
    if subtitle:
        subtitle_html = f'<div class="section-subtitle">{subtitle}</div>'

    st.markdown(f"""
    <div class="section-title">{title}</div>
    {subtitle_html}
    """, unsafe_allow_html=True)


def module_card(status, icon, title, text, link="#"):
    status_class = "status-active" if status == "Aktiv" else "status-soon"

    st.markdown(f"""
    <a href="{link}" class="module-card-link">
        <div class="module-card">
            <div class="module-card-top">
                <span class="{status_class}">{status}</span>
                <span class="module-icon">{icon}</span>
            </div>
            <h3>{title}</h3>
            <p>{text}</p>
            <div class="module-arrow">Modul öffnen →</div>
        </div>
    </a>
    """, unsafe_allow_html=True)


def feature_strip(title, text, features):
    items = ""
    for feature in features:
        items += f'<div class="feature-item">{feature}</div>'

    st.markdown(f"""
    <div class="feature-strip">
        <h3>{title}</h3>
        <p>{text}</p>
        <div class="feature-list">
            {items}
        </div>
    </div>
    """, unsafe_allow_html=True)


def roadmap_columns():
    r1, r2, r3 = st.columns(3)

    with r1:
        st.markdown("""
        ### Phase 1 — MVP

        - HOAI Rechner
        - PDF / Word / Excel Export
        - Projekt speichern
        - Login System
        - Basis Dashboard
        """)

    with r2:
        st.markdown("""
        ### Phase 2 — Office Suite

        - Projektakte
        - Firmenbranding
        - Angebotsnummern
        - Premium PDF
        - Kundenverwaltung
        """)

    with r3:
        st.markdown("""
        ### Phase 3 — Professional Platform

        - Bauablaufplan
        - LV Generator
        - DIN 276
        - Bauleitung
        - AI Assistent
        """)


def info_panel(title, text, icon="ℹ️"):
    st.markdown(f"""
    <div class="info-panel">
        <div class="info-panel-icon">{icon}</div>
        <div>
            <h3>{title}</h3>
            <p>{text}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)


def premium_banner(title, text, button_label=None, button_link="#"):
    button_html = ""
    if button_label:
        button_html = f'<a href="{button_link}" class="banner-button">{button_label}</a>'

    st.markdown(f"""
    <div class="premium-banner">
        <div>
            <h2>{title}</h2>
            <p>{text}</p>
        </div>
        {button_html}
    </div>
    """, unsafe_allow_html=True)


def footer():
    st.markdown("""
    <div class="arch-footer">

        <div class="footer-main">

            <div>
                <h2>ARCHiTool</h2>
                <p>
                    Digitale Arbeitsplattform für Architektur- und Ingenieurbüros.
                    HOAI, Projektplanung, Ausschreibung, Bauleitung und Kostenmanagement
                    in einem modularen professionellen System.
                </p>
            </div>

            <div>
                <h4>Plattform</h4>
                <a href="/">Dashboard</a>
                <a href="/Projekte">Projekte</a>
                <a href="/Einstellungen">Einstellungen</a>
                <a href="/Login">Login</a>
            </div>

            <div>
                <h4>Module</h4>
                <a href="/HOAI_Center">HOAI Center</a>
                <a href="/Projektplanung">Projektplanung</a>
                <a href="/Ausschreibung_LV">Ausschreibung / LV</a>
                <a href="/Bauleitung">Bauleitung</a>
                <a href="/Kostenmanagement">Kostenmanagement</a>
            </div>

            <div>
                <h4>Tools</h4>
                <a href="/HOAI_Rechner">HOAI Rechner</a>
                <a href="/Kostenmanagement">DIN 276</a>
                <a href="/Ausschreibung_LV">LV Generator</a>
                <a href="/Projektplanung">Bauablaufplan</a>
                <a href="/Bauleitung">Bautagebuch</a>
            </div>

        </div>

        <div class="footer-bottom">
            <span>© 2026 ARCHiTool</span>
            <span>Professional Architecture Intelligence Platform</span>
        </div>

    </div>
    """, unsafe_allow_html=True)