import streamlit as st
import pandas as pd

st.title("🌍 CO₂-Fussabdruck Daten")

# Sicherstellen, dass die Session-State Variable existiert
data_df = st.session_state["data_df"]
if 'data_df' not in st.session_state:
    st.session_state['data_df'] = pd.DataFrame(columns=["Transportmittel", "Kilometer pro Tag", "CO₂ (kg/Jahr)", "timestamp"])

data_df = st.session_state['data_df']

if data_df.empty:
    st.info('Keine CO₂-Daten vorhanden. Berechnen Sie Ihren CO₂-Fussabdruck auf der Startseite.')
    st.stop()

# Sortiere die Daten nach Zeitstempel absteigend
data_df = data_df.sort_values('timestamp', ascending=False)

# Zeige die Daten als Tabelle an
st.dataframe(data_df)
