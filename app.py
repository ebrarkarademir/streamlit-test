import streamlit as st
from dashboard import run as run_dashboard
from login import run as run_login
from admin import run as run_admin_panel
from model import run as run_model

st.set_page_config(layout='wide', page_title='HAKSAN YENİ MODEL')
print(st.session_state)
# Check if the user is logged in or not
if 'loggedin' not in st.session_state:
    st.session_state['loggedin'] = False

# If the user is not logged in, show the login form
if not st.session_state['loggedin']:
    run_login()
else:
    run_model()
