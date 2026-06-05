import streamlit as st
from ui.style import apply_global_style
from database.database import load_projects, load_project_data, delete_project

apply_global_style()

st.title("📂 Projekte")

user = st.session_state.get("user")

if not user:
    st.warning("Bitte zuerst einloggen.")
    st.stop()

projects = load_projects(user["id"])

if not projects:
    st.info("Noch keine Projekte gespeichert.")
else:
    for p in projects:
        project_id, project_name, firma_name, project_date = p

        with st.container():
            st.subheader(f"#{project_id} — {project_name}")
            st.write(f"**Firma:** {firma_name}")
            st.write(f"**Datum:** {project_date}")

            c1, c2 = st.columns(2)

            with c1:
                if st.button("📂 Projekt öffnen", key=f"open_{project_id}"):
                    data = load_project_data(project_id, user["id"])
                    st.session_state.loaded_project = data
                    st.session_state.result = data
                    st.success("Projekt geladen. Bitte zum HOAI Rechner wechseln.")

            with c2:
                if st.button("🗑️ Projekt löschen", key=f"delete_{project_id}"):
                    delete_project(project_id, user["id"])
                    st.success("Projekt gelöscht.")
                    st.rerun()

            st.markdown("---")