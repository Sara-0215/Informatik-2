import streamlit as st
import plotly.express as px

# Titel der App
st.title("🌍 CO₂-Fußabdruck Rechner")
st.write("Berechne deinen jährlichen CO₂-Ausstoß basierend auf deinem Transportmittel.")

st.divider()  # Trennlinie für bessere Struktur

# CO₂-Emissionen pro km für verschiedene Transportmittel
CO2_WERTE = {
    "Auto (Benzin)": 120,
    "Auto (Diesel)": 135,
    "Bus": 40,
    "Zug": 8,
    "Flugzeug": 250,
    "Fahrrad": 0,
    "Zu Fuß": 0
}

# Benutzer-Eingabe
st.markdown("### 🚗 Einzelne Transportmittel")
transportmittel = st.selectbox("Wähle dein Transportmittel:", list(CO2_WERTE.keys()), key="transportwahl_1")
km_pro_tag = st.number_input("Wie viele Kilometer fährst du pro Tag?", min_value=0.0, step=0.1)

def berechne_co2(transportmittel, km_pro_tag):
    if transportmittel not in CO2_WERTE:
        return None
    co2_pro_jahr = (CO2_WERTE[transportmittel] * km_pro_tag * 365) / 1000  # Umrechnung in kg
    return round(co2_pro_jahr, 2)

if st.button("CO₂ berechnen"):
    ergebnis = berechne_co2(transportmittel, km_pro_tag)
    if ergebnis is not None:
        color = "green" if ergebnis < 1000 else "red"
        st.markdown(f"<h4 style='color:{color}'>Dein jährlicher CO₂-Ausstoß mit {transportmittel} beträgt <b>{ergebnis} kg CO₂</b> pro Jahr.</h4>", unsafe_allow_html=True)
    else:
        st.error("Bitte wähle ein gültiges Transportmittel.")

st.divider()  # Trennlinie für bessere Struktur

# Mehrere Transportmittel vergleichen
st.markdown("### 🔄 Berechnung für mehrere Transportmittel")
co2_input = st.number_input("Gib deinen jährlichen CO₂-Verbrauch in kg ein:", min_value=0.0, step=1.0)
if st.button("Gesamt CO₂ berechnen"):
    color = "green" if co2_input < 5000 else "red"
    st.markdown(f"<h4 style='color:{color}'>Dein Gesamt-CO₂-Ausstoß beträgt <b>{co2_input} kg CO₂</b> pro Jahr.</h4>", unsafe_allow_html=True)

st.divider()  # Trennlinie

# Diagramm für CO₂-Vergleich
st.markdown("### 📊 CO₂-Emissionen im Vergleich")
def plot_co2_vergleich():
    labels = list(CO2_WERTE.keys())
    werte = [CO2_WERTE[t] * km_pro_tag * 365 / 1000 for t in labels]
    farben = ["green" if w < 1000 else "red" for w in werte]  # Grün für niedrige Werte, Rot für hohe

    fig = px.bar(x=labels, y=werte, title="CO₂-Ausstoß verschiedener Transportmittel",
                 labels={"x": "Transportmittel", "y": "CO₂-Ausstoß (kg/Jahr)"}, color=werte, color_continuous_scale=["green", "red"])
    st.plotly_chart(fig)

if km_pro_tag > 0:
    plot_co2_vergleich()



 


        


