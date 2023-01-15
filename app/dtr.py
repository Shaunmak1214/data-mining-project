from re import S
import pandas as pd
import streamlit as st
import numpy as np
import joblib

def app():
  st.subheader("Decision Tree Regressor - Age Range")
  st.write("Decision Tree is a supervised learning algorithm that can be used for both classification and regression problems, but mostly it is preferred for solving Classification problems. The goal is to create a model that predicts the value of a target variable by learning simple decision rules inferred from the data features.")
  
  st.write(" ")
  st.subheader("Model Traning Results:")
  st.table(pd.DataFrame ({"Model": ["Decision Tree Regressor"], "R2 Score": [-5.75], "MSE": [166.48], "MAE": [10.87]}))

  st.write(" ")
  st.subheader("Tuning of the model:")
  
  st.image('./ar_dtr_depth_vs_mae.png')