import streamlit as st
from ui.style import apply_global_style
from auth.auth import init_auth_db, register_user, login_user

apply_global_style()
init_auth_db()

st.title("👤 Benutzerkonto")

if "user" not in st.session_state:
    st.session_state.user = None

if st.session_state.user:
    st.success(f"Eingeloggt als {st.session_state.user['name']}")
    st.write(f"E-Mail: {st.session_state.user['email']}")

    if st.button("Logout"):
        st.session_state.user = None
        st.rerun()

else:
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
            ok, msg = register_user(name, reg_email, reg_password)

            if ok:
                st.success(msg)
            else:
                st.error(msg)