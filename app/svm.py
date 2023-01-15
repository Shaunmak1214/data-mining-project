from re import S
import pandas as pd
import streamlit as st
import numpy as np
import joblib

def app():
  st.subheader("SVM - Wash Item")
  st.write("SVM is a supervised machine learning algorithm which can be used for both classification or regression challenges. However, it is mostly used in classification problems.")
  
  st.subheader("Model Traning Results:")
  st.table(pd.DataFrame ({
      "Model": ["Naive Bayes"], 
      "Accuracy on traning set": [ 1.000], 
      "Accuracy on test set": [0.558], 
      "Precision Score": [0.5575342465753425],
      "Recall Score": [1.0],
      "F1 Score": [0.7159190853122251],
    }))
  
  st.code("""
              precision    recall  f1-score   support

0   0.000000  0.000000  0.000000       323
1   0.557534  1.000000  0.715919       407

accuracy                       0.557534       730
macro avg   0.278767  0.500000  0.357960       730
weighted avg   0.310844  0.557534  0.399149       730

Class 0 ROC AUC OvR: 0.5100
Class 1 ROC AUC OvR: 0.5063
Average ROC AUC OvR: 0.5082
          """)
  
  st.subheader("ROC Curve:")
  st.image("./WASHITEM_SVC_1_ROC.png", width=600)