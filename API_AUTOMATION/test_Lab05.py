import pytest
import allure
import requests

@allure.title("TC#1  Create Booking CRUD Positive")
@allure.description("TC#1 - Verify the Create Booking")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    # To make a request - POST
    # URL
    # Method - POST
    # Headers - content-type = Application/JSON
    # Payload/Data/Body-> Dictionary/JSON
    #No Auth
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    url = base_url + base_path
    headers = {"Content-type":"application/json"}
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
    #Response Body Verification
    #Headers
    #Status Code
    #JSON Schema Validation
    #Time Response
    assert response.status_code == 200
    assert(response_data["bookingid"] is not None)
    assert(response_data["bookingid"] > 0)
    assert type(response_data["bookingid"] == int)
    firstname = response_data["booking"]["firstname"]
    assert type(firstname) is str
    lastname = response_data["booking"]["lastname"]
    assert type(lastname) is str
    assert response_data["booking"]["bookingdates"]["checkin"] is not None
    totalprice = response_data["booking"]["totalprice"]
    depositpaid = response_data["booking"]["depositpaid"]
    assert totalprice == 111
    assert depositpaid == True

@allure.title("TC#2  Create Booking CRUD Positive")
@allure.description("TC#2 - Verify that Booking is not created with {} data")
@pytest.mark.crud
def test_create_booking_negative_tc2():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    url = base_url + base_path
    headers = {"Content-type": "application/json"}
    payload = {}
    response = requests.post(url=url, headers=headers, json=payload)
    print(type(url))
    print(type(headers))
    print(type(payload))

    #Assertions
    assert response.status_code == 500

@allure.title(" TC#3  Create Booking CRUD Negative")
@allure.description("TC#3 - Verify the Booking with totalprice as a string value")
@pytest.mark.crud
def test_create_booking_negative_tc3():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    url = base_url + base_path
    headers = {"Content-type": "application/json"}
    payload = {
        "firstname": "Mark",
        "lastname": "Brown",
        "totalprice": "vyshnav",
        "depositpaid": "true",
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-04-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=url, headers=headers, json=payload)
    response_data = response.json()
    totalprice = response_data["booking"]["totalprice"]

    #Assertions
    assert response.status_code == 201

