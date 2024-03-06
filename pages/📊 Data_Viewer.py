import statsmodels.api as sm
import plotly.express as px
import pandas as pd
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
    st.title('📊 Data Viewer')
    uploaded_file = st.file_uploader("Please upload a csv file.")
    
    with st.sidebar:
        data_selection = st.selectbox("Demo Datasets", options = ["Please select a demo dataset", "hersdataset.csv"])
        if data_selection == "hersdataset.csv":
            uploaded_file = "hersdataset.csv"
    if uploaded_file is not None:
        
        def name_changer():
            option_change = st.selectbox(
            'Select variable to change name of.',
            list(df.columns), index = None, placeholder = "Choose an option.."
            )
          
            new_name = st.text_input("Enter new name of variable selected.")
            if st.button("Change") and option_change is not None and new_name is not None:
                df.rename(columns={option_change : new_name}, inplace = True)
                
            #amr 
            new_name = ""
            option_change = ""
        
        df = pd.read_csv(uploaded_file)


    #    if st.button("Press to change column header"):
    #        name_changer()


        numeric_df = df.select_dtypes(['float','int'])
        numeric_cols = numeric_df.columns

        text_df = df.select_dtypes(['object'])
        text_cols = text_df.columns
        with st.expander("Data Preview"):
            st.dataframe(df)
        list_of_cols = list(df.columns)
        option_x = st.selectbox(
        'Select x-variable for scatter plot.',
        numeric_cols, index = None, placeholder="Choose an option.."
        )

        option_y = st.selectbox(
        'Select y-variable for scatter plot.',
        numeric_cols, index = None, placeholder="Choose an option.."
        )

        option_cat = st.selectbox(
        'Select categorical variable for distribution.',
        text_cols, index = None, placeholder="Choose an option.."    
        )
        if option_x is not None and option_y is not None:
            
            st.write(f"Here is a scatter plot of {option_y} vs {option_x} in your given dataset:")
            fig = px.scatter(df,x = option_x, y = option_y, trendline = 'ols')
            st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        
        if option_cat is not None:
            st.write("Here is a histogram for the selected categorical variable:")
            fig_2 = px.histogram(df, x = option_cat)
            st.plotly_chart(fig_2,theme="streamlit", use_container_width=True)
        