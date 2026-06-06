import pandas as pd


def interpolate_fee(cost, zone, honorarsatz, table_path):
    df = pd.read_csv(table_path)
    df = df[df["zone"] == zone].sort_values("cost")

    if cost < df["cost"].min() or cost > df["cost"].max():
        raise ValueError("Anrechenbare Kosten HOAI tablosu aralığı dışında.")

    lower = df[df["cost"] <= cost].iloc[-1]
    upper = df[df["cost"] >= cost].iloc[0]

    if lower["cost"] == upper["cost"]:
        min_fee = lower["min"]
        max_fee = lower["max"]
    else:
        ratio = (cost - lower["cost"]) / (upper["cost"] - lower["cost"])
        min_fee = lower["min"] + ratio * (upper["min"] - lower["min"])
        max_fee = lower["max"] + ratio * (upper["max"] - lower["max"])

    if honorarsatz == "Basissatz":
        fee = min_fee
    elif honorarsatz == "Mittelsatz":
        fee = min_fee + (max_fee - min_fee) * 0.5
    else:
        fee = max_fee

    return round(float(fee), 2)


def calculate_hoai_offer(
    base_fee,
    selected_lph,
    adjustments,
    mwst_percent=19,
):
    lph_rows = []
    honorarsumme = 0
    lph8_fee = 0

    for lph, percent in selected_lph.items():
        fee = base_fee * percent / 100
        honorarsumme += fee

        if "LPH 8" in lph:
            lph8_fee = fee

        lph_rows.append({
            "Leistungsphase": lph,
            "Prozent": percent,
            "Honorar netto €": round(fee, 2),
        })

    steps = []
    subtotal = honorarsumme

    steps.append(["Grundhonorar 100%", base_fee])
    steps.append(["Honorarsumme gewählte LPH", honorarsumme])

    ordered_adjustments = sorted(adjustments, key=lambda x: x["order"])

    for adj in ordered_adjustments:
        name = adj["name"]
        value = adj["value"]
        kind = adj["kind"]

        if value == 0:
            continue

        if kind == "percent_plus_current":
            amount = subtotal * value / 100
            subtotal += amount
            steps.append([f"+ {name} {value}%", amount])

        elif kind == "percent_minus_current":
            amount = subtotal * value / 100
            subtotal -= amount
            steps.append([f"- {name} {value}%", -amount])

        elif kind == "percent_plus_lph8":
            amount = lph8_fee * value / 100
            subtotal += amount
            steps.append([f"+ {name} {value}% auf LPH 8", amount])

        elif kind == "fixed_plus":
            amount = value
            subtotal += amount
            steps.append([f"+ {name}", amount])

    netto = subtotal
    mwst = netto * mwst_percent / 100
    brutto = netto + mwst

    steps.append(["Nettohonorar", netto])
    steps.append([f"+ MwSt {mwst_percent}%", mwst])
    steps.append(["Bruttohonorar", brutto])

    summary = {
        "Grundhonorar 100%": round(base_fee, 2),
        "Honorarsumme LPH": round(honorarsumme, 2),
        "Netto": round(netto, 2),
        "MwSt": round(mwst, 2),
        "Brutto": round(brutto, 2),
    }

    return lph_rows, steps, summary