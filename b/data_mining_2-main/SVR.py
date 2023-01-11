from re import S
import pandas as pd
import streamlit as st
import numpy as np

def app():
    st.write("# Support Vector Regression")
    st.write("SVR can be used to tackle the same problems as linear regression solves. Unlike linear regression, however, SVR allows you to model non-linear connections between variables and allows you to tune hyperparameters to change the model's robustness.")

    st.write("The graph below is the regplot of Support Vector Regression for Age_Range.")
    st.image('SVR.png')
    
    st.write("Two error metrics have been used for evaluating and reporting the performance of Support Vector Regression")
    a_file = open("SVR.txt")
    lines = a_file.readlines()
    for line in lines:
        st.write(line)
    st.write('\n')
    
    st.write("The graph below shown us the value of MAE when the gamma increases")
    st.image('gamma_vs_mae.png')
    
    st.write("The graph below shown us the value of MAE when the C increases")
    st.image('c_vs_mae.png')
    
    st.write("The graph below shown us the value of MAE when the degree increases")
    st.image('degree_vs_mae.png')
