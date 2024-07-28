#PUT
# URL
# PATH PARAM - Booking id
# Token for authentication
# Payload
# 1) create token , 2) create booking , 3) create the testfunction for put request

import pytest
import allure
import requests
def test_put_request_positive(create_token, create_booking):
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking)
    PUT_URL = base_url + base_path
    cookie = "token="+ create_token
    headers = {
        "Content-type": "application/json",
        "Cookie":cookie
    }
    payload = {
        "firstname": "Vyshnav",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-04-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.put(url=PUT_URL, headers=headers, json=payload)
    response_data = response.json()
    print(response_data)
    #Assertions
    assert response.status_code == 200
    assert response_data["firstname"] == "Vyshnav"

def test_delete(create_booking, create_token):
    base_url = "https://restful-booker.herokuapp.com/booking/"
    bookingid = create_booking
    DELETE_URL = base_url + str(bookingid)
    cookie = "token=" + create_token
    headers = {
        "Content-type": "application/json",
        "Cookie": cookie
    }
    print(headers)
    response = requests.delete(url=DELETE_URL,headers=headers)
