from re import S
import pandas as pd
import streamlit as st
import numpy as np
import joblib

def app():
  st.subheader("Naive Bayes - Wash Item")
  st.write("Naive bayes is used for classification problems. It is based on Bayes Theorem and assumes that the presence of a particular feature in a class is unrelated to the presence of any other feature.")
  
  st.subheader("Model Traning Results:")
  st.table(pd.DataFrame ({
      "Model": ["Naive Bayes"], 
      "Accuracy on traning set": [0.556], 
      "Accuracy on test set": [0.560], 
      "Precision Score": [0.6360759493670886],
      "Recall Score": [0.49385749385749383],
      "F1 Score": [0.5560165975103734],
    }))
  
  st.code("""
                        precision    recall  f1-score     support
0              0.502415  0.643963  0.564450  323.000000
1              0.636076  0.493857  0.556017  407.000000
accuracy       0.560274  0.560274  0.560274    0.560274
macro avg      0.569246  0.568910  0.560234  730.000000
weighted avg   0.576936  0.560274  0.559748  730.000000
Class 0 ROC AUC OvR: 0.5869
Class 1 ROC AUC OvR: 0.5869
Average ROC AUC OvR: 0.5869
          """)
  
  st.subheader("Confusion Matrix:")
  st.image("./NB_WI_CM.png", width=600)
  
  st.subheader("ROC Curve:")
  st.image("./WASHITEM_NB_ROC.png", width=600)