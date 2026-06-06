import streamlit as st
from ui.style import apply_global_style
from ui.components import top_navigation, sidebar_navigation, footer, module_card
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

sidebar_navigation()
top_navigation()

if user:
    projects = load_projects(user["id"])
    project_count = len(projects)
else:
    project_count = 0

st.markdown("""
<div class="hero-platform">
    <div class="hero-badge">AEC SOFTWARE · HOAI · PROJEKTPLANUNG · LV · BAULEITUNG</div>
    <h1>Die digitale Arbeitsplattform für moderne Architektur- und Ingenieurbüros</h1>
    <p>
        ARCHiTool bündelt HOAI-Honorarberechnung, Projektplanung,
        Ausschreibung, LV-Erstellung, Bauleitung, Kostenmanagement und AI-gestützte Werkzeuge
        in einer professionellen webbasierten Umgebung.
    </p>
    <div class="hero-actions">
        <a href="/HOAI_Center" class="hero-primary">🏛️ HOAI Center öffnen</a>
        <a href="/Dashboard" class="hero-secondary">📋 Plattform entdecken</a>
    </div>
</div>
""", unsafe_allow_html=True)

if user:
    st.success(f"Willkommen zurück, {user['name']}")
else:
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
st.markdown("""
<div class="section-subtitle">
ARCHiTool ist modular aufgebaut. Jedes Werkzeug kann separat genutzt werden und wird später
mit Projekten, Kunden, Dokumenten, Exporten und AI-Funktionen verbunden.
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    module_card(
        "Aktiv",
        "🏛️",
        "HOAI Center",
        "Honorarberechnung nach HOAI, LPH 1–9, Zuschläge, Abschläge, Angebotsexport als PDF, Word und Excel.",
        "/HOAI_Center"
    )

with col2:
    module_card(
        "Demnächst",
        "📅",
        "Projektplanung",
        "Bauablaufplan, Terminplanung, Meilensteine, Projektphasen, Gantt-Diagramme und Ressourcenplanung.",
        "/Projektplanung"
    )

with col3:
    module_card(
        "Demnächst",
        "📋",
        "Ausschreibung / LV",
        "Einfache Leistungsverzeichnisse, Positionsgenerator, Standardtexte, Kostengruppen und Exportfunktionen.",
        "/Ausschreibung_LV"
    )

col1, col2, col3 = st.columns(3)

with col1:
    module_card(
        "Demnächst",
        "👷",
        "Bauleitung",
        "Bautagebuch, Mängelmanagement, Baustellenberichte, Fotodokumentation und Bauleitungskosten.",
        "/Bauleitung"
    )

with col2:
    module_card(
        "Demnächst",
        "💶",
        "Kostenmanagement",
        "DIN 276, Kostenschätzung, Kostenberechnung, Kostenanschlag, Kostenfeststellung und Kostenkontrolle.",
        "/Kostenmanagement"
    )

with col3:
    module_card(
        "Demnächst",
        "🤖",
        "AI Assistent",
        "AI-gestützte Vorschläge für Angebote, LV-Texte, Projektstruktur, Terminplanung und Dokumente.",
        "/Dashboard"
    )

st.markdown("""
<div class="feature-strip">
    <h3>Ein zentrales System für den Büroalltag</h3>
    <p>
        ARCHiTool wird als professionelle Plattform für den gesamten Projektprozess aufgebaut:
        von der Honorarermittlung über Planung und Ausschreibung bis zu Bauleitung,
        Kostenkontrolle und Dokumentation.
    </p>

    <div class="feature-list">
        <div class="feature-item">🏛️ HOAI Rechner</div>
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

st.markdown('<div class="section-title">🛣️ Entwicklungs-Roadmap</div>', unsafe_allow_html=True)

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

footer()