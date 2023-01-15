from re import S
import pandas as pd
import streamlit as st
import numpy as np

def app():
    st.title("Introducing more datasets!")
    
    merged_dataset = pd.read_csv('./dataset_w_weather&rwi&city.csv')

    st.write("We have also explored other datasets to see if we can find any interesting insights from them. The datasets we have explored are:")
    st.write("##### 1. [**Weather Information**](https://www.worldweatheronline.com/weather-api/)")
    st.write('Introduces us to the weather information of the area where the customer is located. We have used the weather information to see if there is any correlation between the weather and the number of customers.')
    st.write('The respective sample can be interpreted as follows:')
    st.table(pd.DataFrame(merged_dataset['weather'].value_counts()))
    st.markdown(" ")
    st.write("##### 2. [**RWI (Relative Wealth Index) - Meta**](https://data.humdata.org/dataset/relative-wealth-index)")
    st.write('Provides us to the relative wealth index of the area where the customer is located. We have used the relative wealth index to see if there is any correlation between the relative wealth index and the Total Spent RM.')
    st.write('The respective sample can be interpreted as follows:')
    st.table(pd.DataFrame(merged_dataset['rwi'].head(10)))
    st.markdown(" ")
    st.write("##### 3. [**Addresses (Google Maps API)**](https://developers.google.com/maps/documentation)")
    st.write('This dataset introduces us to the addresses of the customers. We have used the addresses to group customers by state and provinces.')
    st.write('The respective sample can be interpreted as follows:')
    st.table(pd.DataFrame(merged_dataset['city'].value_counts()))

    st.write(" ")
    st.markdown('''Made with ❤️ by **TDS3301 Group 30** ''')