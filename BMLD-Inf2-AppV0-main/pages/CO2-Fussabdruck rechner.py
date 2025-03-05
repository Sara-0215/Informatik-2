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
    "Zu Fuß": 0, 
    "E-Bus": 50,
    "Tram": 30
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


import pandas as pd

# Durchschnittlicher CO₂-Verbrauch eines Schweizers (in kg pro Jahr)
average_co2 = 3090 

# Benutzer-Eingabe für CO₂-Verbrauch
user_co2 = st.number_input("Gib deinen jährlichen CO₂-Verbrauch für Transport in Tonnen ein:", min_value=0.0, step=0.1)

# Aufteilung des Nutzer-Verbrauchs auf verschiedene Transportmittel
car_co2 = st.number_input("CO₂-Verbrauch durch Auto (t/Jahr):", min_value=0.0, step=0.1)
bus_co2 = st.number_input("CO₂-Verbrauch durch Bus (t/Jahr):", min_value=0.0, step=0.1)
train_co2 = st.number_input("CO₂-Verbrauch durch Zug (t/Jahr):", min_value=0.0, step=0.1)
plane_co2 = st.number_input("CO₂-Verbrauch durch Flugzeug (t/Jahr):", min_value=0.0, step=0.1)

# Summe des Nutzerverbrauchs
user_total_co2 = car_co2 + bus_co2 + train_co2 + plane_co2

# Farbe bestimmen (grün, wenn weniger als Durchschnitt, sonst rot)
bar_color = "green" if user_total_co2 < average_co2 else "red"

# Daten für das Balkendiagramm
data = pd.DataFrame({
    "Kategorie": ["Durchschnittlicher Schweizer", "Dein Verbrauch"],
    "CO₂-Verbrauch (t/Jahr)": [average_co2, user_total_co2]
})

# Balkendiagramm anzeigen mit gestapeltem Balken für den Nutzer
st.bar_chart(data.set_index("Kategorie"), use_container_width=True)

# Zusätzliche Erklärung
st.write("### Detaillierte Aufschlüsselung deines Verbrauchs:")
st.write(f"Auto: {car_co2} t/Jahr")
st.write(f"Bus: {bus_co2} t/Jahr")
st.write(f"Zug: {train_co2} t/Jahr")
st.write(f"Flugzeug: {plane_co2} t/Jahr")

# Hinweis auf Farbinterpretation
st.markdown(f"Dein Balken ist **{bar_color}**, weil du {'weniger' if user_total_co2 < average_co2 else 'mehr'} CO₂ als der Durchschnitt verbrauchst.")
