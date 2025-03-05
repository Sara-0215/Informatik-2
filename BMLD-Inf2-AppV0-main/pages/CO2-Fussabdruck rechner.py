import streamlit as st

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
st.markdown("### Berechnung für mehrere Transportmittel")
ausgewaehlte_transportmittel = st.multiselect("Wähle deine Transportmittel:", list(CO2_WERTE.keys()))

km_pro_tag_mehrere = {}
for t in ausgewaehlte_transportmittel:
    km_pro_tag_mehrere[t] = st.number_input(f"Wie viele Kilometer fährst du pro Tag mit {t}?", min_value=0.0, step=0.1, key=t)

def berechne_gesamt_co2(km_pro_tag_mehrere):
    """Berechnet den jährlichen CO₂-Ausstoß basierend auf mehreren Transportmitteln und deren täglicher Strecke."""
    gesamt_co2 = 0
    for t, km in km_pro_tag_mehrere.items():
        gesamt_co2 += (CO2_WERTE[t] * km * 365) / 1000  # Umrechnung in kg
    return round(gesamt_co2, 2)

if st.button("Gesamt CO₂ berechnen"):
    gesamt_ergebnis = berechne_gesamt_co2(km_pro_tag_mehrere)
    st.success(f"Dein jährlicher CO₂-Ausstoß mit den ausgewählten Transportmitteln beträgt **{gesamt_ergebnis} kg CO₂** pro Jahr.")

st.divider()  # Trennlinie

import pandas as pd

# Durchschnittlicher CO₂-Verbrauch eines Schweizers (in kg pro Jahr)
average_co2 = 3090

# Benutzer-Eingabe für CO₂-Verbrauch
user_co2 = st.number_input("Gib deinen jährlichen CO₂-Verbrauch in kg ein:", min_value=0.0, step=0.1)

# Daten für das Balkendiagramm
data = pd.DataFrame({
    "Kategorie": ["Durchschnittlicher Schweizer", "Dein Verbrauch"],
    "CO₂-Verbrauch (t/Jahr)": [average_co2, user_co2]
})

# Balkendiagramm anzeigen
st.bar_chart(data.set_index("Kategorie"), use_container_width=True) 

# Ergänztes Diagramm mit Plotly, dynamischen Farben und Beschriftung
def plot_dynamisches_co2_diagramm(user_co2, average_co2=3090):
    import plotly.express as px
    import pandas as pd

    # Daten vorbereiten
    data = pd.DataFrame({
        "Kategorie": ["Durchschnittlicher Schweizer 🇨🇭", "Dein Verbrauch 🌱"],
        "CO₂-Verbrauch (kg/Jahr)": [average_co2, user_co2]
    })

    # Dynamische Farben je nach Verbrauch
    farben = ['green' if wert < average_co2 else 'red' for wert in data["CO₂-Verbrauch (t/Jahr)"]]

    fig = px.bar(
        data, 
        x="Kategorie", 
        y="CO₂-Verbrauch (t/Jahr)", 
        color="Kategorie",
        color_discrete_sequence=farben,
        title="📊 Dein CO₂-Verbrauch im Vergleich zum Durchschnitt"
    )

    # Diagramm anzeigen
    st.plotly_chart(fig, use_container_width=True)

# Diagramm anzeigen wenn User-Eingabe vorhanden ist
if user_co2 > 0:
    plot_dynamisches_co2_diagramm(user_co2)
