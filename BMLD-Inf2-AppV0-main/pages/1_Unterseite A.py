import streamlit as st

# Titel der Unterseite
st.title("🌍 CO₂-Fußabdruck Rechner")

st.write("Berechne deinen jährlichen CO₂-Ausstoß basierend auf deinem Transportmittel.")

# CO₂-Emissionen pro km für verschiedene Transportmittel
CO2_WERTE = {
    "Auto (Benzin)": 120,
    "Auto (Diesel)": 135,
    "Bus": 80,
    "Zug": 40,
    "Flugzeug": 250,
    "Fahrrad": 0,
    "Zu Fuß": 0
}

# Benutzer-Eingabe
transportmittel = st.selectbox("Wähle dein Transportmittel:", list(CO2_WERTE.keys()))
km_pro_tag = st.number_input("Wie viele Kilometer fährst du pro Tag?", min_value=0.0, step=0.1)

# Berechnungsfunktion
def berechne_co2(transportmittel, km_pro_tag):
    """Berechnet den jährlichen CO₂-Ausstoß basierend auf Transportmittel und täglicher Strecke."""
    if transportmittel not in CO2_WERTE:
        return None
    co2_pro_jahr = (CO2_WERTE[transportmittel] * km_pro_tag * 365) / 1000  # Umrechnung in kg
    return round(co2_pro_jahr, 2)

# Berechnung starten
if st.button("CO₂ berechnen"):
    ergebnis = berechne_co2(transportmittel, km_pro_tag)
    if ergebnis is not None:
        st.success(f"Dein jährlicher CO₂-Ausstoß mit {transportmittel} beträgt **{ergebnis} kg CO₂** pro Jahr.")
    else:
        st.error("Bitte wähle ein gültiges Transportmittel.")
st.markdown("<h1 style='text-align: center; color: green;'>🌍 CO₂-Fußabdruck Rechner</h1>", unsafe_allow_html=True)
st.write("Berechne deinen jährlichen CO₂-Ausstoß basierend auf deinem Transportmittel.")

import matplotlib.pyplot as plt

# Balkendiagramm erstellen
def plot_co2_vergleich(dein_wert):
    labels = list(CO2_WERTE.keys())
    werte = [CO2_WERTE[t] * km_pro_tag * 365 / 1000 for t in labels]

    plt.figure(figsize=(8, 5))
    plt.bar(labels, werte, color=['gray' if t != transportmittel else 'green' for t in labels])
    plt.ylabel("CO₂-Ausstoß (kg/Jahr)")
    plt.xticks(rotation=45, ha='right')
    plt.title("CO₂-Ausstoß verschiedener Transportmittel")

    st.pyplot(plt)

if st.button("CO₂ berechnen"):
    ergebnis = berechne_co2(transportmittel, km_pro_tag)
    if ergebnis is not None:
        st.success(f"Dein jährlicher CO₂-Ausstoß mit {transportmittel} beträgt **{ergebnis} kg CO₂**.")
        plot_co2_vergleich(ergebnis)  # Diagramm anzeigen 
        


