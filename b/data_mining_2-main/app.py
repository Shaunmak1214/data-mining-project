from re import S
import pandas as pd
import streamlit as st
import numpy as np

import home
import eda
import FeatureSelection
import SVR
import DTR
import NB
import RFC
import KNN
import NeuralNet
import playground
import Model1

st.set_page_config(page_title='What\'s interesting about a Laundry Shop?', page_icon=None, layout="wide",
                    initial_sidebar_state="auto", menu_items=None)
PAGES = {
    "Home" : home,
    "Exploratory Data Analyis" : eda,
    "Feature Selection": FeatureSelection,
    "Models - Regression (SVR) ": SVR,
    "Models - Regression (DecisionTree)": DTR,
    "Models - Classification (NB)" : NB,
    "Models - Classification (RFC)" : RFC,
    "Models - Classification (KNN)" : KNN,
    "Models - Classification (NN)" : NeuralNet,
    "Live Prediction Playground (Baskets)" : playground,
    "Live Prediction Playground (Age)" : Model1
}
st.sidebar.title('The Data Mining Process')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()