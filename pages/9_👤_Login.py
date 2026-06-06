import streamlit as st

from ui.style import apply_global_style
from ui.components import (
    top_navigation,
    section_header,
    info_panel,
    premium_banner,
    footer,
)

from auth.auth import init_auth_db, register_user, login_user


apply_global_style()
top_navigation()
init_auth_db()

if "user" not in st.session_state:
    st.session_state.user = None


st.markdown("""
<div class="hero-platform">
    <div class="hero-badge">BENUTZERKONTO · LOGIN · PROJEKTE · EINSTELLUNGEN</div>
    <h1>Benutzerkonto</h1>
    <p>
        Melde dich an, um Projekte zu speichern, Einstellungen zu sichern
        und später projektbezogene Arbeitsbereiche zu nutzen.
    </p>
    <div class="hero-actions">
        <a href="/Dashboard" class="hero-primary">🏠 Zur Übersicht</a>
        <a href="/HOAI_Rechner" class="hero-secondary">🏛️ HOAI Rechner</a>
    </div>
</div>
""", unsafe_allow_html=True)


if st.session_state.user:
    user = st.session_state.user

    st.success(f"Eingeloggt als {user['name']}")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Benutzer", user["name"])

    with c2:
        st.metric("E-Mail", user["email"])

    with c3:
        st.metric("Status", "Aktiv")

    section_header("Konto Übersicht", "Dein aktueller Login-Status.")

    info_panel(
        "Benutzerkonto aktiv",
        "Du kannst Projekte speichern, gespeicherte Projekte öffnen und persönliche Einstellungen verwenden.",
        "👤",
    )

    if st.button("Logout"):
        st.session_state.user = None
        st.success("Logout erfolgreich.")
        st.rerun()

else:
    section_header(
        "Login oder Registrierung",
        "Erstelle ein Konto oder melde dich an, um ARCHiTool projektbezogen zu nutzen."
    )

    tab1, tab2 = st.tabs(["Login", "Registrieren"])

    with tab1:
        st.subheader("Login")

        email = st.text_input("E-Mail", key="login_email")
        password = st.text_input("Passwort", type="password", key="login_password")

        if st.button("Einloggen"):
            ok, user, msg = login_user(email, password)

            if ok:
                st.session_state.user = user
                st.success(msg)
                st.rerun()
            else:
                st.error(msg)

    with tab2:
        st.subheader("Registrieren")

        name = st.text_input("Name")
        reg_email = st.text_input("E-Mail", key="register_email")
        reg_password = st.text_input("Passwort", type="password", key="register_password")

        if st.button("Konto erstellen"):
            if not name or not reg_email or not reg_password:
                st.warning("Bitte alle Felder ausfüllen.")
            else:
                ok, msg = register_user(name, reg_email, reg_password)

                if ok:
                    st.success(msg)
                else:
                    st.error(msg)

    premium_banner(
        "Warum ein Benutzerkonto?",
        "Mit Login kannst du Projekte speichern, Einstellungen sichern und später Cloud-Funktionen nutzen.",
        "Zum HOAI Rechner",
        "/HOAI_Rechner",
    )


footer()