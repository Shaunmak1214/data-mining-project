from re import S
import pandas as pd
import streamlit as st
import numpy as np
import joblib

def app():
  st.subheader("KNN - Wash Item")
  st.write("KNN is a non-parametric method used for classification and regression. In both cases, the input consists of the k closest training examples in the feature space. The output depends on whether k-NN is used for classification or regression:")
  
  st.subheader("Model Traning Results:")
  st.table(pd.DataFrame ({
      "Model": ["Naive Bayes"], 
      "Accuracy on traning set": [0.761], 
      "Accuracy on test set": [0.515], 
      "Precision Score": [0.6360759493670886],
      "Recall Score": [0.49385749385749383],
      "F1 Score": [0.5560165975103734],
    }))
  
  st.code("""
              precision    recall  f1-score   support

           0   0.468303  0.708978  0.564039       323
           1   0.609959  0.361179  0.453704       407

    accuracy                       0.515068       730
   macro avg   0.539131  0.535079  0.508872       730
weighted avg   0.547281  0.515068  0.502523       730

Class 0 ROC AUC OvR: 0.5587
Class 1 ROC AUC OvR: 0.5587
Average ROC AUC OvR: 0.5587
          """)
  
  st.subheader("Confusion Matrix:")
  st.image("./KNN_WI_CM.png", width=600)
  
  st.subheader("ROC Curve:")
  st.image("./WASHITEM_KNN_ROC.png", width=600)