import streamlit as st
from datetime import date

from core.hoai import interpolate_fee, calculate_hoai_offer
from exports.documents import export_excel, export_word, export_pdf

from database.database import (
    init_db,
    save_project,
    load_projects,
    load_project_data,
    delete_project
)

st.set_page_config(page_title="ARCHiTool", page_icon="🏛️", layout="wide")
init_db()


# ---------------------------------------------------
# SESSION
# ---------------------------------------------------

if "result" not in st.session_state:
    st.session_state.result = None

if "loaded_project" not in st.session_state:
    st.session_state.loaded_project = None


def clear_all():
    st.session_state.clear()
    st.rerun()


def load_saved_project(project_id):
    data = load_project_data(project_id)

    if data:
        st.session_state.loaded_project = data
        st.session_state.result = data
        st.rerun()


# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

with st.sidebar:
    st.header("📂 Projekte")

    projects = load_projects()

    if not projects:
        st.info("Noch keine Projekte gespeichert.")

    for p in projects:
        project_id, project_name, firma_name, project_date = p

        st.write(f"**#{project_id} — {project_name}**")
        st.caption(f"{firma_name} | {project_date}")

        col_open, col_delete = st.columns(2)

        with col_open:
            if st.button("📂 Aç", key=f"load_{project_id}"):
                load_saved_project(project_id)

        with col_delete:
            if st.button("🗑️ Sil", key=f"delete_{project_id}"):
                delete_project(project_id)
                st.success("Projekt gelöscht.")
                st.rerun()

        st.markdown("---")

    if st.button("🧹 Alles löschen / Yeni hesaplama"):
        clear_all()


# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.title("🏛️ ARCHiTool")
st.subheader("HOAI Honorarangebot Rechner")

st.markdown("---")


# ---------------------------------------------------
# LOADED DATA
# ---------------------------------------------------

loaded = st.session_state.loaded_project or {}

loaded_meta = loaded.get("meta", {})
loaded_params = loaded.get("params", {})


# ---------------------------------------------------
# COMPANY DATA
# ---------------------------------------------------

st.header("🏢 Firmendaten")

c1, c2 = st.columns(2)

with c1:
    firma = st.text_input(
        "Firma",
        value=loaded_meta.get("Firma", "")
    )

    email = st.text_input(
        "E-Mail",
        value=loaded_meta.get("E-Mail", "")
    )

    telefon = st.text_input(
        "Telefon",
        value=loaded_meta.get("Telefon", "")
    )

with c2:
    adresse = st.text_area(
        "Adresse",
        value=loaded_meta.get("Adresse", "")
    )

    projektleiter = st.text_input(
        "Projektleiter",
        value=loaded_meta.get("Projektleiter", "")
    )


# ---------------------------------------------------
# PROJECT DATA
# ---------------------------------------------------

st.header("📁 Projektdaten")

c1, c2 = st.columns(2)

with c1:
    projektname = st.text_input(
        "Projekt",
        value=loaded_meta.get("Projekt", "")
    )

    bauherr = st.text_input(
        "Bauherr",
        value=loaded_meta.get("Bauherr", "")
    )

with c2:
    ort = st.text_input(
        "Ort",
        value=loaded_meta.get("Ort", "")
    )

    datum = st.date_input("Datum", value=date.today())


# ---------------------------------------------------
# HOAI DATA
# ---------------------------------------------------

st.header("📐 HOAI Parameter")

c1, c2, c3, c4 = st.columns(4)

with c1:
    kosten = st.number_input(
        "Anrechenbare Kosten (€)",
        min_value=25000.0,
        value=485500.0,
        step=10000.0
    )

with c2:
    zone = st.selectbox(
        "Honorarzone",
        ["I", "II", "III", "IV", "V"],
        index=2
    )

with c3:
    honorarsatz = st.selectbox(
        "Honorarsatz",
        ["Basissatz", "Mittelsatz", "Obersatz"]
    )

with c4:
    mwst = st.number_input(
        "MwSt %",
        value=19.0,
        step=1.0
    )


# ---------------------------------------------------
# ADJUSTMENTS
# ---------------------------------------------------

st.header("➕ Zuschläge / Abschläge")

st.info(
    "Die Reihenfolge bestimmt, in welcher Reihenfolge Zuschläge und Abschläge "
    "auf die aktuelle Zwischensumme angewendet werden."
)

c1, c2, c3, c4 = st.columns(4)

with c1:
    umbau = st.number_input("Umbauzuschlag %", value=0.0)

with c2:
    umbau_order = st.number_input("Reihenfolge Umbau", value=1, step=1)

with c3:
    modernisierung = st.number_input("Modernisierungszuschlag %", value=0.0)

with c4:
    modernisierung_order = st.number_input("Reihenfolge Modernisierung", value=2, step=1)


c1, c2, c3, c4 = st.columns(4)

with c1:
    instandhaltung = st.number_input(
        "Instandhaltung / Instandsetzung %",
        value=0.0
    )

with c2:
    instandhaltung_order = st.number_input(
        "Reihenfolge Instandhaltung",
        value=3,
        step=1
    )

with c3:
    nebenkosten = st.number_input("Nebenkosten %", value=0.0)

with c4:
    nebenkosten_order = st.number_input(
        "Reihenfolge Nebenkosten",
        value=4,
        step=1
    )


c1, c2, c3, c4 = st.columns(4)

with c1:
    besondere_leistungen = st.number_input(
        "Besondere Leistungen €",
        value=0.0
    )

with c2:
    besondere_order = st.number_input(
        "Reihenfolge Besondere Leistungen",
        value=5,
        step=1
    )

with c3:
    nachlass = st.number_input(
        "Abschlag / Rabatt / Nachlass %",
        value=0.0
    )

with c4:
    nachlass_order = st.number_input(
        "Reihenfolge Nachlass",
        value=6,
        step=1
    )


# ---------------------------------------------------
# LPH
# ---------------------------------------------------

st.header("📊 Leistungsphasen")

lph_data = {
    "LPH 1 Grundlagenermittlung": 2,
    "LPH 2 Vorplanung": 7,
    "LPH 3 Entwurfsplanung": 15,
    "LPH 4 Genehmigungsplanung": 3,
    "LPH 5 Ausführungsplanung": 25,
    "LPH 6 Vorbereitung Vergabe": 10,
    "LPH 7 Mitwirkung Vergabe": 4,
    "LPH 8 Objektüberwachung": 32,
    "LPH 9 Objektbetreuung": 2,
}

selected_lph = {}

for lph, percent in lph_data.items():
    c1, c2 = st.columns([4, 1])

    with c1:
        active = st.checkbox(lph, value=True, key=f"active_{lph}")

    with c2:
        new_percent = st.number_input(
            f"{lph}_percent",
            value=float(percent),
            label_visibility="collapsed",
            key=f"percent_{lph}"
        )

    if active:
        selected_lph[lph] = new_percent

total_percent = sum(selected_lph.values())

if total_percent > 100:
    st.error(f"Gesamte Leistungsphasen: {total_percent}% — darf 100% nicht überschreiten.")
else:
    st.info(f"Gesamte Leistungsphasen: {total_percent}%")


# ---------------------------------------------------
# CALCULATION
# ---------------------------------------------------

st.markdown("---")
st.header("💰 Honorarberechnung")

if st.button("🔵 Angebot berechnen"):
    try:
        basis = interpolate_fee(
            cost=kosten,
            zone=zone,
            honorarsatz=honorarsatz,
            table_path="data/hoai_gebaeude_2021.csv"
        )

        adjustments = [
            {
                "name": "Umbauzuschlag",
                "value": umbau,
                "order": umbau_order,
                "kind": "percent_plus_current",
            },
            {
                "name": "Modernisierungszuschlag",
                "value": modernisierung,
                "order": modernisierung_order,
                "kind": "percent_plus_current",
            },
            {
                "name": "Instandhaltung / Instandsetzung",
                "value": instandhaltung,
                "order": instandhaltung_order,
                "kind": "percent_plus_lph8",
            },
            {
                "name": "Nebenkosten",
                "value": nebenkosten,
                "order": nebenkosten_order,
                "kind": "percent_plus_current",
            },
            {
                "name": "Besondere Leistungen",
                "value": besondere_leistungen,
                "order": besondere_order,
                "kind": "fixed_plus",
            },
            {
                "name": "Abschlag / Rabatt / Nachlass",
                "value": nachlass,
                "order": nachlass_order,
                "kind": "percent_minus_current",
            },
        ]

        lph_rows, steps, summary = calculate_hoai_offer(
            base_fee=basis,
            selected_lph=selected_lph,
            adjustments=adjustments,
            mwst_percent=mwst,
        )

        meta = {
            "Firma": firma,
            "Adresse": adresse,
            "E-Mail": email,
            "Telefon": telefon,
            "Projektleiter": projektleiter,
            "Projekt": projektname,
            "Bauherr": bauherr,
            "Ort": ort,
            "Datum": str(datum),
        }

        params = {
            "Anrechenbare Kosten": f"{kosten:,.2f} €",
            "Honorarzone": zone,
            "Honorarsatz": honorarsatz,
            "Gewählte LPH Summe": f"{total_percent}%",
            "Umbauzuschlag": f"{umbau}%",
            "Modernisierungszuschlag": f"{modernisierung}%",
            "Instandhaltung / Instandsetzung": f"{instandhaltung}%",
            "Nebenkosten": f"{nebenkosten}%",
            "Besondere Leistungen": f"{besondere_leistungen:,.2f} €",
            "Abschlag / Rabatt / Nachlass": f"{nachlass}%",
            "MwSt": f"{mwst}%",
        }

        form_data = {
            "firma": firma,
            "email": email,
            "telefon": telefon,
            "adresse": adresse,
            "projektleiter": projektleiter,
            "projektname": projektname,
            "bauherr": bauherr,
            "ort": ort,
            "datum": str(datum),
            "kosten": kosten,
            "zone": zone,
            "honorarsatz": honorarsatz,
            "mwst": mwst,
            "umbau": umbau,
            "umbau_order": umbau_order,
            "modernisierung": modernisierung,
            "modernisierung_order": modernisierung_order,
            "instandhaltung": instandhaltung,
            "instandhaltung_order": instandhaltung_order,
            "nebenkosten": nebenkosten,
            "nebenkosten_order": nebenkosten_order,
            "besondere_leistungen": besondere_leistungen,
            "besondere_order": besondere_order,
            "nachlass": nachlass,
            "nachlass_order": nachlass_order,
            "selected_lph": selected_lph,
        }

        st.session_state.result = {
            "meta": meta,
            "params": params,
            "lph_rows": lph_rows,
            "steps": steps,
            "summary": summary,
            "form_data": form_data,
        }

    except Exception as e:
        st.error(str(e))


# ---------------------------------------------------
# RESULT DISPLAY
# ---------------------------------------------------

if st.session_state.result:
    result = st.session_state.result

    st.success("Berechnung erfolgreich")

    summary = result["summary"]

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Grundhonorar 100%",
        f"{summary['Grundhonorar 100%']:,.2f} €"
    )

    c2.metric(
        "Nettohonorar",
        f"{summary['Netto']:,.2f} €"
    )

    c3.metric(
        "MwSt",
        f"{summary['MwSt']:,.2f} €"
    )

    c4.metric(
        "Bruttohonorar",
        f"{summary['Brutto']:,.2f} €"
    )

    st.subheader("Leistungsphasen Übersicht")
    st.dataframe(result["lph_rows"], use_container_width=True)

    st.subheader("HOAI Berechnungsgrundlagen")

    for key, value in result["params"].items():
        st.write(f"**{key}:** {value}")

    st.subheader("Kademelige Kalkulation")

    for label, value in result["steps"]:
        st.write(f"{label}: {value:,.2f} €")

    st.markdown("---")

    col_save, col_info = st.columns([1, 3])

    with col_save:
        if st.button("💾 Projekt speichern"):
            save_project(
                result["meta"].get("Projekt", ""),
                result["meta"].get("Firma", ""),
                result["meta"].get("Datum", ""),
                result,
            )

            st.success("Projekt gespeichert. Bitte Seite neu laden oder Berechnung erneut speichern, damit es links erscheint.")

    excel_file = export_excel(
        result["meta"],
        result["params"],
        result["lph_rows"],
        result["steps"]
    )

    word_file = export_word(
        result["meta"],
        result["params"],
        result["lph_rows"],
        result["steps"]
    )

    pdf_file = export_pdf(
        result["meta"],
        result["params"],
        result["lph_rows"],
        result["steps"]
    )

    st.subheader("📥 Dateien herunterladen")

    d1, d2, d3 = st.columns(3)

    with d1:
        st.download_button(
            "Excel herunterladen",
            data=excel_file,
            file_name="ARCHiTool_Honorarangebot.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    with d2:
        st.download_button(
            "Word herunterladen",
            data=word_file,
            file_name="ARCHiTool_Honorarangebot.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

    with d3:
        st.download_button(
            "PDF herunterladen",
            data=pdf_file,
            file_name="ARCHiTool_Honorarangebot.pdf",
            mime="application/pdf"
        )