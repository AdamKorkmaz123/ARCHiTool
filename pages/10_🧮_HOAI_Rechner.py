import streamlit as st
from datetime import date, datetime

from ui.style import apply_global_style
from ui.components import (
    top_navigation,
    section_header,
    info_panel,
    premium_banner,
    footer,
)

from core.hoai import interpolate_fee, calculate_hoai_offer
from exports.documents import export_excel, export_word, export_pdf

from database.database import (
    init_db,
    save_project,
    load_projects,
    load_project_data,
    delete_project,
)


apply_global_style()
top_navigation()
init_db()


if "result" not in st.session_state:
    st.session_state.result = None

if "loaded_project" not in st.session_state:
    st.session_state.loaded_project = None


def get_current_user():
    return st.session_state.get("user")


def parse_date(value):
    try:
        if value:
            return datetime.strptime(value, "%Y-%m-%d").date()
    except Exception:
        pass

    return date.today()


def clear_calculation():
    st.session_state.result = None
    st.session_state.loaded_project = None
    st.rerun()


def load_saved_project(project_id):
    user = get_current_user()

    if not user:
        st.warning("Bitte zuerst einloggen.")
        return

    data = load_project_data(project_id, user["id"])

    if data:
        st.session_state.loaded_project = data
        st.session_state.result = data
        st.success("Projekt geladen.")
        st.rerun()


st.markdown("""
<div class="hero-platform">
    <div class="hero-badge">HOAI RECHNER · LPH 1–9 · ANGEBOT · EXPORT</div>
    <h1>HOAI Honorarangebot Rechner</h1>
    <p>
        Berechne professionelle Honorarangebote auf Basis anrechenbarer Kosten,
        Honorarzone, Honorarsatz, Leistungsphasen, Zuschlägen, Nachlässen und Nebenkosten.
    </p>
    <div class="hero-actions">
        <a href="/HOAI_Center" class="hero-primary">🏛️ HOAI Center</a>
        <a href="/Projekte" class="hero-secondary">📂 Projekte</a>
    </div>
</div>
""", unsafe_allow_html=True)


user = get_current_user()

if user:
    st.success(f"Eingeloggt als: {user['name']}")
else:
    st.warning("Nicht eingeloggt. Berechnen ist möglich, Speichern aber erst nach Login.")


with st.expander("📂 Gespeicherte Projekte", expanded=False):
    if not user:
        st.info("Bitte zuerst einloggen, um gespeicherte Projekte zu sehen.")
    else:
        projects = load_projects(user["id"])

        if not projects:
            st.info("Noch keine Projekte gespeichert.")
        else:
            for p in projects:
                project_id, project_name, firma_name, project_date = p

                c1, c2, c3 = st.columns([4, 1, 1])

                with c1:
                    st.write(f"**#{project_id} — {project_name}**")
                    st.caption(f"{firma_name} | {project_date}")

                with c2:
                    if st.button("📂 Öffnen", key=f"load_{project_id}"):
                        load_saved_project(project_id)

                with c3:
                    if st.button("🗑️ Löschen", key=f"delete_{project_id}"):
                        delete_project(project_id, user["id"])
                        st.success("Projekt gelöscht.")
                        st.rerun()


if st.button("🧹 Neue Berechnung / Temizle"):
    clear_calculation()

loaded = st.session_state.loaded_project or {}
loaded_meta = loaded.get("meta", {})
loaded_form = loaded.get("form_data", {})


section_header("Firmendaten", "Angaben zum anbietenden Büro.")

c1, c2 = st.columns(2)

with c1:
    firma = st.text_input(
        "Firma",
        value=loaded_form.get("firma", loaded_meta.get("Firma", "")),
    )

    email = st.text_input(
        "E-Mail",
        value=loaded_form.get("email", loaded_meta.get("E-Mail", "")),
    )

    telefon = st.text_input(
        "Telefon",
        value=loaded_form.get("telefon", loaded_meta.get("Telefon", "")),
    )

with c2:
    adresse = st.text_area(
        "Adresse",
        value=loaded_form.get("adresse", loaded_meta.get("Adresse", "")),
    )

    projektleiter = st.text_input(
        "Projektleiter",
        value=loaded_form.get("projektleiter", loaded_meta.get("Projektleiter", "")),
    )


section_header("Projektdaten", "Projekt, Bauherr, Ort und Datum.")

c1, c2 = st.columns(2)

with c1:
    projektname = st.text_input(
        "Projekt",
        value=loaded_form.get("projektname", loaded_meta.get("Projekt", "")),
    )

    bauherr = st.text_input(
        "Bauherr",
        value=loaded_form.get("bauherr", loaded_meta.get("Bauherr", "")),
    )

with c2:
    ort = st.text_input(
        "Ort",
        value=loaded_form.get("ort", loaded_meta.get("Ort", "")),
    )

    datum = st.date_input(
        "Datum",
        value=parse_date(loaded_form.get("datum", loaded_meta.get("Datum", ""))),
    )


section_header("HOAI Parameter", "Grundlagen der Honorarberechnung.")

zones = ["I", "II", "III", "IV", "V"]
honorarsaetze = ["Basissatz", "Mittelsatz", "Obersatz"]

loaded_zone = loaded_form.get("zone", "III")
loaded_honorarsatz = loaded_form.get("honorarsatz", "Basissatz")

c1, c2, c3, c4 = st.columns(4)

with c1:
    kosten = st.number_input(
        "Anrechenbare Kosten (€)",
        min_value=25000.0,
        value=float(loaded_form.get("kosten", 485500.0)),
        step=10000.0,
    )

with c2:
    zone = st.selectbox(
        "Honorarzone",
        zones,
        index=zones.index(loaded_zone) if loaded_zone in zones else 2,
    )

with c3:
    honorarsatz = st.selectbox(
        "Honorarsatz",
        honorarsaetze,
        index=honorarsaetze.index(loaded_honorarsatz)
        if loaded_honorarsatz in honorarsaetze
        else 0,
    )

with c4:
    mwst = st.number_input(
        "MwSt %",
        value=float(loaded_form.get("mwst", 19.0)),
        step=1.0,
    )


section_header(
    "Zuschläge / Abschläge",
    "Reihenfolge bestimmt, wie Zuschläge und Nachlässe auf Zwischensummen angewendet werden."
)

c1, c2, c3, c4 = st.columns(4)

with c1:
    umbau = st.number_input(
        "Umbauzuschlag %",
        value=float(loaded_form.get("umbau", 0.0)),
    )

with c2:
    umbau_order = st.number_input(
        "Reihenfolge Umbau",
        value=int(loaded_form.get("umbau_order", 1)),
        step=1,
    )

with c3:
    modernisierung = st.number_input(
        "Modernisierungszuschlag %",
        value=float(loaded_form.get("modernisierung", 0.0)),
    )

with c4:
    modernisierung_order = st.number_input(
        "Reihenfolge Modernisierung",
        value=int(loaded_form.get("modernisierung_order", 2)),
        step=1,
    )


c1, c2, c3, c4 = st.columns(4)

with c1:
    instandhaltung = st.number_input(
        "Instandhaltung / Instandsetzung %",
        value=float(loaded_form.get("instandhaltung", 0.0)),
    )

with c2:
    instandhaltung_order = st.number_input(
        "Reihenfolge Instandhaltung",
        value=int(loaded_form.get("instandhaltung_order", 3)),
        step=1,
    )

with c3:
    nebenkosten = st.number_input(
        "Nebenkosten %",
        value=float(loaded_form.get("nebenkosten", 0.0)),
    )

with c4:
    nebenkosten_order = st.number_input(
        "Reihenfolge Nebenkosten",
        value=int(loaded_form.get("nebenkosten_order", 4)),
        step=1,
    )


c1, c2, c3, c4 = st.columns(4)

with c1:
    besondere_leistungen = st.number_input(
        "Besondere Leistungen €",
        value=float(loaded_form.get("besondere_leistungen", 0.0)),
    )

with c2:
    besondere_order = st.number_input(
        "Reihenfolge Besondere Leistungen",
        value=int(loaded_form.get("besondere_order", 5)),
        step=1,
    )

with c3:
    nachlass = st.number_input(
        "Abschlag / Rabatt / Nachlass %",
        value=float(loaded_form.get("nachlass", 0.0)),
    )

with c4:
    nachlass_order = st.number_input(
        "Reihenfolge Nachlass",
        value=int(loaded_form.get("nachlass_order", 6)),
        step=1,
    )


section_header("Leistungsphasen", "Auswahl und Anpassung der LPH 1–9.")

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

loaded_lph = loaded_form.get("selected_lph", {})
selected_lph = {}

for lph, default_percent in lph_data.items():
    c1, c2 = st.columns([4, 1])

    with c1:
        active = st.checkbox(
            lph,
            value=lph in loaded_lph if loaded_lph else True,
            key=f"active_{lph}",
        )

    with c2:
        new_percent = st.number_input(
            f"{lph}_percent",
            value=float(loaded_lph.get(lph, default_percent)),
            label_visibility="collapsed",
            key=f"percent_{lph}",
        )

    if active:
        selected_lph[lph] = new_percent

total_percent = sum(selected_lph.values())

if total_percent > 100:
    st.error(f"Gesamte Leistungsphasen: {total_percent}% — darf 100% nicht überschreiten.")
else:
    st.info(f"Gesamte Leistungsphasen: {total_percent}%")


section_header("Honorarberechnung", "Berechnung, Ergebnis und Export.")

if st.button("🔵 Angebot berechnen"):
    try:
        basis = interpolate_fee(
            cost=kosten,
            zone=zone,
            honorarsatz=honorarsatz,
            table_path="data/hoai_gebaeude_2021.csv",
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
            "Logo": st.session_state.get("logo_path", ""),
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


if st.session_state.result:
    result = st.session_state.result

    st.success("Berechnung erfolgreich")

    summary = result["summary"]

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Grundhonorar 100%", f"{summary['Grundhonorar 100%']:,.2f} €")
    c2.metric("Nettohonorar", f"{summary['Netto']:,.2f} €")
    c3.metric("MwSt", f"{summary['MwSt']:,.2f} €")
    c4.metric("Bruttohonorar", f"{summary['Brutto']:,.2f} €")

    section_header("Leistungsphasen Übersicht")
    st.dataframe(result["lph_rows"], use_container_width=True)

    section_header("HOAI Berechnungsgrundlagen")
    for key, value in result["params"].items():
        st.write(f"**{key}:** {value}")

    section_header("Kademelige Kalkulation")
    for label, value in result["steps"]:
        st.write(f"{label}: {value:,.2f} €")

    if st.button("💾 Projekt speichern"):
        user = get_current_user()

        if not user:
            st.warning("Bitte zuerst einloggen, um Projekte zu speichern.")
        else:
            save_project(
                user["id"],
                result["meta"].get("Projekt", ""),
                result["meta"].get("Firma", ""),
                result["meta"].get("Bauherr", ""),
                result["meta"].get("Datum", ""),
                result,
            )

            st.success("Projekt gespeichert.")

    excel_file = export_excel(
        result["meta"],
        result["params"],
        result["lph_rows"],
        result["steps"],
    )

    word_file = export_word(
        result["meta"],
        result["params"],
        result["lph_rows"],
        result["steps"],
    )

    pdf_file = export_pdf(
        result["meta"],
        result["params"],
        result["lph_rows"],
        result["steps"],
    )

    section_header("Dateien herunterladen")

    d1, d2, d3 = st.columns(3)

    with d1:
        st.download_button(
            "Excel herunterladen",
            data=excel_file,
            file_name="ARCHiTool_Honorarangebot.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )

    with d2:
        st.download_button(
            "Word herunterladen",
            data=word_file,
            file_name="ARCHiTool_Honorarangebot.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )

    with d3:
        st.download_button(
            "PDF herunterladen",
            data=pdf_file,
            file_name="ARCHiTool_Honorarangebot.pdf",
            mime="application/pdf",
        )


premium_banner(
    "HOAI Rechner als aktives Kernmodul",
    "Dieses Modul bildet die Grundlage für spätere HOAI-Angebotsgeneratoren, Projektakten und Premium PDF-Vorlagen.",
    "Zurück zum HOAI Center",
    "/HOAI_Center",
)

footer()