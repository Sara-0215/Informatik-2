import streamlit as st
import plotly.express as px

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
    "Zu Fuß": 0, 
    "E-Bus": 50,
    "Tram": 30
}

# Benutzer-Eingabe
st.markdown("### 🚗 Einzelne Transportmittel")
transportmittel = st.selectbox("Wähle dein Transportmittel:", list(CO2_WERTE.keys()))
km_pro_tag = st.number_input("Wie viele Kilometer fährst du pro Tag?", min_value=0.0, step=0.1)

# Berechnungsfunktion
def berechne_co2(transportmittel, km_pro_tag):
    """Berechnet den jährlichen CO₂-Ausstoss basierend auf Transportmittel und täglicher Strecke."""
    if transportmittel not in CO2_WERTE:
        return None
    co2_pro_jahr = (CO2_WERTE[transportmittel] * km_pro_tag * 365) / 1000  # Umrechnung in kg
    return round(co2_pro_jahr, 2)

# Berechnung starten
if st.button("CO₂ berechnen"):
    ergebnis = berechne_co2(transportmittel, km_pro_tag)
    if ergebnis is not None:
        color = "green" if ergebnis < 1000 else "red"
        st.markdown(f"<h4 style='color:{color}'>Dein jährlicher CO₂-Ausstoß mit {transportmittel} beträgt <b>{ergebnis} kg CO₂</b> pro Jahr.</h4>", unsafe_allow_html=True)
    else:   
        st.error("Bitte wähle ein gültiges Transportmittel.")

st.divider()  # Trennlinie für bessere Struktur

# Multi-Transportmittel Berechnung
st.markdown("### 🔄 Berechnung für mehrere Transportmittel")
co2_input = st.number_input("Gib deinen jährlichen CO₂-Verbrauch in kg ein:", min_value=0.0, step=1.0)
if st.button("Gesamt CO₂ berechnen"):
    color = "green" if co2_input < 5000 else "red"
    st.markdown(f"<h4 style='color:{color}'>Dein Gesamt-CO₂-Ausstoß beträgt <b>{co2_input} kg CO₂</b> pro Jahr.</h4>", unsafe_allow_html=True)

st.divider()  # Trennlinie

import pandas as pd

# Daten für Vergleich mit Schweizer Durchschnitt
average_co2 = 3090

# Benutzer-Eingabe für Vergleich
st.markdown("### 📊 Vergleich mit Durchschnitt")
user_co2 = st.number_input("Gib deinen jährlichen CO₂-Verbrauch in kg ein:", min_value=0.0, step=0.1)

# Daten für das Balkendiagramm
data = pd.DataFrame({
    "Kategorie": ["Durchschnittlicher Schweizer", "Dein Verbrauch"],
    "CO₂-Verbrauch (kg/Jahr)": [average_co2, user_co2]
})

# Balkendiagramm anzeigen
st.bar_chart(data.set_index("Kategorie"), use_container_width=True)

st.divider()  # Trennlinie für bessere Struktur

# Diagramm-Funktion für Transportmittelvergleich
def plot_co2_vergleich(km_pro_tag):
    labels = list(CO2_WERTE.keys())
    werte = [CO2_WERTE[t] * km_pro_tag * 365 / 1000 for t in labels]
    farben = ["green" if w < 1000 else "red" for w in werte]  # Grün für niedrige Werte, Rot für hohe

    fig = px.bar(
        x=labels, 
        y=werte, 
        title="CO₂-Ausstoß verschiedener Transportmittel",
        labels={"x": "Transportmittel", "y": "CO₂-Ausstoß (kg/Jahr)"},
        color=werte,
        color_continuous_scale=["green", "yellow", "red"]
    )
    st.plotly_chart(fig)

# Button und Anzeige
if st.button("Vergleich CO₂ pro Transportmittel anzeigen"):
    if km_pro_tag > 0:
        plot_co2_vergleich(km_pro_tag)
    else:
        st.error("Bitte gib eine gültige Kilometeranzahl ein.")
