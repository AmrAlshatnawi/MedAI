import pandas as pd
import numpy as np
import streamlit as st
from functions import *

# set page icon and tab title
st.set_page_config(
        page_title="MedAI - Data",
        page_icon="📊",
        layout = 'wide'
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
    uploaded_file = st.file_uploader("Please upload a csv file.")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        numeric_df = df.select_dtypes(['float','int'])
        numeric_cols = numeric_df.columns

        text_df = df.select_dtypes(['object'])
        text_cols = text_df.columns

        with st.expander("Data Preview"):
            st.dataframe(df)
        list_of_cols = list(df.columns)
        option_x = st.selectbox(
        'Select x-variable',
        numeric_cols)

        option_y = st.selectbox(
        'Select y-variable',
        numeric_cols)
        
        st.write(f'You selected: {option_y} against {option_x}')