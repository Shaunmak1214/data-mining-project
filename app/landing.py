from re import S
import pandas as pd
import streamlit as st
import numpy as np

def app():
    st.title("Laundry Data Mining")
    st.write("This demo explains and showcases the exploration and modelling of data done from the laundry shop dataset provided.")

    dataset = pd.read_csv('./dataset.csv')
    
    st.write("#### A quick look at the dataset")
    st.dataframe(dataset)
    st.write("The dataset contains",len(dataset), "rows and", len(dataset.columns), "columns")
    
    st.write("#### Unique values in each column")
    st.write(dataset.nunique())

    st.write("#### Now let's look at the data types of each column")
    st.write(dataset.dtypes)
    
    st.write("#### How about null/nan values?")
    st.write(dataset.isnull().sum())
    st.write("As you can see, there are quite a number null values in the dataset, head to the Cleaning page to see how we handle them!")
    
    st.write(" ")
    st.markdown('''Made with ❤️ by **TDS3301 Group 2** ''')