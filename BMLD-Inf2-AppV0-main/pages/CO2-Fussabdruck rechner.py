import streamlit as st
import pandas as pd
from functions.co2_calculator import calculate_co2
from utils.data_manager import DataManager

# Titel der Unterseite
st.title("🌍 CO₂-Fussabdruck Rechner")

st.write("Berechne deinen jährlichen CO₂-Ausstoss basierend auf deinem Transportmittel.")

st.divider() # Trennlinie

# CO₂-Emissionen pro km für verschiedene Transportmittel
CO2_WERTE = {
    "Auto (Benzin)": 120,
    "Auto (Diesel)": 135,
    "Bus": 80,
    "Zug": 40,
    "Flugzeug": 250,
    "Fahrrad": 0,
    "Zu Fuss": 0, 
    "E-Bus": 50,
    "Tram": 30
}

# Multi-Transportmittel Berechnung
st.markdown("### 🚗 Berechnung für mehrere Transportmittel")
ausgewaehlte_transportmittel = st.multiselect("Wähle deine Transportmittel:", list(CO2_WERTE.keys()), key="ausgewaehlte_transportmittel")

km_pro_tag_mehrere = {}
for t in ausgewaehlte_transportmittel:
    km_pro_tag_mehrere[t] = st.number_input(f"Wie viele Kilometer fährst du pro Tag mit {t}?", min_value=0.0, step=0.1, key=t)

def berechne_gesamt_co2(km_pro_tag_mehrere):
    """Berechnet den jährlichen CO₂-Ausstoss basierend auf mehreren Transportmitteln und deren täglicher Strecke."""
    gesamt_co2 = 0
    for t, km in km_pro_tag_mehrere.items():
        gesamt_co2 += (CO2_WERTE[t] * km * 365) / 1000  # Umrechnung in kg
    return round(gesamt_co2, 2)

if st.button("Gesamt CO₂ berechnen", key="co2_button_2"):
    gesamt_ergebnis = berechne_gesamt_co2(km_pro_tag_mehrere)
    st.success(f"Dein jährlicher CO₂-Ausstoss mit den ausgewählten Transportmitteln beträgt **{gesamt_ergebnis} kg CO₂** pro Jahr.")


    for t, km in km_pro_tag_mehrere.items():
        DataManager.append_record(
            session_state="data.df",
            record_dict={
            "Transportmittel": t,
            "Kilometer pro Tag": km,
            "Jährlicher CO₂-Ausstoß (kg)": round((CO2_WERTE[t] * km * 365) / 1000, 2)
        })

# Benutzer-Eingabe
transportmittel = st.selectbox("Wähle dein Transportmittel:", list(CO2_WERTE.keys()), key="transportmittel_select_2")
km_pro_tag = st.number_input("Wie viele Kilometer fährst du pro Tag?", min_value=0.0, step=0.1)

# Button zum Berechnen
if st.button("CO₂ berechnen", key="co2_button_3"):
    ergebnis = calculate_co2(transportmittel, km_pro_tag)
    st.success(f"Dein jährlicher CO₂-Ausstoß beträgt **{ergebnis['Jährlicher CO₂-Ausstoß (kg)']}** kg CO₂ pro Jahr.")
    DataManager.append_record(
        session_state="data_df",
        record_dict=ergebnis
    )

df = pd.DataFrame(st.session_state["data.df"])
st.write("### Deine eingegebenen Daten")
st.dataframe(df)

st.divider()  # Trennlinie

import pandas as pd
import streamlit as st

# Durchschnittlicher CO₂-Verbrauch eines Schweizers (in kg pro Jahr)
average_co2 = 3090

# Benutzer-Eingabe für CO₂-Verbrauch
user_co2 = st.number_input("Gib deinen jährlichen CO₂-Verbrauch in kg ein:", min_value=0.0, step=0.1)

# Daten vorbereiten
data = pd.DataFrame({
    "Kategorie": ["Durchschnittlicher Schweizer", "Dein Verbrauch"],
    "CO₂-Verbrauch (kg/Jahr)": [average_co2, user_co2],
    "Farbe": ["#FF4B4B" if user_co2 > average_co2 else "#32CD32", "#32CD32"]
})

# Balkendiagramm anzeigen
st.bar_chart(
    data.set_index("Kategorie"),
    y="CO₂-Verbrauch (kg/Jahr)",
    color="Farbe",
    horizontal=True,  # hier setzen wir horizontal=True
    use_container_width=True
)
st.divider()













