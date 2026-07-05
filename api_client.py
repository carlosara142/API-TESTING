import requests

URL_BASE = "https://reqres.in/api" 

HEADERS = {
    "x-api-key": "free_user_3FgmAr0RrHxHSDZztVEDtpR4TfV",
}
creds = {
    "email": "eve.holt@reqres.in", 
    "password": "cityslicka"
}
def get_users():
    return requests.get(f"{URL_BASE}/users", headers=HEADERS)

def get_one_user(user_id):
    return requests.get(f"{URL_BASE}/users/{user_id}", headers=HEADERS)

def create_user(name , job):
    data = {
        "name": name,
         "job": job
    }
    return requests.post(f"{URL_BASE}/users", headers=HEADERS, json=data)

#PUT = actualizar todo. PATCH = actualizar parcialmente.
def update_user(name, job,user_id):
    data = {
        "name": name,
        "job": job
    }
    return requests.put(f"{URL_BASE}/users/{user_id}", headers=HEADERS, json=data)

def delete_user(user_id):
    return requests.delete(f"{URL_BASE}/users/{user_id}", headers=HEADERS)


def login_user(email, password):
    data = {
        "email": email,
        "password": password
    }
    return requests.post(f"{URL_BASE}/login", headers=HEADERS, json=data)



# def get_users():
#     response = requests.get(f"{URL_BASE}/users", headers=HEADERS)

#     if response.status_code == 200:
#         print(f"codigo de respuesta: {response.status_code}")
#         print(response.json())
#     else:
#         print(f"Error: {response.status_code}")

# get_users()                         

# def login_post():
#     response = requests.post(f"{URL_BASE}/login", headers=HEADERS, json=creds)

#     if response.status_code == 200:
#         print(f"codigo de respuesta: {response.status_code}")
#         success = response.json()
#         print(success["token"])
#     else:
#         print(f"Error: {response.status_code}")

# login_post()