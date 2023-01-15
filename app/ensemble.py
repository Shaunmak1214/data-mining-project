from re import S
import pandas as pd
import streamlit as st
import numpy as np
import joblib

def app():
  st.subheader("Ensemble - Wash Item")
  st.write("Ensemble learning is a machine learning paradigm where multiple models, such as classifiers or experts, are strategically generated and combined to solve a particular computational intelligence problem. Ensemble methods are used in a wide variety of application areas, such as classification, regression, and control.")
  
  st.subheader("1. Voting Classifier:")
  
  st.write("#### Model Architecture:")
  st.table(pd.DataFrame ({
      "Model": ["LogisticRegression", "KNeighborsClassifier", "RandomForestClassifier", "Voting Classifier"],
    }))
  
  st.write("##### Model Traning Results:")
  st.table(pd.DataFrame ({
      "Model": ["Naive Bayes"], 
      "Accuracy on traning set": [ 0.825], 
      "Accuracy on test set": [0.559], 
      "Precision Score": [0.5869120654396728],
      "Recall Score": [0.7051597051597052],
      "F1 Score": [0.6406249999999999],
    }))
  
  st.code("""
              precision    recall  f1-score   support

           0   0.502075  0.374613  0.429078       323
           1   0.586912  0.705160  0.640625       407

    accuracy                       0.558904       730
   macro avg   0.544493  0.539886  0.534852       730
weighted avg   0.549374  0.558904  0.547023       730
          """)
  
  st.subheader("2. Stacked Classifier:")
  
  st.write("#### Model Architecture:")
  st.table(pd.DataFrame ({
      "Model": ["LogisticRegression", "KNeighborsClassifier", "CART", "SVM", "Naive Bayes", "Stacked Classifier"],
    }))
  
  st.write("#### Model Traning Result:")
  st.image("./stacked-boxplot.png", width=900)