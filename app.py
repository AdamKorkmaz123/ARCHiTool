import streamlit as st
from ui.style import apply_global_style
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

st.markdown("""
<div class="hero-card">
    <h1>🏛️ ARCHiTool</h1>
    <p>Professionelles HOAI Honorarangebot-System für Architektur- und Ingenieurbüros.</p>
</div>
""", unsafe_allow_html=True)

if user:
    st.success(f"Willkommen, {user['name']}")
    projects = load_projects(user["id"])
    project_count = len(projects)
else:
    st.warning("Bitte einloggen, um Projekte zu speichern und zu verwalten.")
    project_count = 0

c1, c2, c3, c4 = st.columns(4)

c1.metric("Gespeicherte Projekte", project_count)
c2.metric("Exportformate", "PDF / Word / Excel")
c3.metric("HOAI Modul", "Gebäude")
c4.metric("Status", "Online MVP")

st.markdown("---")

st.header("🚀 Schnellzugriff")

c1, c2, c3 = st.columns(3)

with c1:
    st.page_link(
        "pages/1_🏛️_HOAI_Rechner.py",
        label="🏛️ HOAI Rechner öffnen",
        icon="🏛️"
    )

with c2:
    st.page_link(
        "pages/2_📂_Projekte.py",
        label="📂 Projekte verwalten",
        icon="📂"
    )

with c3:
    st.page_link(
        "pages/3_⚙️_Einstellungen.py",
        label="⚙️ Einstellungen",
        icon="⚙️"
    )

st.markdown("---")

st.header("📌 Aktuelle Module")

st.write("""
ARCHiTool unterstützt aktuell:

- HOAI Gebäude / LPH 1–9
- Anrechenbare Kosten
- Honorarzone I–V
- Basissatz / Mittelsatz / Obersatz
- Umbauzuschlag
- Modernisierungszuschlag
- Instandhaltung / Instandsetzung
- Nebenkosten
- Nachlass / Rabatt / Abschlag
- PDF, Word und Excel Export
- Benutzerlogin
- Benutzerbezogene Projektspeicherung
""")