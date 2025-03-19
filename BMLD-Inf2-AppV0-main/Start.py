# ====== Start Init Block ======
# This needs to copied on top of the entry point of the app (Start.py)
import streamlit as st
import pandas as pd
from utils.data_manager import DataManager
from utils.login_manager import LoginManager

st.title("Meine erste Streamlit App")

# initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="CO2-Fussabdruck")  # switch drive 

# initialize the login manager
login_manager = LoginManager(data_manager)
login_manager.login_register()

# load the data from the persistent storage into the session state
data_manager.load_user_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value = pd.DataFrame(), 
    parse_dates = ['timestamp']
)
#from utils.data_manager import DataManager

# !! WICHTIG: Eure Emails müssen in der App erscheinen!!

# Streamlit über den Text unten direkt in die App - cool!
"""
Diese App wurde von folgenden Personen entwickelt:
- Albina Krasniqi (krasnal2@students.zhaw.ch)
- Sara Cruz Silva (cruzssar@students.zhaw.ch)

Diese App ist das leere Gerüst für die App-Entwicklung im Modul Informatik 2 (BMLD/ZHAW)

"""

