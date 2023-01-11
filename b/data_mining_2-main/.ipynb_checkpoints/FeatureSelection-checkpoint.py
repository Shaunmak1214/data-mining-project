import imp
from re import S
import pandas as pd
import streamlit as st
import numpy as np

def app():
    st.write("# Feature Selection")
    st.write("There are 2 types of feature selection techniques we have been used in this project.")
    
    st.write("## What are the top features that can be found with Boruta?")
    
    st.write("Boruta is an algorithm for feature selection. It functions as a wrapper algorithm for the Random Forest algorithm. When a data collection with multiple variables is provided for model creation, this technique becomes extremely important. The top 10 features are listed in the charts below.")
    st.image('Baskets_Boruta.png')
    st.image('Age_Boruta.png')
    
    st.write("## What are the top features that can be found with RFE?")
    
    st.write("Recursive Feature Elimination (RFE) is a wrapper-type feature selection algorithm. This means that in the core of the technique, a different machine learning algorithm is given and used, which is wrapped by RFE and used to help choose features. Filter-based feature selections, on the other hand, score each feature and select the features with the highest (or lowest) score. The top 10 features are listed in the charts below.")
    st.image('Baskets_RFE.png')
    st.image('Age_RFE.png')