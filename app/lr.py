from re import S
import pandas as pd
import streamlit as st
import numpy as np
import joblib

def app():
  st.subheader("Linear Regression - Age Range")
  st.write(" ")
  st.write("Proposing a linear regression is hard when the data is not linear. We can see that the data is not linear in the plot below.")
  st.image("./lr_scatter_non_linear.png")
  
  st.subheader("Model Traning Results:")
  st.table(pd.DataFrame ({"Model": ["Linear Regression"], "Mean Absolute Error": [10.11], "MSE": [140.48], "Intercept": [21.283461574981608]}))
  
  st.write(" ")
  st.write("As shown above, the model training results is not good enough. The mean absolute error is 10.11 and the MSE is 140.48. The intercept is 21.")