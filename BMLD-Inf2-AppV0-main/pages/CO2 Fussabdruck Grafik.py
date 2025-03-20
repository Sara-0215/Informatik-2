import streamlit as st
import pandas as pd

# Titel der Unterseite
st.title("🌍 CO₂-Fussabdruck Verlauf")

# Sicherstellen, dass die Daten im Session State existieren
if 'data_df' not in st.session_state:
    st.session_state['data_df'] = pd.DataFrame(columns=['co2_emission'])

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine CO₂-Daten vorhanden. Berechnen Sie Ihren Fussabdruck auf der Startseite.')
    st.stop()

# Verlauf des CO₂-Ausstoßes anzeigen
st.line_chart(data_df['co2_emission'], use_container_width=True)
st.caption('Jährlicher CO₂-Ausstoss über Zeit (kg)')