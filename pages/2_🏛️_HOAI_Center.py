import streamlit as st
from ui.style import apply_global_style

apply_global_style()

st.title("🏛️ HOAI Center")

st.markdown("""
ARCHiTool HOAI Center, Architektur- und Ingenieurbüros için HOAI süreçlerini
tek yerde toplayan modül alanıdır.
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("🧮 **HOAI Rechner**\n\nLPH 1–9 Honorarangebot berechnen.")
    st.write("Sol menüden **HOAI Rechner** sayfasını aç.")

with col2:
    st.warning("📚 **HOAI Wissen**\n\nDemnächst: HOAI paragrafları ve açıklamalar.")

with col3:
    st.warning("📄 **Angebot Generator**\n\nDemnächst: hazır teklif metinleri.")