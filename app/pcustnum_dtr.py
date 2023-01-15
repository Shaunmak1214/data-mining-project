from re import S
import pandas as pd
import streamlit as st
import numpy as np
import joblib

def app():
  st.subheader("Decision Tree Regression For Customer Numbers (Prediction)")
  st.write("The tree structure can be interpreted as a series of questions about the attributes of the data. The leaf nodes of the tree contain an output variable (e.g. a class label) which is used to make a prediction. The deeper the tree, the more complex the decisions and the fitter the model.")
  st.write("Thefore it explains why the use of this model is suitable for our data. The model is able to predict the number of customers in the laundry shop based on the weather, time and day of the week")
  
  st.subheader("Model Traning Results:")
  st.table(pd.DataFrame ({"Model": ["Decision Tree Regression"], "R2 Score": [0.80], "Mean Absolute Error": [4.607], "RMSE": [5.919]}))
  
  st.subheader("Making a prediction")
  st.write("The model is able to predict the number of customers in the laundry shop based on the weather, time and day of the week")

  with st.form(key='my_form'):
    day = st.selectbox('Day', ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    time = st.selectbox('Time', ['Morning', 'Afternoon', 'Evening', "Night"])
    weather = st.selectbox('Weather', ['Clear', 'Cloudy', 'Light rain shower', 'Mist', 'Moderate or heavy rain shower', 'Partly cloudy', 'Patchy light drizzle', 'Patchy rain possible'])

    submit_button = st.form_submit_button(label='Predict')
    
  if submit_button:
    model = joblib.load('./numcust_dtr_model.sav')
    test_row = pd.read_csv('./pcustnum_test_row.csv')
    day_col = 'Day_' + day
    time_col = 'Time_' + time
    weather_col = 'weather_' + weather
    test_row[day_col] = 1
    test_row[time_col] = 1
    test_row[weather_col] = 1
    prediction = model.predict(test_row)

    st.write("The number of customers in the laundry shop is predicted to be", prediction[0])
  
  st.subheader("Tuning of the model")
  st.image("./numcust_dtr_depth_vs_mae.png", width=700)
  st.write("The graph above shows the mean absolute error of the model as the depth of the tree increases.")