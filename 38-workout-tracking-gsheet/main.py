import requests 
import os
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path
import json

# load env
dotenv_path = Path('.env')
load_dotenv()

NUT_APP_ID = os.getenv("NUT_APP_ID")
NUT_API_KEY = os.getenv("NUT_API_KEY")
NUT_TRACK_API_URL = "https://trackapi.nutritionix.com" 
NUT_EXEC_ENDPOINT = NUT_TRACK_API_URL+"/v2/natural/exercise"
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT") #https://api.sheety.co/****/myWorkouts/workouts
SHEETY_BASIC_AUTH = os.getenv("SHEETY_BASIC_AUTH")

raw_data = input("Tell me which exercise you did: ")
# print(raw_data)

headers = {
    "x-app-id":NUT_APP_ID,
    "x-app-key":NUT_API_KEY,
    "x-remote-user-id":"0",
}

req = {
    "query":raw_data,
    "gender": "male",
    "weight_kg" : 80,
    "height_cm":166,
    "age":28
}

resp = requests.post(NUT_EXEC_ENDPOINT,headers=headers,data=req)
# print("exec:",resp.json())
data = resp.json()["exercises"][0]
duration = data["duration_min"]
nf_calories = data["nf_calories"]
execise = data["user_input"]

# get data
resp = requests.get(SHEETY_ENDPOINT)
# print("s_data:",resp.json())

# add row
s_header = {
    "content-type":"application/json",
    "authorization":SHEETY_BASIC_AUTH,
}
body = {
    "workout":{
        "date":datetime.now().strftime("%d/%m/%Y"),
        "time":datetime.now().strftime("%I:%M:%S %p"),
        "exercise":execise.title(),
        "duration":duration,
        "calories":nf_calories,
    }
}
json_data = json.dumps(body)
#print("ready_to_add:",json_data)
resp = requests.post(SHEETY_ENDPOINT,data=json_data,headers=s_header)
print("success add row: ",resp.json())