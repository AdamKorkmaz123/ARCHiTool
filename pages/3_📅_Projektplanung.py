import streamlit as st
from ui.style import apply_global_style

apply_global_style()

st.title("📅 Projektplanung")

st.warning("Modul befindet sich in Entwicklung.")

st.markdown("""
Geplante Funktionen:

- Bauablaufplan
- Terminplanung
- Gantt Diagramme
- Projektphasen
- Meilensteine
- Ressourcenplanung
""")