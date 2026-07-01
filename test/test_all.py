from api_client import get_users, create_user, login_user


def test_get_users():
    response = get_users()
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert "data" in data
    assert len(data["data"]) > 0

def test_create_user():
    response = create_user(
        "Bray", 
        "Software Engineer")
    assert response.status_code == 201
    body = response.json()
    print(body)
    # assert "name" in body
    # assert "job" in body
    assert body["name"] == "Bray"
    assert body["job"] == "Software Engineer"

# def test_login_user():
#     response = login_user("eve.holt@reqres.in", "cityslicka")
#     assert response.status_code == 200
#     data = response.json()
#     assert "token" in data