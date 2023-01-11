from re import S
import pandas as pd
import streamlit as st
import numpy as np

def app():
    st.write("# Decision Tree Regression")
    st.write("When there are complicated relationships between the features and the output variables, decision trees come in handy. they perform better in comparison to other methods when there are missing features, a mix of categorical and numerical features, or a large variance in the scale of features.")

    st.write("The graph below is the regplot of Decision Tree Regression for Age_Range.")
    st.image('DTR.png')
    
    st.write("Two error metrics have been used for evaluating and reporting the performance of Decision Tree Regression")
    a_file = open("DTR.txt")
    lines = a_file.readlines()
    for line in lines:
        st.write(line)
    st.write('\n')
    
    st.write("The graph below shown us the value of MAE when the max_depth increases")
    st.image('depth_vs_mae.png')