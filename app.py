import streamlit as st
from ui.style import apply_global_style
from ui.components import top_navigation, footer, module_card
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
    st.write("**Navigation**")
    st.write("🏠 Dashboard")
    st.write("🏛️ HOAI Center")
    st.write("📅 Projektplanung")
    st.write("📋 Ausschreibung LV")
    st.write("👷 Bauleitung")
    st.write("💶 Kostenmanagement")
    st.write("📂 Projekte")
    st.write("⚙️ Einstellungen")
    st.write("👤 Login")

top_navigation()

st.markdown("""
<div class="hero-platform">
    <div class="hero-badge">ARCHITECTURE · ENGINEERING · CONSTRUCTION</div>
    <h1>Digitale Plattform für Architektur- und Ingenieurbüros</h1>
    <p>
        ARCHiTool vereint HOAI-Honorarberechnung, Projektplanung,
        Ausschreibung, LV-Erstellung, Bauleitung und Kostenmanagement
        in einer modernen webbasierten Arbeitsumgebung.
    </p>
    <div class="hero-actions">
        <span class="hero-primary">🏛️ HOAI Center öffnen</span>
        <span class="hero-secondary">📋 Module entdecken</span>
    </div>
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

with c1:
    st.metric("Projekte", project_count)

with c2:
    st.metric("Aktive Module", "1")

with c3:
    st.metric("Geplante Module", "6+")

with c4:
    st.metric("Status", "Online MVP")

st.markdown('<div class="section-title">🚀 Plattformmodule</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Alle Werkzeuge, die Architektur- und Ingenieurbüros im Alltag brauchen — schrittweise als professionelle Module aufgebaut.</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    module_card(
        "Aktiv",
        "🏛️",
        "HOAI Center",
        "HOAI Rechner, LPH 1–9, Zuschläge, Abschläge, Honorarangebot und Export als PDF, Word und Excel."
    )

with col2:
    module_card(
        "Demnächst",
        "📅",
        "Projektplanung",
        "Bauablaufplan, Terminplanung, Meilensteine, Projektphasen, Gantt und Ressourcenplanung."
    )

with col3:
    module_card(
        "Demnächst",
        "📋",
        "Ausschreibung / LV",
        "Einfaches LV erstellen, Positionen generieren, Standardtexte, Kostengruppen und Exportfunktionen."
    )

col1, col2, col3 = st.columns(3)

with col1:
    module_card(
        "Demnächst",
        "👷",
        "Bauleitung",
        "Bautagebuch, Mängelmanagement, Baustellenberichte, Fotodokumentation und Bauleitungskosten."
    )

with col2:
    module_card(
        "Demnächst",
        "💶",
        "Kostenmanagement",
        "DIN 276, Kostenschätzung, Kostenberechnung, Kostenanschlag, Kostenfeststellung und Kontrolle."
    )

with col3:
    module_card(
        "Demnächst",
        "🤖",
        "AI Assistent",
        "Automatische Vorschläge für Angebote, LV-Texte, Projektstruktur, Terminplanung und Dokumente."
    )

st.markdown("""
<div class="feature-strip">
    <h3>Ein System für den gesamten Büroalltag</h3>
    <p>
        ARCHiTool wird als modulare Plattform aufgebaut. Jedes Modul kann eigenständig genutzt
        werden und später mit Projekten, Kunden, Exporten und AI-Funktionen verbunden werden.
    </p>

    <div class="feature-list">
        <div class="feature-item">🏛️ HOAI</div>
        <div class="feature-item">📅 Bauablaufplan</div>
        <div class="feature-item">📋 LV Generator</div>
        <div class="feature-item">💶 DIN 276</div>
        <div class="feature-item">👷 Bauleitung</div>
        <div class="feature-item">📂 Projektakte</div>
        <div class="feature-item">📄 Export Center</div>
        <div class="feature-item">🤖 AI Tools</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">📌 Entwicklungs-Roadmap</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### Kurzfristig

    - HOAI Center verbessern
    - PDF Premium Template
    - Projektakte
    - Firmenlogo / Branding
    - Benutzerprofile
    - Angebotsnummern
    """)

with col2:
    st.markdown("""
    ### Mittelfristig

    - Bauablaufplan Generator
    - LV Generator
    - DIN 276 Kostenmanagement
    - Bautagebuch
    - AI Angebotsassistent
    - Cloud Datenbank
    """)

footer()