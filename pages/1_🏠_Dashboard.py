import streamlit as st

from ui.style import apply_global_style
from ui.components import (
    top_navigation,
    sidebar_navigation,
    section_header,
    module_card,
    feature_strip,
    info_panel,
    premium_banner,
    roadmap_columns,
    footer,
)

from database.database import load_projects


apply_global_style()
sidebar_navigation()
top_navigation()

user = st.session_state.get("user")

if user:
    projects = load_projects(user["id"])
    project_count = len(projects)
    user_label = user["name"]
else:
    project_count = 0
    user_label = "Gast"


st.markdown("""
<div class="hero-platform">
    <div class="hero-badge">DASHBOARD · ARCHITECTURE PLATFORM</div>
    <h1>Willkommen im ARCHiTool Dashboard</h1>
    <p>
        Zentrale Übersicht für Projekte, HOAI-Berechnungen, Ausschreibungen,
        Bauleitung, Kostenmanagement und zukünftige AI-gestützte Büroprozesse.
    </p>
    <div class="hero-actions">
        <a href="/HOAI_Center" class="hero-primary">🏛️ HOAI Center öffnen</a>
        <a href="/Projekte" class="hero-secondary">📂 Projekte verwalten</a>
    </div>
</div>
""", unsafe_allow_html=True)

if user:
    st.success(f"Willkommen zurück, {user_label}")
else:
    st.info("Du bist als Gast unterwegs. Für Projektspeicherung bitte einloggen.")


c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Aktive Projekte", project_count)

with c2:
    st.metric("HOAI Berechnungen", "0")

with c3:
    st.metric("Exportierte Dateien", "0")

with c4:
    st.metric("Systemstatus", "Online")


feature_strip(
    title="Deine zentrale Arbeitsoberfläche",
    text="Von hier aus erreichst du alle Hauptmodule der Plattform.",
    features=[
        "🏛️ HOAI",
        "📅 Projektplanung",
        "📋 LV / Ausschreibung",
        "👷 Bauleitung",
        "💶 Kostenmanagement",
        "📂 Projektakte",
        "📄 Export Center",
        "🤖 AI Werkzeuge",
    ],
)


section_header(
    "Schnellzugriff",
    "Die wichtigsten Bereiche der Plattform auf einen Blick."
)

col1, col2, col3 = st.columns(3)

with col1:
    module_card(
        "Aktiv",
        "🏛️",
        "HOAI Center",
        "Honorarberechnung, Zuschläge, LPH und professionelle Angebotsausgabe.",
        "/HOAI_Center",
    )

with col2:
    module_card(
        "Aktiv",
        "📂",
        "Projekte",
        "Gespeicherte Projekte öffnen, verwalten und später projektbezogen auswerten.",
        "/Projekte",
    )

with col3:
    module_card(
        "Aktiv",
        "⚙️",
        "Einstellungen",
        "Logo, Farben, Dark Mode und Corporate Design anpassen.",
        "/Einstellungen",
    )


section_header(
    "Systemübersicht",
    "ARCHiTool wird als vollständiges digitales Büro-System aufgebaut."
)

info_panel(
    "Modulare Plattform",
    "Jedes Modul kann eigenständig entwickelt und später mit Projekten, Kunden, Exporten und AI-Funktionen verbunden werden.",
    "🧩",
)

info_panel(
    "AEC Workflow",
    "Die Plattform orientiert sich am realen Arbeitsprozess von Architektur- und Ingenieurbüros: Honorar, Planung, Ausschreibung, Bauleitung und Kosten.",
    "🏗️",
)

premium_banner(
    "Nächster Entwicklungsschritt",
    "Als nächstes werden HOAI Center und HOAI Rechner optisch auf Premium-Niveau gebracht.",
    "HOAI Center öffnen",
    "/HOAI_Center",
)

section_header("Roadmap", "Geplante Produktentwicklung.")

roadmap_columns()

footer()