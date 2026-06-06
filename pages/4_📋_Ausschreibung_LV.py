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

apply_global_style()
top_navigation()

st.markdown("""
<div class="hero-platform">
    <div class="hero-badge">AUSSCHREIBUNG · LV · POSITIONEN · TEXTBAUSTEINE</div>
    <h1>Ausschreibung und Leistungsverzeichnis</h1>
    <p>
        Dieses Modul wird später einfache LV-Strukturen, Positionslisten,
        Standardtexte, Kostengruppen und AI-gestützte Ausschreibungstexte erzeugen.
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
    st.metric("Modul", "LV")
with c3:
    st.metric("Export", "Geplant")
with c4:
    st.metric("AI Texte", "Geplant")

feature_strip(
    title="Geplante LV-Funktionen",
    text="ARCHiTool soll künftig einfache Ausschreibungs- und LV-Strukturen automatisch vorbereiten.",
    features=[
        "📋 LV Generator",
        "🧾 Positionen",
        "📚 Standardtexte",
        "💶 Kostengruppen",
        "📄 Word Export",
        "📊 Excel Export",
        "🤖 AI Texte",
        "🏗️ Projektbezug",
    ],
)

section_header(
    "Ausschreibungs-Werkzeuge",
    "Diese Funktionen werden schrittweise integriert."
)

col1, col2, col3 = st.columns(3)

with col1:
    module_card(
        "Coming Soon",
        "📋",
        "LV Generator",
        "Erstellung einfacher Leistungsverzeichnisse mit Positionen, Mengen und Kurztexten.",
        "/Ausschreibung_LV",
    )

with col2:
    module_card(
        "Coming Soon",
        "🧾",
        "Positionsgenerator",
        "Automatische Erzeugung typischer Positionen für Bauleistungen und Kostengruppen.",
        "/Ausschreibung_LV",
    )

with col3:
    module_card(
        "Coming Soon",
        "📚",
        "Standardtexte",
        "Bibliothek für Ausschreibungstexte, Leistungsbeschreibungen und wiederkehrende Textbausteine.",
        "/Ausschreibung_LV",
    )

col1, col2, col3 = st.columns(3)

with col1:
    module_card(
        "Coming Soon",
        "💶",
        "Kostengruppen",
        "Verknüpfung mit DIN 276, Kostenpositionen und späterem Kostenmanagement.",
        "/Kostenmanagement",
    )

with col2:
    module_card(
        "Coming Soon",
        "📄",
        "LV Export",
        "Export von Leistungsverzeichnissen als Word, Excel oder PDF.",
        "/Ausschreibung_LV",
    )

with col3:
    module_card(
        "Coming Soon",
        "🤖",
        "AI LV Assistent",
        "KI-gestützte Vorschläge für Positionstexte, Mengenlogik und Leistungsbeschreibungen.",
        "/Ausschreibung_LV",
    )

section_header(
    "Geplanter Workflow",
    "So soll das LV-Modul später funktionieren."
)

info_panel(
    "1. Projekt und Kostengruppe wählen",
    "Das LV wird projektbezogen erstellt und kann mit DIN 276 Kostengruppen verknüpft werden.",
    "📁",
)

info_panel(
    "2. Positionen erzeugen",
    "Positionen werden manuell erstellt oder aus Vorlagen und AI-Vorschlägen generiert.",
    "🧾",
)

info_panel(
    "3. Texte und Mengen ergänzen",
    "Kurztexte, Langtexte, Einheiten, Mengen und Preise werden strukturiert ergänzt.",
    "📋",
)

info_panel(
    "4. LV exportieren",
    "Das fertige Leistungsverzeichnis kann später als Word, Excel oder PDF ausgegeben werden.",
    "📄",
)

premium_banner(
    "LV Generator wird vorbereitet",
    "Dieses Modul wird später Ausschreibung, Positionen und Standardtexte professionell bündeln.",
    "Zurück zum Dashboard",
    "/Dashboard",
)

footer()