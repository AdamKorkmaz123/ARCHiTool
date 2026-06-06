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
    <div class="hero-badge">KOSTENMANAGEMENT · DIN 276 · BUDGET · CONTROLLING</div>
    <h1>Kostenmanagement für Architektur- und Bauprojekte</h1>
    <p>
        Dieses Modul wird später DIN 276 Kostenstrukturen, Kostenschätzung,
        Kostenberechnung, Kostenanschlag, Kostenfeststellung und laufende
        Kostenkontrolle in einer zentralen Umgebung abbilden.
    </p>
    <div class="hero-actions">
        <a href="/Projekte" class="hero-primary">📂 Projekte öffnen</a>
        <a href="/Dashboard" class="hero-secondary">🏠 Zur Übersicht</a>
    </div>
</div>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Status", "In Entwicklung")
c2.metric("Norm", "DIN 276")
c3.metric("Kostenphasen", "5")
c4.metric("Export", "Geplant")

feature_strip(
    title="Geplante Kostenmanagement-Funktionen",
    text="ARCHiTool soll künftig Kosten vom ersten Schätzwert bis zur Kostenfeststellung strukturiert begleiten.",
    features=[
        "💶 DIN 276",
        "📈 Kostenschätzung",
        "📊 Kostenberechnung",
        "📑 Kostenanschlag",
        "✅ Kostenfeststellung",
        "📉 Kostenkontrolle",
        "📄 Export",
        "🤖 AI Analyse",
    ],
)

section_header("Kostenmanagement-Werkzeuge", "Diese Module werden schrittweise aufgebaut.")

col1, col2, col3 = st.columns(3)

with col1:
    module_card(
        "Coming Soon",
        "💶",
        "DIN 276 Struktur",
        "Kosten nach Kostengruppen erfassen, strukturieren und projektbezogen auswerten.",
        "/Kostenmanagement",
    )

with col2:
    module_card(
        "Coming Soon",
        "📈",
        "Kostenschätzung",
        "Frühe Kostenannahmen anhand Projektart, Flächen, Kennwerten und Kostengruppen.",
        "/Kostenmanagement",
    )

with col3:
    module_card(
        "Coming Soon",
        "📊",
        "Kostenberechnung",
        "Detailliertere Berechnung nach Planungsstand, Gewerken und Kostengruppen.",
        "/Kostenmanagement",
    )

col1, col2, col3 = st.columns(3)

with col1:
    module_card(
        "Coming Soon",
        "📑",
        "Kostenanschlag",
        "Kosten auf Basis von Ausschreibung, Angeboten und Vergabeergebnissen abbilden.",
        "/Kostenmanagement",
    )

with col2:
    module_card(
        "Coming Soon",
        "✅",
        "Kostenfeststellung",
        "Abschlusskosten, Rechnungsstände und Kostenkontrolle dokumentieren.",
        "/Kostenmanagement",
    )

with col3:
    module_card(
        "Coming Soon",
        "🤖",
        "AI Kostenanalyse",
        "KI-gestützte Plausibilitätsprüfung und Kostenkennwertanalyse.",
        "/Kostenmanagement",
    )

section_header("Geplanter Workflow", "So soll das Kostenmodul später funktionieren.")

info_panel(
    "1. Kostengruppen anlegen",
    "Projektkosten werden nach DIN 276 strukturiert und in Kostengruppen gegliedert.",
    "💶",
)

info_panel(
    "2. Kostenphasen erfassen",
    "Schätzung, Berechnung, Anschlag und Feststellung können phasenweise verglichen werden.",
    "📊",
)

info_panel(
    "3. Abweichungen analysieren",
    "Budgetabweichungen und Kostenentwicklungen werden grafisch und tabellarisch dargestellt.",
    "📉",
)

info_panel(
    "4. Berichte exportieren",
    "Kostenberichte können später als PDF, Word oder Excel ausgegeben werden.",
    "📄",
)

premium_banner(
    "Kostenmanagement wird vorbereitet",
    "Dieses Modul wird später DIN 276, Kostenkontrolle und AI-gestützte Kostenanalyse verbinden.",
    "Zurück zum Dashboard",
    "/Dashboard",
)

footer()