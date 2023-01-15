from re import S
import pandas as pd
import streamlit as st
import numpy as np

import landing
import ext_datasets
import cleaning
import eda
import fs
import models
# import playground
# import Model1

def renderFooter ():
  st.write(" ")
  st.markdown('''Made with ❤️ by **TDS3301 Group 30** ''')

st.set_page_config(page_title='Laundry Data Mining?', page_icon=None, layout="wide",
                    initial_sidebar_state="auto", menu_items=None)
PAGES = {
    "Overview" : landing,
    "Data Cleaning": cleaning,
    "External_Datasets": ext_datasets,
    "Exploratory Data Analyis" : eda,
    "Feature Selection": fs,
    "Models": models,
    # "Live Prediction Playground (Baskets)" : playground,
    # "Live Prediction Playground (Age)" : Model1
}
st.sidebar.title('Interactive Data Mining')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()