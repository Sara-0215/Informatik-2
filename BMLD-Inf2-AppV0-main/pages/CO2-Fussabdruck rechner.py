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
st.markdown("### 🚗 Berechnung für ein Transportmittel")
transportmittel = st.selectbox("Wähle deine Transportmittel:", list(CO2_WERTE.keys()), key="transportmittel_select")

# Kilometer pro Tag eingeben
km_pro_tag = st.number_input(f"Wie viele Kilometer fährst du pro Tag mit {transportmittel}?", min_value=0.0, step=0.1, key="km_input")

def berechne_co2(transportmittel, km_pro_tag):
    """Berechnet den jährlichen CO₂-Ausstoss basierend auf dem gewählten Transportmitteln."""
    if transportmittel not in CO2_WERTE:
        return 0
    return round((CO2_WERTE[transportmittel] * km_pro_tag * 365) / 1000, 2)  # Umrechnung in kg

if st.button("CO₂ berechnen", key="co2_button"):
    gesamt_ergebnis = berechne_co2(transportmittel, km_pro_tag)
    st.success(f"Dein jährlicher CO₂-Ausstoss mit den ausgewählten Transportmitteln beträgt **{gesamt_ergebnis} kg CO₂** pro Jahr.")

 # Speichern der Daten mit DataManager
    data_manager = DataManager()
    data_manager.append_record(
        session_state_key="data_df",
        record_dict={
            "Transportmittel": transportmittel,
            "Kilometer pro Tag": km_pro_tag,
            "Jährlicher CO₂-Ausstoss (kg)": gesamt_ergebnis
        }
    )
 # Anzeigen der gespeicherten Daten
    df = pd.DataFrame(st.session_state.get("data_df", []))
    st.write("### Deine gespeicherten Daten")
    st.dataframe(df)

st.divider()  # Trennlinie

# Durchschnittlicher CO₂-Verbrauch eines Schweizers (in kg pro Jahr)
average_co2 = 3090

# Benutzer-Eingabe für CO₂-Verbrauch
user_co2 = st.number_input("Gib deinen jährlichen CO₂-Verbrauch in kg ein:", min_value=0.0, step=0.1, key="user_co2_input")

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













