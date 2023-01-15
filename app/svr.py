from re import S
import pandas as pd
import streamlit as st
import numpy as np
import joblib

def app():
  st.subheader("Support Vector Regression - Age Range")
  st.write("The Support Vector Regression model is a supervised learning model that is used for regression analysis. It is based on the concept of Support Vector Machines (SVM). The SVM algorithm is used to find a hyperplane in an N-dimensional space (N — the number of features) that distinctly classifies the data points. The hyperplane is chosen so that the distance between the nearest data points of both the classes is maximized. The figure below shows the hyperplane that separates the two classes. The SVM algorithm is used to find the optimal hyperplane that maximizes the margin between the two classes.")
  
  st.write(" ")
  st.subheader("Model Traning Results:")
  st.table(pd.DataFrame ({"Model": ["Support Vector Regressor"], "R2 Score": [0.004], "MSE": [141.080], "MAE": [10.110]}))

  st.write(" ")
  st.subheader("Tuning of the model:")
  
  st.image('./AgeRange_SVR_Gamma_vs_Mae.png')
  st.image('./AgeRange_SVR_Gamma_vs_Accuracy.png')
  st.image('./AgeRange_SVR_Gamma_vs_MSE.png')
  
  st.subheader("Support Vector Regression - Total Spent")
  
  st.write(" ")
  st.subheader("Model Traning Results:")
  st.table(pd.DataFrame ({"Model": ["Support Vector Regressor"], "R2 Score": [0.003], "MSE": [20.421], "MAE": [3.932]}))

  st.write(" ")
  st.subheader("Tuning of the model:")
  
  st.image('./TotalSpent_SVR_Gamma_vs_Mae.png')
  st.image('./TotalSpent_SVR_Gamma_vs_Accuracy.png')
  st.image('./TotalSpent_SVR_Gamma_vs_MSE.png')