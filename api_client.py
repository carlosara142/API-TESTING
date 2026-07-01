import token

import requests

URL_BASE = "https://reqres.in/api" 

HEADERS = {
    "x-api-key": "free_user_3FgmAr0RrHxHSDZztVEDtpR4TfV",
}
creds = {
    "email": "eve.holt@reqres.in", 
    "password": "cityslicka"
}

# def get_users():
#     response = requests.get(f"{URL_BASE}/users", headers=HEADERS)

#     if response.status_code == 200:
#         print(f"codigo de respuesta: {response.status_code}")
#         print(response.json())
#     else:
#         print(f"Error: {response.status_code}")

# get_users()                         

def login_post():
    response = requests.post(f"{URL_BASE}/login", headers=HEADERS, json=creds)

    if response.status_code == 200:
        print(f"codigo de respuesta: {response.status_code}")
        success = response.json()
        print(success["token"])
    else:
        print(f"Error: {response.status_code}")

login_post()