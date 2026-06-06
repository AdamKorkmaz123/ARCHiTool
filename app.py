import streamlit as st
from ui.style import apply_global_style
from database.database import init_db, load_projects

st.set_page_config(
    page_title="ARCHiTool",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_global_style()
init_db()

user = st.session_state.get("user")

with st.sidebar:
    st.title("🏛️ ARCHiTool")
    st.markdown("---")
    st.write("**Platform Navigation**")
    st.write("🏛️ HOAI Rechner")
    st.write("📂 Projekte")
    st.write("⚙️ Einstellungen")
    st.write("👤 Login")
    st.markdown("---")
    st.caption("Weitere Module werden schrittweise ergänzt.")

st.markdown("""
<div class="hero-card">
    <h1>🏛️ ARCHiTool</h1>
    <p>
        Die digitale Arbeitsplattform für Architektur- und Ingenieurbüros:
        HOAI, Projektplanung, Ausschreibung, Bauleitung und Kostenmanagement.
    </p>
</div>
""", unsafe_allow_html=True)

if user:
    projects = load_projects(user["id"])
    project_count = len(projects)
    st.success(f"Willkommen zurück, {user['name']}")
else:
    project_count = 0
    st.info("Du kannst ARCHiTool testen. Für Projektspeicherung bitte einloggen.")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Gespeicherte Projekte", project_count)
c2.metric("Aktive Module", "1")
c3.metric("Exportformate", "PDF / Word / Excel")
c4.metric("Status", "MVP Online")

st.markdown('<div class="section-title">🚀 Module</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="module-card">
        <span class="status-active">Aktiv</span>
        <h3>🏛️ HOAI Center</h3>
        <p>HOAI Honorarberechnung, LPH 1–9, Zuschläge, Abschläge, PDF/Word/Excel Export.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="module-card">
        <span class="status-soon">Demnächst</span>
        <h3>📅 Projektplanung</h3>
        <p>Bauablaufplan, Terminplan, Meilensteine, Projektphasen und Zeitachsen.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="module-card">
        <span class="status-soon">Demnächst</span>
        <h3>📋 Ausschreibung / LV</h3>
        <p>Einfaches LV, Positionsgenerator, Kostengruppen und Textbausteine.</p>
    </div>
    """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="module-card">
        <span class="status-soon">Demnächst</span>
        <h3>👷 Bauleitung</h3>
        <p>Bauleitungskosten, Bautagebuch, Mängelmanagement und Baustellenberichte.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="module-card">
        <span class="status-soon">Demnächst</span>
        <h3>💶 Kostenmanagement</h3>
        <p>DIN 276, Kostenschätzung, Kostenberechnung, Kostenanschlag und Kostenkontrolle.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="module-card">
        <span class="status-soon">Demnächst</span>
        <h3>🤖 AI Assistent</h3>
        <p>Automatische Vorschläge für Angebote, LV-Texte, Projektstruktur und Dokumente.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown('<div class="section-title">📌 Plattformbereiche</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("🏛️ **HOAI Rechner**\n\nHonorarangebote berechnen.")

with col2:
    st.info("📂 **Projekte**\n\nProjekte speichern und verwalten.")

with col3:
    st.info("⚙️ **Einstellungen**\n\nFarben, Logo und Design.")

with col4:
    st.info("👤 **Login**\n\nBenutzerkonto verwalten.")

st.markdown("---")

st.markdown('<div class="section-title">🛣️ Roadmap</div>', unsafe_allow_html=True)

st.write("""
**Geplante Erweiterungen:**

- HOAI Wissen / Paragraphen / Erklärungstexte
- Bauablaufplan Generator
- Einfacher LV Generator
- Bauleitungskosten Tabellen
- DIN 276 Kostenmanagement
- Angebotsnummern und Firmenvorlagen
- Premium PDF Templates
- Kundenverwaltung
- Cloud Datenbank
- Team- und Rollenverwaltung
""")