import streamlit as st

from ui.style import apply_global_style
from ui.components import (
    top_navigation,
    section_header,
    info_panel,
    premium_banner,
    footer,
)

from database.database import load_projects, load_project_data, delete_project

apply_global_style()
top_navigation()

st.markdown("""
<div class="hero-platform">
    <div class="hero-badge">PROJEKTE · PROJEKTAKTE · VERWALTUNG</div>
    <h1>Projektverwaltung</h1>
    <p>
        Hier werden gespeicherte HOAI-Berechnungen und spätere Projektakten
        zentral verwaltet. In Zukunft wird dieser Bereich zu einem vollständigen
        Projekt- und Kundencenter erweitert.
    </p>
    <div class="hero-actions">
        <a href="/HOAI_Rechner" class="hero-primary">🏛️ Neues HOAI Angebot</a>
        <a href="/Dashboard" class="hero-secondary">🏠 Zur Übersicht</a>
    </div>
</div>
""", unsafe_allow_html=True)

user = st.session_state.get("user")

if not user:
    st.warning("Bitte zuerst einloggen, um gespeicherte Projekte zu sehen.")
    info_panel(
        "Login erforderlich",
        "Projekte werden benutzerbezogen gespeichert. Melde dich an, um deine eigenen Projekte zu verwalten.",
        "👤",
    )
    footer()
    st.stop()

projects = load_projects(user["id"])
project_count = len(projects)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Gespeicherte Projekte", project_count)
c2.metric("Aktiver Benutzer", user["name"])
c3.metric("Projektakte", "MVP")
c4.metric("Cloud Sync", "Geplant")

section_header(
    "Gespeicherte Projekte",
    "Öffne oder lösche deine gespeicherten Projekte."
)

if not projects:
    st.info("Noch keine Projekte gespeichert.")
    premium_banner(
        "Noch keine Projekte vorhanden",
        "Erstelle im HOAI Rechner dein erstes Angebot und speichere es anschließend als Projekt.",
        "HOAI Rechner öffnen",
        "/HOAI_Rechner",
    )
else:
    for p in projects:
        project_id, project_name, firma_name, project_date = p

        st.markdown(f"""
        <div class="module-card">
            <div class="module-card-top">
                <span class="status-active">Gespeichert</span>
                <span class="module-icon">📂</span>
            </div>
            <h3>#{project_id} — {project_name}</h3>
            <p><b>Firma:</b> {firma_name}</p>
            <p><b>Datum:</b> {project_date}</p>
        </div>
        """, unsafe_allow_html=True)

        c1, c2, c3 = st.columns([1, 1, 4])

        with c1:
            if st.button("📂 Öffnen", key=f"open_{project_id}"):
                data = load_project_data(project_id, user["id"])
                st.session_state.loaded_project = data
                st.session_state.result = data
                st.success("Projekt geladen. Bitte zum HOAI Rechner wechseln.")

        with c2:
            if st.button("🗑️ Löschen", key=f"delete_{project_id}"):
                delete_project(project_id, user["id"])
                st.success("Projekt gelöscht.")
                st.rerun()

        st.markdown("---")

section_header("Geplante Erweiterungen", "Projektverwaltung wird später deutlich erweitert.")

info_panel(
    "Projektakte",
    "Zukünftig werden alle Berechnungen, Dokumente, LV, Kostenstände und Bauleitungsdaten projektbezogen gespeichert.",
    "📁",
)

info_panel(
    "Kundenverwaltung",
    "Später können Bauherren, Firmen, Ansprechpartner und Projektdaten zentral gepflegt werden.",
    "🏢",
)

footer()