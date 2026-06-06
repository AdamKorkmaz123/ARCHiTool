import os
import streamlit as st

from ui.style import apply_global_style
from ui.components import (
    top_navigation,
    section_header,
    info_panel,
    premium_banner,
    footer,
)

from auth.auth import save_user_settings, load_user_settings

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

if "primary_color" not in st.session_state:
    st.session_state.primary_color = "#1e3a8a"

user = st.session_state.get("user")

if user:
    settings = load_user_settings(user["id"])
    st.session_state.dark_mode = settings["dark_mode"]
    st.session_state.primary_color = settings["primary_color"]

apply_global_style()
top_navigation()

st.markdown("""
<div class="hero-platform">
    <div class="hero-badge">EINSTELLUNGEN · DESIGN · BRANDING</div>
    <h1>Plattform-Einstellungen</h1>
    <p>
        Passe ARCHiTool optisch an dein Büro an: Dark Mode,
        Primärfarbe, Firmenlogo und später vollständiges Corporate Design.
    </p>
    <div class="hero-actions">
        <a href="/Dashboard" class="hero-primary">🏠 Zur Übersicht</a>
        <a href="/Login" class="hero-secondary">👤 Benutzerkonto</a>
    </div>
</div>
""", unsafe_allow_html=True)

if not user:
    st.warning("Bitte zuerst einloggen, damit Einstellungen dauerhaft gespeichert werden.")

section_header("Design Einstellungen", "Passe die Oberfläche an dein Büro oder Corporate Design an.")

c1, c2 = st.columns(2)

with c1:
    darkmode = st.toggle(
        "Dark Mode",
        value=st.session_state.dark_mode,
    )

with c2:
    farbe = st.color_picker(
        "Primärfarbe",
        value=st.session_state.primary_color,
    )

section_header("Firmenlogo", "Dieses Logo kann später in PDF- und Word-Dokumenten verwendet werden.")

logo = st.file_uploader(
    "Firmenlogo hochladen",
    type=["png", "jpg", "jpeg"],
)

logo_path = None

if logo:
    os.makedirs("assets", exist_ok=True)

    logo_path = f"assets/user_logo_{user['id']}.png" if user else "assets/temp_logo.png"

    with open(logo_path, "wb") as f:
        f.write(logo.getbuffer())

    st.session_state.logo_path = logo_path
    st.image(logo_path, width=180)

if st.button("✅ Einstellungen speichern"):
    st.session_state.dark_mode = darkmode
    st.session_state.primary_color = farbe

    if logo_path:
        st.session_state.logo_path = logo_path

    if user:
        save_user_settings(
            user["id"],
            darkmode,
            farbe,
        )
        st.success("Einstellungen wurden gespeichert.")
    else:
        st.info("Einstellungen wurden nur temporär angewendet.")

    st.rerun()

section_header("Systeminformationen", "Aktueller Stand der Plattform-Anpassungen.")

info_panel(
    "Temporäre und gespeicherte Einstellungen",
    "Ohne Login gelten Farbe und Dark Mode nur temporär. Mit Login werden sie benutzerbezogen gespeichert.",
    "⚙️",
)

info_panel(
    "Branding Roadmap",
    "Später werden Firmenadresse, Logo, Angebotsnummern, Fußzeilen und PDF-Templates vollständig konfigurierbar.",
    "🏢",
)

premium_banner(
    "Corporate Design vorbereitet",
    "ARCHiTool wird schrittweise zu einer vollständig brandbaren Büroplattform erweitert.",
    "Zurück zum Dashboard",
    "/Dashboard",
)

footer()