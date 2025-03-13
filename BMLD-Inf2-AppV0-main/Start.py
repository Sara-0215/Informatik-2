import streamlit as st
import pandas as pd


# Assuming DataManager is defined in a module named data_manager_module
from .data_manager_module import DataManager

st.title("Meine erste Streamlit App")

# !! WICHTIG: Eure Emails müssen in der App erscheinen!!

# Streamlit über den Text unten direkt in die App - cool!
"""
Diese App wurde von folgenden Personen entwickelt:
- Albina Krasniqi (krasnal2@students.zhaw.ch)
- Sara Cruz Silva (cruzssar@students.zhaw.ch)

Diese App ist das leere Gerüst für die App-Entwicklung im Modul Informatik 2 (BMLD/ZHAW)

"""
# initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="App")  # switch drive 

# load the data from the persistent storage into the session state
data_manager.load_app_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value = pd.DataFrame(), 
    parse_dates = ['timestamp']
    )

