import pytest
import allure
import requests

@allure.title("TC-02 CREATE BOOKING , DELETE  IT AND VERIFY")
@allure.description("Create a booking, Delete the booking with that id, Verify the GET request that it should not exist")
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

@allure.title("TC-02 CREATE BOOKING , DELETE  IT AND VERIFY")
@allure.description("Create a booking, Delete the booking with that id, Verify the GET request that it should not exist")
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

@allure.title("TC-02 CREATE BOOKING , DELETE  IT AND VERIFY")
@allure.description("Create a booking, Delete the booking with that id, Verify the GET request that it should not exist")
@pytest.mark.integration
def test_delete_booking():
    base_url = "https://restful-booker.herokuapp.com/booking/"
    url = base_url+ str(create_booking())
    cookies = "token="+create_token()
    headers = {"Content-Type":"application/json", "Cookie":cookies}
    response = requests.delete(url=url, headers=headers)
    assert response.status_code == 200

@allure.description("Create a booking, Delete the booking with that id, Verify the GET request that it should not exist")
@pytest.mark.integration
def test_get_booking_deleted():
    base_url = "https://restful-booker.herokuapp.com/booking/"
    url = base_url+str(create_booking())
    response = requests.get(url=url)
    assert  response.status_code == 404