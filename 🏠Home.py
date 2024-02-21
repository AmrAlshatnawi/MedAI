import streamlit as st
from functions import *

# set page icon and tab title
st.set_page_config(
        page_title="MedAI - Home",
        page_icon="🤖",
    )
# Make page content larger (zoom)
st.markdown("""<style>body {zoom: 1.4;  /* Adjust this value as needed */}</style>""", unsafe_allow_html=True)

# check if authenticated is in session state 
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# check if user is authenticated
if not st.session_state['authenticated']:
    authenticate()
# Show page if user is authenticated
if st.session_state['authenticated']:

    # page content starts here
    st.title("🤖 MedAI")

    # Welcome message
    st.markdown("""
        <div style="
            border: 1px solid #ffffff;
            border-radius: 20px;
            padding: 30px;
            margin: 30px 0;
            background-color: #ffffff;
            color: #000000;
            ">
            <h2 style="color: #000000;text-align: center;">🌟 Welcome to MedAI – Your Smart Health Companion! 🌟</h2>
            <p>Dive right into our <strong>AI-powered Medical Assistance Chat</strong> for instant insights and support on health queries. Or, explore our <strong>Dynamic Data Tools</strong> for a visual snapshot of vital health trends and data insights.</p>
            <p>
            Get started now and unlock smarter, data-driven health decisions today!
        </p>
        <p><b>Access our tools using the side navigation.</b> </p>
                        
        </div>
        """, unsafe_allow_html=True)