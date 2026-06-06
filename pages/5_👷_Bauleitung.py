import streamlit as st

from ui.style import apply_global_style
from ui.components import (
    top_navigation,
    section_header,
    module_card,
    feature_strip,
    info_panel,
    premium_banner,
    footer,
)

apply_global_style()()
top_navigation()

st.markdown("""
<div class="hero-platform">
    <div class="hero-badge">BAULEITUNG · BAUTAGEBUCH · MÄNGEL · BERICHTE</div>
    <h1>Bauleitung und Baustellendokumentation</h1>
    <p>
        Dieses Modul wird später Bauleitungskosten, Bautagebuch,
        Mängelmanagement, Baustellenberichte, Fotodokumentation und
        Abnahmeprotokolle digital abbilden.
    </p>
    <div class="hero-actions">
        <a href="/Projekte" class="hero-primary">📂 Projekte öffnen</a>
        <a href="/Dashboard" class="hero-secondary">🏠 Zur Übersicht</a>
    </div>
</div>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Status", "In Entwicklung")
with c2:
    st.metric("Modul", "Bauleitung")
with c3:
    st.metric("Dokumentation", "Geplant")
with c4:
    st.metric("Export", "Geplant")

feature_strip(
    title="Geplante Bauleitungs-Funktionen",
    text="ARCHiTool soll künftig Baustellenprozesse, Mängel, Berichte und Dokumentation zentral erfassen.",
    features=[
        "👷 Bauleitung",
        "📒 Bautagebuch",
        "⚠️ Mängel",
        "📸 Fotodoku",
        "📄 Berichte",
        "✅ Abnahme",
        "💶 Kosten",
        "🤖 AI Protokolle",
    ],
)

section_header(
    "Bauleitungs-Werkzeuge",
    "Diese Funktionen werden schrittweise integriert."
)

col1, col2, col3 = st.columns(3)

with col1:
    module_card(
        "Coming Soon",
        "📒",
        "Bautagebuch",
        "Digitale tägliche Baustellendokumentation mit Wetter, Beteiligten, Leistungen und Ereignissen.",
        "/Bauleitung",
    )

with col2:
    module_card(
        "Coming Soon",
        "⚠️",
        "Mängelmanagement",
        "Erfassung, Verfolgung und Dokumentation von Mängeln inklusive Status und Fristen.",
        "/Bauleitung",
    )

with col3:
    module_card(
        "Coming Soon",
        "📸",
        "Fotodokumentation",
        "Projektbezogene Fotoablage für Baustellenfortschritt, Mängel und Nachweise.",
        "/Bauleitung",
    )

col1, col2, col3 = st.columns(3)

with col1:
    module_card(
        "Coming Soon",
        "📄",
        "Baustellenberichte",
        "Automatische Berichte für Baufortschritt, Termine, Beteiligte und offene Punkte.",
        "/Bauleitung",
    )

with col2:
    module_card(
        "Coming Soon",
        "✅",
        "Abnahmeprotokolle",
        "Strukturierte Protokolle für Abnahmen, Teilabnahmen und Dokumentationspflichten.",
        "/Bauleitung",
    )

with col3:
    module_card(
        "Coming Soon",
        "💶",
        "Bauleitungskosten",
        "Tabellen und Kalkulationen zur Ermittlung und Auswertung von Bauleitungskosten.",
        "/Bauleitung",
    )

section_header(
    "Geplanter Workflow",
    "So soll das Bauleitungsmodul später funktionieren."
)

info_panel(
    "1. Baustelle dokumentieren",
    "Tägliche Baustellendaten, Beteiligte, Wetter, Leistungen und besondere Vorkommnisse werden erfasst.",
    "📒",
)

info_panel(
    "2. Mängel erfassen",
    "Mängel werden mit Beschreibung, Foto, Frist, Status und Verantwortlichkeit dokumentiert.",
    "⚠️",
)

info_panel(
    "3. Berichte erzeugen",
    "Aus den Daten werden automatisch Baustellenberichte, Protokolle und Dokumentationen erstellt.",
    "📄",
)

info_panel(
    "4. Kosten auswerten",
    "Bauleitungskosten und Aufwand können später projektbezogen ausgewertet werden.",
    "💶",
)

premium_banner(
    "Bauleitungsmodul wird vorbereitet",
    "Dieses Modul wird später Baustellendokumentation, Mängelmanagement und Bauleitungskosten verbinden.",
    "Zurück zum Dashboard",
    "/Dashboard",
)

footer()