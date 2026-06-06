
import streamlit as st
from ui.style import apply_global_style

apply_global_style()

st.title("💶 Kostenmanagement")

st.warning("Modul befindet sich in Entwicklung.")

st.markdown("""
Geplante Funktionen:

- DIN 276
- Kostenschätzung
- Kostenberechnung
- Kostenanschlag
- Kostenkontrolle
""")