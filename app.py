import streamlit as st
from ui.style import apply_global_style
from database.database import init_db, load_projects

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="ARCHiTool",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------
# INIT
# ---------------------------------------------------

apply_global_style()
init_db()

user = st.session_state.get("user")

# ---------------------------------------------------
# HERO SECTION
# ---------------------------------------------------

st.markdown("""
<div class="hero-card">
    <h1>🏛️ ARCHiTool</h1>
    <p>
        Professionelles HOAI Honorarangebot-System
        für Architektur- und Ingenieurbüros.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# USER INFO
# ---------------------------------------------------

if user:
    st.success(f"Willkommen, {user['name']}")

    projects = load_projects(user["id"])
    project_count = len(projects)

else:
    st.warning(
        "Bitte einloggen, um Projekte zu speichern und zu verwalten."
    )

    project_count = 0

# ---------------------------------------------------
# DASHBOARD METRICS
# ---------------------------------------------------

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Gespeicherte Projekte",
        project_count
    )

with c2:
    st.metric(
        "Exportformate",
        "PDF / Word / Excel"
    )

with c3:
    st.metric(
        "HOAI Modul",
        "Gebäude"
    )

with c4:
    st.metric(
        "Status",
        "Online MVP"
    )

# ---------------------------------------------------
# QUICK ACCESS
# ---------------------------------------------------

st.markdown("---")

st.header("🚀 Schnellzugriff")

st.info(
    "Navigation bitte über das linke Seitenmenü verwenden."
)

st.markdown("""
### Verfügbare Bereiche

- 🏛️ **HOAI Rechner**  
  Professionelle HOAI-Honorarberechnung

- 📂 **Projekte**  
  Gespeicherte Projekte anzeigen und verwalten

- ⚙️ **Einstellungen**  
  Design, Farben und Firmenlogo anpassen

- 👤 **Login**  
  Benutzerkonto verwalten
""")

# ---------------------------------------------------
# MODULES
# ---------------------------------------------------

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

# ---------------------------------------------------
# ROADMAP
# ---------------------------------------------------

st.markdown("---")

st.header("🛣️ Roadmap")

st.write("""
Geplante Erweiterungen:

- KI-gestützte HOAI Vorschläge
- LV / Ausschreibung Modul
- AVA Integration
- Angebotsvergleich
- Multi-User Team System
- Cloud Datenbank
- E-Mail Versand
- CRM Modul
- Zeiterfassung
- Rechnungsmodul
- HOAI 202X Erweiterungen
""")