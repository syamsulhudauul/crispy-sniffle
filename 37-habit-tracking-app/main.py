import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_request = {
    "token": "",
    "username": "syamsulhudauul",
    "aggreTermsOfService":"yes",
    "notMinor":"yes",
}

response = requests.post(pixela_endpoint,params=user_request)
print(response.text)