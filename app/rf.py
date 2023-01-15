from re import S
import pandas as pd
import streamlit as st
import numpy as np
import joblib

def app():
  st.subheader("Random Forest - Wash Item")
  st.write("Random Forest is an ensemble learning method for classification, regression and other tasks, that operates by constructing a multitude of decision trees at training time and outputting the class that is the mode of the classes (classification) or mean/average prediction (regression) of the individual trees.")
  
  st.subheader("Model Traning Results:")
  st.table(pd.DataFrame ({
      "Model": ["Naive Bayes"], 
      "Accuracy on traning set": [0.659], 
      "Accuracy on test set": [0.547], 
      "Precision Score": [0.5641891891891891],
      "Recall Score": [0.8206388206388207],
      "F1 Score": [0.6686686686686687],
    }))
  
  st.code("""
              precision    recall  f1-score   support

0   0.471014  0.201238  0.281996       323
1   0.564189  0.820639  0.668669       407

accuracy                       0.546575       730
macro avg   0.517602  0.510939  0.475332       730
weighted avg   0.522963  0.546575  0.497579       730

Class 0 ROC AUC OvR: 0.5863
Class 1 ROC AUC OvR: 0.5863
Average ROC AUC OvR: 0.5863
          """)
  
  st.subheader("Confusion Matrix:")
  st.image("./RF_WI_CM.png", width=600)
  
  st.subheader("ROC Curve:")
  st.image("./WASHITEM_RF_ROC.png", width=600)
  
  st.subheader("Model Tuning:")
  st.write('Grid Search is used to find the best parameters for the model. The best parameters are:')
  st.table(pd.DataFrame ({"Model": ["Random Forest"], "n_estimators": [1000], "max_depth": [5]}))