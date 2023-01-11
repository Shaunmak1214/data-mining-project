from re import S
import pandas as pd
import streamlit as st
import numpy as np

def app():
    st.title("What's interesting about this Laundry Shop?")
    st.write("**Prepared By** - *(Tee Eng Leong, 1191201404), (Anirban Bala Pranto, 1181202317)*")

    st.write("This application showcases the exploration and modelling of data obtained from a Laundry Shop. The application has been developed as part of a project for **Data Mining (TDS 3301)** class at **Multimedia University, Cyberjaya**")

    df1 = pd.read_csv('LaundryData_2021_T2.csv')

    st.write("The Dataset we're working with")
    #showing our initial dataframe here
    st.dataframe(df1)
    st.write('## Next Steps!')
    st.write("Please use the navigation bar to navigate between different parts of the project!")