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
    <div class="hero-badge">HOAI CENTER · HONORAR · LPH · ANGEBOTE</div>
    <h1>HOAI Center für professionelle Honorarangebote</h1>
    <p>
        Das HOAI Center bündelt Honorarberechnung, Leistungsphasen,
        Zuschläge, Abschläge, Angebotserstellung und zukünftige HOAI-Wissensmodule
        in einem zentralen Arbeitsbereich.
    </p>
    <div class="hero-actions">
        <a href="/HOAI_Rechner" class="hero-primary">🧮 HOAI Rechner öffnen</a>
        <a href="/Projekte" class="hero-secondary">📂 Projekte ansehen</a>
    </div>
</div>
""", unsafe_allow_html=True)


c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Status", "Aktiv")

with c2:
    st.metric("LPH", "1–9")

with c3:
    st.metric("Export", "PDF / Word / Excel")

with c4:
    st.metric("Modulgruppe", "HOAI")


feature_strip(
    title="HOAI Funktionen an einem Ort",
    text="Das HOAI Center wird Schritt für Schritt zu einer vollständigen HOAI-Arbeitsumgebung erweitert.",
    features=[
        "🧮 Honorarrechner",
        "📊 LPH Analyse",
        "➕ Zuschläge",
        "➖ Nachlässe",
        "📄 Angebotsexport",
        "📚 HOAI Wissen",
        "🏗️ Projektbezug",
        "🤖 AI Assistent",
    ],
)


section_header(
    "Verfügbare HOAI Werkzeuge",
    "Aktive und geplante Funktionen des HOAI Centers."
)

col1, col2, col3 = st.columns(3)

with col1:
    module_card(
        "Aktiv",
        "🧮",
        "HOAI Rechner",
        "Berechnung von Honoraren auf Basis anrechenbarer Kosten, Honorarzone, Honorarsatz und Leistungsphasen.",
        "/HOAI_Rechner",
    )

with col2:
    module_card(
        "Coming Soon",
        "📚",
        "HOAI Wissen",
        "HOAI Grundlagen, Begriffe, Paragraphen, Leistungsbilder und erklärende Fachinformationen.",
        "/HOAI_Center",
    )

with col3:
    module_card(
        "Coming Soon",
        "📄",
        "Angebot Generator",
        "Automatisch formulierte Honorarangebote mit Textbausteinen, Firmenbranding und PDF Layout.",
        "/HOAI_Center",
    )


col1, col2, col3 = st.columns(3)

with col1:
    module_card(
        "Coming Soon",
        "📊",
        "LPH Analyse",
        "Analyse und Visualisierung der Leistungsphasen, Honoraranteile und Projektstruktur.",
        "/HOAI_Center",
    )

with col2:
    module_card(
        "Coming Soon",
        "🏗️",
        "Projektbezogene HOAI",
        "HOAI-Daten direkt mit gespeicherten Projekten, Kunden und Dokumenten verbinden.",
        "/Projekte",
    )

with col3:
    module_card(
        "Coming Soon",
        "🤖",
        "AI HOAI Assistent",
        "KI-gestützte Vorschläge für Honorarstruktur, Zuschläge, Angebotstexte und Projektlogik.",
        "/HOAI_Center",
    )


section_header(
    "HOAI Workflow",
    "So soll der professionelle Ablauf im HOAI Center funktionieren."
)

info_panel(
    "1. Projektdaten erfassen",
    "Firma, Bauherr, Projektort, Datum, anrechenbare Kosten und Honorarparameter werden strukturiert erfasst.",
    "📁",
)

info_panel(
    "2. Leistungsphasen bestimmen",
    "LPH 1–9 können aktiviert, angepasst und mit individuellen Prozentsätzen versehen werden.",
    "📊",
)

info_panel(
    "3. Zuschläge und Nachlässe berechnen",
    "Umbauzuschlag, Modernisierung, Nebenkosten, besondere Leistungen und Nachlässe werden schrittweise berechnet.",
    "➕",
)

info_panel(
    "4. Angebot exportieren",
    "Das Ergebnis kann als Excel, Word oder PDF exportiert und später mit Premium Templates erweitert werden.",
    "📄",
)


premium_banner(
    "HOAI Rechner ist bereits aktiv",
    "Starte direkt mit der Honorarberechnung und erstelle dein erstes professionelles Angebot.",
    "HOAI Rechner öffnen",
    "/HOAI_Rechner",
)


section_header(
    "Geplante Erweiterungen",
    "Das HOAI Center wird kontinuierlich ausgebaut."
)

st.markdown("""
<div class="feature-strip">
    <h3>Roadmap HOAI Center</h3>
    <p>
        Der aktuelle Rechner ist der erste aktive Baustein. Danach folgen Wissen,
        automatische Angebotstexte, Projektbezug und AI-gestützte Prüfung.
    </p>

    <div class="feature-list">
        <div class="feature-item">📚 HOAI Lexikon</div>
        <div class="feature-item">📄 Angebotsvorlagen</div>
        <div class="feature-item">📊 Diagramme</div>
        <div class="feature-item">🏢 Firmenbranding</div>
        <div class="feature-item">🧾 Angebotsnummern</div>
        <div class="feature-item">🔍 Plausibilitätsprüfung</div>
        <div class="feature-item">🤖 AI Texte</div>
        <div class="feature-item">☁️ Cloud Speicherung</div>
    </div>
</div>
""", unsafe_allow_html=True)


footer()