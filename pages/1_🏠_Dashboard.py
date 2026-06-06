import streamlit as st
from ui.style import apply_global_style

apply_global_style()

st.title("🏠 Dashboard")

st.markdown("""
Willkommen bei ARCHiTool.

Diese Plattform entwickelt sich zu einem vollständigen System für:

- HOAI
- Projektplanung
- LV / Ausschreibung
- Bauleitung
- Kostenmanagement
- AI Werkzeuge
""")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Aktive Projekte", 0)
c2.metric("Berechnungen", 0)
c3.metric("Exportierte Dateien", 0)
c4.metric("Systemstatus", "Online")
