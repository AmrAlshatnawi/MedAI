import streamlit as st
from functions import *

# set page icon and tab title
st.set_page_config(
        page_title="MedAI - Data",
        page_icon="📊",
    )
# Make page content larger (zoom)
st.markdown("""<style>body {zoom: 1.5;  /* Adjust this value as needed */}</style>""", unsafe_allow_html=True)
# check if authenticated is in session state 
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False
# check if user is authenticated
if not st.session_state['authenticated']:
    authenticate()
# Show page if user is authenticated
if st.session_state['authenticated']: 
    # #page content start here 
    st.write("Page is still under development.")