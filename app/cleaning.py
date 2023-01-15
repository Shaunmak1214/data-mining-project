from re import S
import pandas as pd
import streamlit as st
import numpy as np

def app():
    st.title("Cleaning the datasets")

    st.write("First of all let's plot the nan values in the dataset")
    # display image 
    st.image('./nanvalues_plot.png')
    
    st.write("##### Since the dataset is quite large, we can't just drop the rows with nan values. So we'll have to impute the values. We'll be using the SimpleImputer to impute the values.")
    st.write("##### But just before we do that, for the columns Race, Gender, latitude and longitude, since they are columns that are very important, without them we can't really do much, we'll just drop the rows with nan values for these columns.")
    st.write("#### Dropping the rows with nan values")
    st.code('''p_df = p_df.dropna(subset=['Race', 'Gender', 'latitude', 'longitude'], inplace=False)''')
    
    st.write("#### Imputing the values")
    st.code('''imp = SimpleImputer(missing_values=np.nan, strategy='most_frequent')''')
    
    st.write("#### After imputing the values, we can see that there are no more nan values in the dataset")
    st.image('./after_imputing.png')
    st.write("*The data is then saved as a csv file and ready for exploration*")
 
    st.write(" ")
    st.markdown('''Made with ❤️ by **TDS3301 Group 2** ''')