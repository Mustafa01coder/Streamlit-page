import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns

## Creating the nagivation Bar
st.set_page_config(page_title="Company Data Portal", layout="wide")

## sidebar for navigation
st.sidebar.title('Navigation Pane')
page = st.sidebar.radio('Go to', ['Home', 'Data Upload and View', 'Graphical Insights'])

if 'df' not in st.session_state:
    st.session_state.df = None

## Home page Creating
if page == 'Home':
    st.title('Company Data Portal')
    st.subheader('Company Details')
    
    ## text inputs for company details
    company_name = st.text_input('Enter Company Name')
    user_name = st.text_input('Enter Your Name')

    if st.button('Save Details'):
        st.success('Details Saved Successfully')
        st.write('Company Name:', company_name)
        st.write('User Name:', user_name)

## Data Upload and View Page
elif page == 'Data Upload and View':
    st.title('Data Upload and Veiw')
    uploaded_file = st.file_uploader('upload CSV file', type=['csv'])
    if uploaded_file is not None:
        df= pd.read_csv(uploaded_file)
        st.session_state.df =df
        st.success('Data Uploaded Successfully')
        st.subheader('Data Pewview')
        st.dataframe(df)


## Graphical Insights Page
elif page == 'Graphical Insights':
    st.title('Graphical Insights')

    df = st.session_state.df

    if df is not None:

        st.subheader(' Dataset Overview')
        st.dataframe(df.head())

        # Convert numeric columns safely
        df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
        df['Profit'] = pd.to_numeric(df['Profit'], errors='coerce')

        # ---------------- GRAPH 1 ----------------
        st.subheader(' Total Sales by Category')

        sales_by_category = df.groupby('Category')['Sales'].sum()

        st.bar_chart(sales_by_category)

        # ---------------- GRAPH 2 ----------------
        st.subheader('Total Profit by Region')

        profit_by_region = df.groupby('Region')['Profit'].sum()

        st.bar_chart(profit_by_region)

    else:
        st.warning('Please upload a dataset first in the Data Upload section.')





