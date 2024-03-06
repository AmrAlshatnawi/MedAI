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

################ no need to authenticate this page ################

# # check if authenticated is in session state 
# if 'authenticated' not in st.session_state:
#     st.session_state['authenticated'] = False
# # check if user is authenticated
# if not st.session_state['authenticated']:
#     authenticate()
# # Show page if user is authenticated
# if st.session_state['authenticated']: 
    # #page content start here 
    #title of the page



st.title(':bar_chart: :blue[Data Viewer]')
#uploader that takes file as input from user
st.subheader("Upload your own csv file for investigation or choose a demo dataset from the sidebar to explore.")
uploaded_file = st.file_uploader("Please upload a csv file here.")

#functionality within sidebar to select a demo dataset
with st.sidebar:
    data_selection = st.selectbox("Demo Datasets", options = ["hersdataset.csv"], index = None, placeholder = "Please select a demo dataset")
    if data_selection == "hersdataset.csv":
        uploaded_file = "hersdataset.csv"
#verification to make sure there is a file uploaded
if uploaded_file is not None:
#trying to add functionality to change column header names for the future that is commented out for now    
#   def name_changer():
#       option_change = st.selectbox(
#       'Select variable to change name of.',
#       list(df.columns), index = None, placeholder = "Choose an option.."
#       )
#      
#       new_name = st.text_input("Enter new name of variable selected.")
#       if st.button("Change") and option_change is not None and new_name is not None:
#           df.rename(columns={option_change : new_name}, inplace = True)
            
    #using pandas to read the uploaded csv and load it into a DataFrame
    df = pd.read_csv(uploaded_file)


#   if st.button("Press to change column header"):
#       name_changer()

    #selecting the variables/columns that contain a numerical value
    numeric_df = df.select_dtypes(['float','int'])
    numeric_cols = numeric_df.columns

    #selecting the variables/columns that contain a text value or are categorical
    text_df = df.select_dtypes(['object'])
    text_cols = text_df.columns
    #displaying a preview of the data that can be expanded and minimized
    with st.expander("Data Preview"):
        st.dataframe(df)
    
    #header that displays to select variables
    st.header(":blue[Variable Selection]")
    
    #dropdown to select x variable for plotly scatterplot
    option_x = st.selectbox(
    'Select x-variable for scatter plot.',
    numeric_cols, index = None, placeholder="Choose an option.."
    )

    #dropdown to select y variable for plotly scatterplot
    option_y = st.selectbox(
    'Select y-variable for scatter plot.',
    numeric_cols, index = None, placeholder="Choose an option.."
    )

    #dropdown to select a variable among the categorical variables for histogram
    option_cat = st.selectbox(
    'Select categorical variable for distribution.',
    text_cols, index = None, placeholder="Choose an option.."    
    )
    #scatterplot is only displayed if user selects required variables
    if option_x is not None and option_y is not None:
        
        #subheader that displays to indicate where the scatterplot is
        st.subheader(f":blue[Scatter plot of {option_y} vs {option_x} in your given dataset]", divider = 'rainbow')
        #plotly scatter plot that takes the df and variables selected above as input and renders a trendline using statsmodels
        fig = px.scatter(df,x = option_x, y = option_y, trendline = 'ols')
        #st.plotly_chart displays the scatterplot in streamlit
        st.plotly_chart(fig, theme=None, use_container_width=True)
    
    #histogram is only displayed if user selects required variable
    if option_cat is not None:
        #subheader that displays to indicate where the histogram is
        st.subheader(f":blue[Histogram showing the distribution of {option_cat}]", divider = 'rainbow')
        #plotly histogram that takes the df and user selected categorical variable to create a histogram
        fig_2 = px.histogram(df, x = option_cat)
        #st.plotly_chart displays the histogram in streamlit
        st.plotly_chart(fig_2,theme=None, use_container_width=True)
        