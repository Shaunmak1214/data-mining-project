from re import S
import pandas as pd
import streamlit as st
import numpy as np
import joblib

def app():
  st.subheader("Clustering")
  st.write("Clustering is a method of unsupervised learning. It is used to group data points together based on their similarity. The goal of clustering is to find groups of similar data points.")
  
  st.subheader("Quick look at what we can cluster - Lat Lng")
  st.image('./lat_lng_scatter.png', width=600)
  
  st.write("#### KMeans Clustering - Lat Lng")
  st.write("Finding the optimal k value for KMeans Clustering")
  
  st.image('./long_lat_silhouette.png', width=900)
  st.write("The optimal k value is 3")
  
  st.subheader("KMeans Clustering, K=3")
  st.image('./long_lat_clustered.png', width=900)

  st.subheader("A try on clustering - Age Range X Rwi")
  st.image("./city_rwi_scatter.png", width=600)
  
  st.subheader("#### KMeans Clustering - Age Range X Rwi")
  st.write("Finding the optimal k value for KMeans Clustering")
  
  st.image('./ar_rwi_silhouette.png', width=900)
  st.write("The optimal k value is 3")
  
  st.subheader("KMeans Clustering, K=3")
  st.image('./age_range_rwi_clustered.png', width=900)
