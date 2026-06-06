import streamlit as st


def top_navigation():
    st.markdown("""
    <div class="top-nav">
        <div class="brand">
            <span class="brand-icon">🏛️</span>
            <span class="brand-text">ARCHiTool</span>
        </div>

        <div class="nav-links">
            <span>HOAI</span>
            <span>Projektplanung</span>
            <span>LV / Ausschreibung</span>
            <span>Bauleitung</span>
            <span>Kostenmanagement</span>
            <span>AI Tools</span>
        </div>

        <div class="nav-action">
            <span class="login-pill">Login</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


def footer():
    st.markdown("""
    <div class="footer">
        <div>
            <h3>ARCHiTool</h3>
            <p>Digitale Plattform für Architektur- und Ingenieurbüros.</p>
        </div>

        <div>
            <h4>Module</h4>
            <p>HOAI Center</p>
            <p>Projektplanung</p>
            <p>Ausschreibung / LV</p>
            <p>Bauleitung</p>
        </div>

        <div>
            <h4>Tools</h4>
            <p>Honorarberechnung</p>
            <p>Bauablaufplan</p>
            <p>LV Generator</p>
            <p>Kostenmanagement</p>
        </div>

        <div>
            <h4>System</h4>
            <p>Login</p>
            <p>Projekte</p>
            <p>Einstellungen</p>
            <p>Export</p>
        </div>
    </div>

    <div class="footer-bottom">
        © 2026 ARCHiTool — Professional Architecture Software Platform
    </div>
    """, unsafe_allow_html=True)


def module_card(status, icon, title, text):
    status_class = "status-active" if status == "Aktiv" else "status-soon"

    st.markdown(f"""
    <div class="module-card">
        <span class="{status_class}">{status}</span>
        <h3>{icon} {title}</h3>
        <p>{text}</p>
    </div>
    """, unsafe_allow_html=True)