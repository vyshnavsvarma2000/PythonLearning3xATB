#Integration Scenarios
# 1) Verify that create-booking -> patch request -> Verify that firstname is updated
# 2) Create a booking, Delete the booking with that id, Verify the GET request that it should not exist
# 3) GET an existing booking from GET all bookingid's , Update a booking with that id, Verify with GET request that it is updated
# 4) Create a booking and delete it
# 5) Invalid creation -  Enter a wrong payload or JSON
# 6) Trying to Update on a deleted id

import pytest
import allure
import requests

@allure.title("TC-04 CREATE A BOOKING, DELETE IT")
@allure.description("Create a booking and delete it")
@pytest.mark.integration
def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    payload = {
        "username":"admin",
        "password":"password123"
    }
    response = requests.post(url=url, headers=headers, json=payload)
    response_data = response.json()
    token = response_data["token"]
    return token

@allure.title("TC-04 CREATE A BOOKING, DELETE IT")
@allure.description("Create a booking and delete it")
@pytest.mark.integration

def create_booking():
    booking_url = "https://restful-booker.herokuapp.com/booking/"
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "TEST",
        "lastname": "S Varma",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-04-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=booking_url, headers=headers, json=payload)
    response_data = response.json()
    bookingid= response_data["bookingid"]
    return bookingid

@allure.title("TC-04 CREATE A BOOKING, DELETE IT")
@allure.description("Create a booking and delete it")
@pytest.mark.integration
def test_delete_booking():
    booking_url = "https://restful-booker.herokuapp.com/booking/"
    url = booking_url + str(create_booking)
    cookies = "token="+create_token()
    headers = {"Content-Type": "application/json","Cookie": cookies}
    response = requests.delete(url=url, headers=headers)
    assert response.status_code == 200


