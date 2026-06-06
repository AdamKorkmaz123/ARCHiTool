import streamlit as st


def top_navigation():
    st.markdown("""
    <div class="arch-topbar">
        <div class="arch-logo">
            <div class="arch-logo-mark">A</div>
            <div>
                <div class="arch-logo-title">ARCHiTool</div>
                <div class="arch-logo-subtitle">Architecture Intelligence Platform</div>
            </div>
        </div>

        <div class="arch-menu">

            <div class="arch-menu-item">
                Plattform
                <div class="arch-dropdown">
                    <a href="/">Dashboard</a>
                    <a href="/Dashboard">Übersicht</a>
                    <a href="/Projekte">Projekte</a>
                    <a href="/Einstellungen">Einstellungen</a>
                </div>
            </div>

            <div class="arch-menu-item">
                HOAI
                <div class="arch-dropdown">
                    <a href="/HOAI_Center">HOAI Center</a>
                    <a href="/HOAI_Rechner">HOAI Rechner</a>
                    <a href="/HOAI_Center">HOAI Wissen</a>
                    <a href="/HOAI_Center">Honorarangebot</a>
                </div>
            </div>

            <div class="arch-menu-item">
                Planung
                <div class="arch-dropdown">
                    <a href="/Projektplanung">Bauablaufplan</a>
                    <a href="/Projektplanung">Terminplan</a>
                    <a href="/Projektplanung">Meilensteine</a>
                    <a href="/Projektplanung">Gantt</a>
                </div>
            </div>

            <div class="arch-menu-item">
                Ausschreibung
                <div class="arch-dropdown">
                    <a href="/Ausschreibung_LV">LV Generator</a>
                    <a href="/Ausschreibung_LV">Positionen</a>
                    <a href="/Ausschreibung_LV">DIN 276</a>
                    <a href="/Ausschreibung_LV">Textbausteine</a>
                </div>
            </div>

            <div class="arch-menu-item">
                Bauleitung
                <div class="arch-dropdown">
                    <a href="/Bauleitung">Bautagebuch</a>
                    <a href="/Bauleitung">Mängelmanagement</a>
                    <a href="/Bauleitung">Bauberichte</a>
                    <a href="/Bauleitung">Bauleitungskosten</a>
                </div>
            </div>

            <div class="arch-menu-item">
                Kosten
                <div class="arch-dropdown">
                    <a href="/Kostenmanagement">DIN 276</a>
                    <a href="/Kostenmanagement">Kostenschätzung</a>
                    <a href="/Kostenmanagement">Kostenberechnung</a>
                    <a href="/Kostenmanagement">Kostenkontrolle</a>
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

    <div class="side-section-title">Status</div>
    <div class="side-status">
        <span></span>
        System Online
    </div>
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


def footer():
    st.markdown("""
    <div class="arch-footer">
        <div class="footer-main">
            <div>
                <h2>ARCHiTool</h2>
                <p>
                    Digitale Arbeitsplattform für Architektur- und Ingenieurbüros.
                    HOAI, Projektplanung, Ausschreibung, Bauleitung und Kostenmanagement
                    in einem modularen System.
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
            </div>

            <div>
                <h4>Tools</h4>
                <a href="/HOAI_Rechner">HOAI Rechner</a>
                <a href="/Kostenmanagement">DIN 276</a>
                <a href="/Ausschreibung_LV">LV Generator</a>
                <a href="/Projektplanung">Bauablaufplan</a>
            </div>
        </div>

        <div class="footer-bottom">
            <span>© 2026 ARCHiTool</span>
            <span>Professional Architecture Intelligence Platform</span>
        </div>
    </div>
    """, unsafe_allow_html=True)