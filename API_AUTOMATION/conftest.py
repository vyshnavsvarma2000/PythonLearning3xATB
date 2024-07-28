import pytest
import requests
@pytest.fixture()
def create_token():
    #token
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    payload = {
        "username":"admin",
        "password":"password123"
    }
    response = requests.post(url=url, headers=headers, json=payload)
    token = response.json()["token"]
    print(token)
    return token
@pytest.fixture()
def create_booking():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"
    url = base_url + base_path
    headers = {"Content-type": "application/json"}
    payload = {
        "firstname": "Mark",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-04-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=url, headers=headers, json=payload)
    response_data = response.json()
    bookingid = response_data["bookingid"]
    return bookingid
