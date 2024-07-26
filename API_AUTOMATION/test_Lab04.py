"""Request Module -> Module => Module contains a package or a
library containing functions that we can use repeatedly in our programs"""

"""
To Make HTTP Request- METHODS
Request- Module
# GET , POST, PUT , PATCH , DELETE , OPTIONS..
# WE CAN VERIFY THE URL, Cookies, Auth Verification with Pytest
"""
# GET REQUEST - Booking ID
# REQUEST (Client - Server)

# URL -> https://restful-booker.herokuapp.com/booking/
#Auth -> X
#Payload -> X
#Content-Type - or Header -> X
# Query Param? -> X
#Path Param -> Yes [Get the id 1]


# Response
# Body -> Verify -> using Assert
# Status Code -> Verify
# Time
# JSON Schema , XML Schema

import pytest
import allure
import requests

@allure.title("Test GET Request - RESTful Booker Project #1")
@allure.description('Verify that GET Request with ID Works')
@allure.tag("regression", "p0", "Smoke")
@allure.label("owner","Vyshnav S Varma")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url)
    print(response_data.json())
    assert response_data.status_code == 200

@allure.title("Test GET Request - RESTful Booker Project #2")
@allure.description('Verify that GET Request return Status 200')
@allure.tag("regression", "p0", "Smoke")
@allure.label("owner","Vyshnav S Varma")
@allure.testcase("TC#2")
@pytest.mark.smoke
def test_get_single_request_by_id2():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url)
    print(response_data.json())
    assert response_data.status_code == 200

@allure.title("Test GET Request - RESTful Booker Project #1")
@allure.description('Verify that GET Request with ID Works')
@allure.tag("regression", "p0", "Smoke")
@allure.label("owner","Vyshnav S Varma")
@allure.testcase("TC#3")
@pytest.mark.smoke
def test_get_single_request_by_id3():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url)
    print(response_data.json())
    assert response_data.status_code == 200















