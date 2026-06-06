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
    footer,
)


apply_global_style()
sidebar_navigation()
top_navigation()


st.markdown("""
<div class="hero-platform">
    <div class="hero-badge">PROJEKTPLANUNG · TERMINE · BAUABLAUF · GANTT</div>
    <h1>Projektplanung und Bauablaufsteuerung</h1>
    <p>
        Dieses Modul wird zur zentralen Planungsumgebung für Bauablaufpläne,
        Terminstrukturen, Meilensteine, Projektphasen und Ressourcensteuerung.
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
    st.metric("Planungstyp", "Bauablauf")

with c3:
    st.metric("Diagramme", "Gantt")

with c4:
    st.metric("Export", "Geplant")


feature_strip(
    title="Geplante Projektplanungs-Funktionen",
    text="Das Modul wird später Projektabläufe, Bauzeiten, Abhängigkeiten und Meilensteine strukturiert abbilden.",
    features=[
        "📅 Bauablaufplan",
        "📌 Meilensteine",
        "📈 Gantt Diagramm",
        "🧱 Projektphasen",
        "👥 Ressourcen",
        "⏱️ Fristen",
        "📄 Export",
        "🤖 AI Planung",
    ],
)


section_header(
    "Projektplanungs-Werkzeuge",
    "Diese Funktionen werden schrittweise in ARCHiTool integriert."
)

col1, col2, col3 = st.columns(3)

with col1:
    module_card(
        "Coming Soon",
        "📅",
        "Bauablaufplan",
        "Automatische Erstellung einfacher Bauablaufpläne mit Phasen, Dauern und Abhängigkeiten.",
        "/Projektplanung",
    )

with col2:
    module_card(
        "Coming Soon",
        "📈",
        "Gantt Diagramm",
        "Visualisierung von Projektphasen, Terminen, Abhängigkeiten und kritischen Zeiträumen.",
        "/Projektplanung",
    )

with col3:
    module_card(
        "Coming Soon",
        "📌",
        "Meilensteine",
        "Definition wichtiger Projektpunkte wie Planabgabe, Ausschreibung, Baubeginn und Abnahme.",
        "/Projektplanung",
    )


col1, col2, col3 = st.columns(3)

with col1:
    module_card(
        "Coming Soon",
        "🧱",
        "Projektphasen",
        "Strukturierung nach Vorplanung, Entwurf, Genehmigung, Ausführung und Bauleitung.",
        "/Projektplanung",
    )

with col2:
    module_card(
        "Coming Soon",
        "👥",
        "Ressourcenplanung",
        "Zukünftige Zuordnung von Teams, Verantwortlichkeiten und Kapazitäten.",
        "/Projektplanung",
    )

with col3:
    module_card(
        "Coming Soon",
        "🤖",
        "AI Ablaufplan",
        "KI-gestützte Vorschläge für Terminabfolgen, Abhängigkeiten und typische Bauzeiten.",
        "/Projektplanung",
    )


section_header(
    "Geplanter Workflow",
    "So wird das Projektplanungsmodul später funktionieren."
)

info_panel(
    "1. Projekt anlegen",
    "Das Projekt wird mit Basisdaten, Projektart, Größe und gewünschtem Leistungsumfang erfasst.",
    "📁",
)

info_panel(
    "2. Phasen definieren",
    "Projektphasen und Arbeitspakete werden manuell oder automatisch aus Vorlagen erzeugt.",
    "🧱",
)

info_panel(
    "3. Zeitachsen erstellen",
    "Termine, Dauern und Abhängigkeiten werden in einer strukturierten Planung zusammengeführt.",
    "📈",
)

info_panel(
    "4. Export und Dokumentation",
    "Der Bauablaufplan kann später als PDF, Excel oder Projektbericht ausgegeben werden.",
    "📄",
)


premium_banner(
    "Projektplanung wird vorbereitet",
    "Dieses Modul bildet später die Grundlage für Bauablaufplan, Terminsteuerung und AI-gestützte Projektlogik.",
    "Zurück zum Dashboard",
    "/Dashboard",
)


footer()