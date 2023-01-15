import json
import numpy as np
from fastapi import FastAPI, File, UploadFile
from starlette.responses import HTMLResponse 
import re
import os
from fastapi.middleware.cors import CORSMiddleware
from io import BytesIO
from re import S
import pandas as pd
import numpy as np
import joblib

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/') #basic get view
def basic_view():
    return "Welcome to the Laundry Shop Prediction API"
  
@app.post('/pcustnum', response_class=HTMLResponse)
async def take_inp(day: str, time: str, weather: str):
    model = joblib.load('../numcust_dtr_model.sav')
    test_row = pd.read_csv('../pcustnum_test_row.csv')
    day_col = 'Day_' + day
    time_col = 'Time_' + time
    weather_col = 'weather_' + weather
    test_row[day_col] = 1
    test_row[time_col] = 1
    test_row[weather_col] = 1
    prediction = model.predict(test_row)

    return json.dumps({"Num of customers you can expect: ": prediction[0], }, indent=4)