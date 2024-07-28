#Integration Scenarios
# 1) Verify that create-booking -> patch request -> Verify that firstname is updated
# 2) Create a booking, Delete the booking with that id, Verify the GET request that it should not exist
# 3) GET an existing0 booking from GET all bookingid's , Update a booking with that id, Verify with GET request that it is updated
# 4) Create a booking and delete it
# 5) Invalid creation -  Enter a wrong payload or JSON
# 6) Trying to Update on a deleted id

import pytest
import allure
import requests

@allure.title("TC-01 CREATE BOOKING , PARTIAL_ UPDATE IT AND VERIFY")
@allure.description("Verify that create-booking -> patch request -> Verify that firstname is updated")
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

@allure.title("TC-01 CREATE BOOKING , PARTIAL_ UPDATE IT AND VERIFY")
@allure.description("Verify that create-booking -> patch request -> Verify that firstname is updated")
@pytest.mark.integration
def create_booking():
    booking_url = "https://restful-booker.herokuapp.com/booking/"
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Vyshnav",
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
    bookingid = response_data["bookingid"]
    return bookingid
@allure.title("TC-01 CREATE BOOKING , PARTIAL_ UPDATE IT AND VERIFY")
@allure.description("Verify that create-booking -> patch request -> Verify that firstname is updated")
@pytest.mark.integration
def test_patch_request():
    base_url = "https://restful-booker.herokuapp.com/booking/"
    url = base_url+str(create_booking())
    cookies = "token="+create_token()
    headers = {"Content-Type": "application/json", "Cookie": cookies}
    payload = {
        "firstname": "Vishal",
        "lastname": "S Varma"
    }
    print(cookies)
    response = requests.patch(url=url, headers=headers, json=payload)
    print(response.json())
    return response
    assert response.status_code == 200
@allure.description("Verify that create-booking -> patch request -> Verify that firstname is updated")
@pytest.mark.integration
def test_get_booking():
    base_url = "https://restful-booker.herokuapp.com/booking/"
    url = base_url + str(create_booking())
    response = test_patch_request()
    response_data = response.json()
    assert response_data["firstname"] == "Vishal"
    assert response.status_code == 200

