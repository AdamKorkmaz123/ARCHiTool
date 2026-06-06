import streamlit as st

from ui.style import apply_global_style

from ui.components import (
    top_navigation,
    hero_section,
    section_header,
    module_card,
    feature_strip,
    roadmap_columns,
    info_panel,
    premium_banner,
    footer,
)

from database.database import init_db, load_projects


st.set_page_config(
    page_title="ARCHiTool",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded",
)


apply_global_style()
init_db()

user = st.session_state.get("user")

if user:
    projects = load_projects(user["id"])
    project_count = len(projects)
else:
    project_count = 0


top_navigation()


hero_section(
    badge="ARCHITECTURE · HOAI · LV · BAULEITUNG · DIN276 · AI",
    title="Die nächste Generation digitaler Architekturplattformen",
    text="""
    ARCHiTool verbindet HOAI-Honorarberechnung, Projektplanung,
    Ausschreibung, Kostenmanagement, Bauleitung und AI-gestützte
    Architekturwerkzeuge in einer zentralen professionellen Plattform.
    """,
    primary_label="🏛️ HOAI Center öffnen",
    primary_link="/HOAI_Center",
    secondary_label="📂 Projekte ansehen",
    secondary_link="/Projekte",
)


if user:
    st.success(f"Willkommen zurück, {user['name']}")
else:
    st.warning(
        "Nicht eingeloggt — Projekte und Einstellungen "
        "werden erst nach Login gespeichert."
    )


c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Gespeicherte Projekte", project_count)

with c2:
    st.metric("Aktive Module", "12")

with c3:
    st.metric("Systemstatus", "Online")

with c4:
    st.metric("Exportformate", "PDF / DOCX / XLSX")


feature_strip(
    title="Alles in einer Architekturplattform",
    text="""
    ARCHiTool wurde als vollständiges digitales Betriebssystem
    für Architektur- und Ingenieurbüros konzipiert.
    """,
    features=[
        "🏛️ HOAI",
        "📋 LV Generator",
        "📅 Bauablaufplan",
        "📊 DIN 276",
        "👷 Bauleitung",
        "📂 Projektakte",
        "🤖 AI Assistent",
        "📄 Premium PDF",
    ],
)


section_header(
    "Plattform Module",
    "Modulare professionelle Werkzeuge für Architektur und Bauwesen.",
)

col1, col2, col3 = st.columns(3)

with col1:
    module_card(
        status="Aktiv",
        icon="🏛️",
        title="HOAI Center",
        text="""
        Vollständige HOAI Plattform mit Rechner,
        Wissensdatenbank, LPH Analyse und
        professioneller Angebotserstellung.
        """,
        link="/HOAI_Center",
    )

    module_card(
        status="Aktiv",
        icon="📂",
        title="Projektmanagement",
        text="""
        Projektübersicht, Kundenverwaltung,
        Dokumentation und Projektakte
        in zentraler Umgebung.
        """,
        link="/Projekte",
    )

with col2:
    module_card(
        status="Aktiv",
        icon="📅",
        title="Projektplanung",
        text="""
        Bauablaufpläne, Terminplanung,
        Meilensteine und Gantt-Strukturen
        für komplexe Bauprojekte.
        """,
        link="/Projektplanung",
    )

    module_card(
        status="Coming Soon",
        icon="👷",
        title="Bauleitung",
        text="""
        Bautagebuch, Mängelmanagement,
        Fotodokumentation und
        Baustellenkoordination.
        """,
        link="/Bauleitung",
    )

with col3:
    module_card(
        status="Coming Soon",
        icon="📋",
        title="Ausschreibung / LV",
        text="""
        Automatische LV-Erstellung,
        Positionen, Standardtexte
        und AI-basierte Leistungsverzeichnisse.
        """,
        link="/Ausschreibung_LV",
    )

    module_card(
        status="Coming Soon",
        icon="💶",
        title="Kostenmanagement",
        text="""
        DIN 276 Kostenstruktur,
        Kostenschätzung, Kostenkontrolle
        und Budgetverwaltung.
        """,
        link="/Kostenmanagement",
    )


section_header(
    "Professionelle Architekturplattform",
    "ARCHiTool wurde für reale Architektur- und Ingenieurbüros entwickelt.",
)

info_panel(
    title="Enterprise Architektur",
    text="""
    Modulare Plattformstruktur mit skalierbarer Architektur.
    Neue Module können jederzeit integriert werden:
    AVA, CRM, LV, BIM, AI-Assistenten oder Kostenmanagement.
    """,
    icon="🏗️",
)

info_panel(
    title="Premium Dokumentenerstellung",
    text="""
    Hochwertige PDF-, Word- und Excel-Dokumente
    mit Firmenbranding, Logos und professionellen Layouts.
    """,
    icon="📄",
)

info_panel(
    title="Zukunftssichere Plattform",
    text="""
    Die gesamte Plattform wurde vorbereitet
    für Cloud-Datenbanken, Teamverwaltung,
    APIs und zukünftige AI-Integrationen.
    """,
    icon="🚀",
)


premium_banner(
    title="ARCHiTool Professional Platform",
    text="""
    Die digitale Komplettlösung für Architektur,
    Projektmanagement, Ausschreibung und Bauleitung.
    """,
    button_label="Plattform öffnen",
    button_link="/HOAI_Center",
)


section_header(
    "Produkt Roadmap",
    "Die Plattform wird kontinuierlich erweitert.",
)

roadmap_columns()


section_header(
    "Technologie & Plattform",
    "Professionelle SaaS Architektur für moderne AEC Workflows.",
)

st.markdown(
    """
<div class="main-card">

### Plattformstruktur

- Multi-Page Enterprise Architektur
- Benutzerbasierte Projektdatenbanken
- Responsive SaaS Oberfläche
- Modulares Komponenten-System
- Premium UI / UX
- AI-Ready Architektur
- Cloud Erweiterbarkeit
- Teamfähige Struktur
- Export-System
- Future BIM Integration

</div>
""",
    unsafe_allow_html=True,
)


footer()