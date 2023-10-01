import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "syamsulhudauul"
SECRET = "gIC8lwTwkY"
user_request = {
    "token": SECRET,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

response = requests.post(pixela_endpoint,params=user_request)
print(response.text)

GRAPH_ID = "graph1"
graph_enpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cyling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}
header = {"X-USER-TOKEN":SECRET}
response = requests.get(graph_enpoint,params=graph_config,headers=header)
print(response.text)

# post action
DATETIME = datetime.now().strftime("%Y%m%d")
pixel_creation_enpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data = {
 "date" : DATETIME,
 "quantity": "9.74",
}
response = requests.post(pixel_creation_enpoint,params=pixel_data,headers=header)
print(response.text)

# put action
pixel_update_enpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATETIME}"
new_pixel_data = {
    "quantity": "10",
}
response = requests.put(pixel_update_enpoint,params=new_pixel_data,headers=header)
print(response.text)

# delete action
pixel_delete_enpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATETIME}"
response = requests.delete(pixel_delete_enpoint,headers=header)
print(response.text)