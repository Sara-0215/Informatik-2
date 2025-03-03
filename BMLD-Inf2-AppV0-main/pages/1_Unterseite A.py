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

import streamlit as st
import plotly.express as px  # Für Diagramme

# CO₂-Emissionen in g/km für verschiedene Transportmittel
CO2_WERTE = {
    "Auto (Benzin)": 120,
    "Auto (Diesel)": 135,
    "Bus": 80,
    "Zug": 40,
    "Flugzeug": 250,
    "Fahrrad": 0,
    "Zu Fuß": 0
}

# Titel der Unterseite
st.title("🌍 CO₂-Fußabdruck Rechner")
st.write("Berechne deinen jährlichen CO₂-Ausstoß basierend auf deinem Transportmittel.")

# Eingabefelder
transportmittel = st.selectbox("Wähle dein Transportmittel:", list(CO2_WERTE.keys()))
km_pro_tag = st.number_input("Wie viele Kilometer fährst du pro Tag?", min_value=0.0, step=0.1)

# Berechnungsfunktion
def berechne_co2(transportmittel, km_pro_tag):
    """Berechnet den jährlichen CO₂-Ausstoß basierend auf Transportmittel und täglicher Strecke."""
    if transportmittel not in CO2_WERTE:
        return None
    co2_pro_jahr = (CO2_WERTE[transportmittel] * km_pro_tag * 365) / 1000  # Umrechnung in kg
    return round(co2_pro_jahr, 2)

# Diagramm-Funktion
def plot_co2_vergleich(dein_transportmittel, dein_wert):
    df = {"Transportmittel": list(CO2_WERTE.keys()), 
          "CO₂-Ausstoß (kg/Jahr)": [CO2_WERTE[t] * km_pro_tag * 365 / 1000 for t in CO2_WERTE.keys()]}
    
    fig = px.bar(df, x="Transportmittel", y="CO₂-Ausstoß (kg/Jahr)", title="CO₂-Ausstoß verschiedener Transportmittel",
                 color="Transportmittel", labels={"CO₂-Ausstoß (kg/Jahr)": "CO₂ (kg/Jahr)"})
    
    st.plotly_chart(fig)

# Berechnung starten
if st.button("CO₂ berechnen"):
    ergebnis = berechne_co2(transportmittel, km_pro_tag)
    if ergebnis is not None:
        st.success(f"Dein jährlicher CO₂-Ausstoß mit {transportmittel} beträgt **{ergebnis} kg CO₂** pro Jahr.")
        plot_co2_vergleich(transportmittel, ergebnis)  # Diagramm anzeigen
    else:
        st.error("Bitte wähle ein gültiges Transportmittel.") 

transportmittel = st.selectbox("Wähle dein Transportmittel:", list(CO2_WERTE.keys()), key="transportwahl")




        


