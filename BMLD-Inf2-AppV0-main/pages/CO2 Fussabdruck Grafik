import streamlit as st
import pandas as pd

# Titel der Unterseite
st.title("🌍 CO₂-Fußabdruck Verlauf")

# Sicherstellen, dass die Daten im Session State existieren
if 'co2_data_df' not in st.session_state:
    st.session_state['co2_data_df'] = pd.DataFrame(columns=['timestamp', 'co2_emission'])

data_df = st.session_state['co2_data_df']
if data_df.empty:
    st.info('Keine CO₂-Daten vorhanden. Berechnen Sie Ihren Fußabdruck auf der Startseite.')
    st.stop()

# Verlauf des CO₂-Ausstoßes anzeigen
st.line_chart(data=data_df.set_index('timestamp')['co2_emission'], use_container_width=True)
st.caption('Jährlicher CO₂-Ausstoß über Zeit (kg)')