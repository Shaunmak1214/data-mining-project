from re import S
import pandas as pd
import streamlit as st
import numpy as np
import pickle
import random


@st.cache
def get_mapl():
    print("Loading Mapl")
    return pickle.load((open('mapl.pkl', 'rb')))

@st.cache
def get_lmap():
    print("Loading Lmap")
    return pickle.load((open('lmap.pkl', 'rb')))

@st.cache
def load_model():
    print("Loading model")
    return pickle.load(open('Age_KNN_model.h5', 'rb'))


def app():
    st.title("Model Playground")
    st.write("Please enter your own values in the fields and see the predictions below.")
    st.write("Note : the values of Date, Time, Longitude and Latitude are choses at random everytime you enter a new value. This is because these fields have way too many unique values which makes it really hard to list.")
    loaded_model = load_model()
    mapl = get_mapl()
    lmap = get_lmap()
    data = [{
        "Date":"19/10/2015",
        "Time":"20:17:50",
        "Race":"malay",
        "Gender":"male",
        "Body_Size":"moderate",
        "With_Kids":"yes",
        "Kids_Category":"young",
        "Basket_Size":"big",
        "Basket_colour":"red",
        "Attire":"casual",
        "Shirt_Colour":"blue",
        "shirt_type":"short_sleeve",
        "Pants_Colour":"black",
        "pants_type":"short",
        "Wash_Item":"clothes",
        "Washer_No":"3",
        "Dryer_No":"10",
        "Spectacles":"no",
        "latitude":"2.9123164195153914",
        "longitude":"101.65794781008772",
        "Num_of_Baskets": "1.0"
    }]
    for key in data[0]:
        if(key != "Date" and key != "Time" and key != "latitude" and key != "longitude"):
            st.write("Options", mapl[key].keys())
            data[0][key] = st.text_input(key, data[0][key])
    
    pred_data = {}
    date_list = list(mapl['Date'].keys())
    time_list = list(mapl['Time'].keys())
    lat_list = list(mapl['latitude'].keys())
    lon_list = list(mapl['longitude'].keys())
    rid = random.randint(0, len(date_list) - 1)
    tid = random.randint(0, len(time_list) - 1)
    laid = random.randint(0, len(lat_list) - 1)
    loid = random.randint(0, len(lon_list) - 1)
    for key in data[0]:
        pred_data[key] = mapl[key][data[0][key]]
    pred_data['Date'] = mapl['Date'][date_list[rid]]
    pred_data['Time'] = mapl['Time'][time_list[tid]]
    pred_data['latitude'] = mapl['latitude'][lat_list[laid]]
    pred_data['longitude'] = mapl['longitude'][lon_list[loid]]
    age_range = {}
    for i in range(0,10):
        ran = "[" + str(i*10) + "," + str(i*10+10) + "]"
        age_range[i] = ran

    st.write("Date : ", date_list[rid])
    st.write("Time : ", time_list[tid])
    st.write("Latitude : ", lat_list[laid])
    st.write("Longitude : ", lon_list[laid])
    df = pd.DataFrame.from_records(data=[pred_data])
    pred = loaded_model.predict(df)
    st.write("## Prediction")
    st.write("Binned_Age_Range : ", age_range[pred[0]])