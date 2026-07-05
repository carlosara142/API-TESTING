from api_client import delete_user, get_users, create_user, login_user, update_user, delete_user, get_one_user
from conftest import user_data


# def test_get_users():
#     response = get_users()
#     assert response.status_code == 200
#     data = response.json()
#     print(data)
#     assert "data" in data
#     assert len(data["data"]) > 0

# #@pytest.mark.parametrize("name , job", [user_data])
# def test_create_user(user_data):
#     response = create_user(
#         user_data["name"], 
#         user_data["job"]
#     )
   
#     assert response.status_code == 201
#     body = response.json()
#     print(body)
#     assert body["name"] == "Bray"
#     assert body["job"] == "Software Engineer"

# def update_user(user_data):
#     response = update_user(
#         user_data["name"], 
#         user_data["job"]
#     )
# def test_update_user( ):
#     response = update_user("bray updated","Software Engineer updated",2)
#     assert response.status_code == 200
#     body = response.json()
#     print(body)
    
# def test_delete_user():
#     response = delete_user(1)
#     assert response.status_code == 204
#     print(response.status_code)

def test_get_one_user():
    response = get_one_user(1)
    assert response.status_code == 200
    body = response.json()
    print(body)
    
# def test_login_user():
#     response = login_user("eve.holt@reqres.in", "cityslicka")
#     assert response.status_code == 200
#     data = response.json()
#     assert "token" in data