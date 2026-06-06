import streamlit as st
import os
from ui.style import apply_global_style
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

st.title("⚙️ Einstellungen")

if not user:
    st.warning("Bitte zuerst einloggen, damit Einstellungen gespeichert werden.")

darkmode = st.toggle(
    "Dark Mode",
    value=st.session_state.dark_mode
)

farbe = st.color_picker(
    "Primärfarbe",
    value=st.session_state.primary_color
)

logo = st.file_uploader(
    "Firmenlogo hochladen",
    type=["png", "jpg", "jpeg"]
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
            farbe
        )
        st.success("Einstellungen wurden gespeichert.")
    else:
        st.info("Einstellungen wurden nur temporär angewendet.")

    st.rerun()