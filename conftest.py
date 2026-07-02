import pytest

@pytest.fixture()
def user_data():
    return {
        "name": "Bray",
        "job": "Software Engineer"
    }
