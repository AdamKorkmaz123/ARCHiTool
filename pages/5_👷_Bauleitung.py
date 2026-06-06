import streamlit as st
from ui.style import apply_global_style

apply_global_style()

st.title("👷 Bauleitung")

st.warning("Dieses Modul befindet sich in Entwicklung.")

st.markdown("""
Geplante Funktionen:

- Bauleitungskosten Tabelle
- Bautagebuch
- Mängelmanagement
- Baustellenbericht
- Fotodokumentation
- Abnahmeprotokolle
""")