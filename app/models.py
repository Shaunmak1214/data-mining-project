from re import S
import pandas as pd
import streamlit as st
import numpy as np
import joblib
import pcustnum_dtr
import lr
import svr
import dtr
import nb
import rf
import knn
import svm
import ensemble
import clustering

def app():
    st.title("Models")
    
    menu = ["Decision Tree Regression For Customer Numbers (Prediction)",
      "Linear Regression",
      "Support Vector Regression",
      "Decision Tree Regression",
      "Naive Bayes",
      "Random Forest",
      "KNN",
      "SVM",
      "Ensemble",
      "Clustering"]
    choice = st.sidebar.selectbox("Models Menu", menu)


    if choice == 'Decision Tree Regression For Customer Numbers (Prediction)':
      pcustnum_dtr.app()
    
    if choice == 'Linear Regression':
      lr.app()
    
    if choice == 'Support Vector Regression':
      svr.app()
    
    if choice == 'Decision Tree Regression':
      dtr.app()
      
    if choice == 'Naive Bayes':
      nb.app()
    
    if choice == 'Random Forest':
      rf.app()
      
    if choice == 'KNN':
      knn.app()
      
    if choice == 'SVM':
      svm.app()
      
    if choice == 'Ensemble':
      ensemble.app()
      
    if choice == 'Clustering':
      clustering.app()

    st.write(" ")
    st.markdown('''Made with ❤️ by **TDS3301 Group 2** ''')