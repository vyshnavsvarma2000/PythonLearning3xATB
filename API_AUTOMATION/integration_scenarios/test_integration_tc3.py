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

@allure.title("TC-03 GET ALL BOOKING, GET SINGLE ID, UPDATEIT , VERIFY USING GET")
@allure.description("GET an existing booking from GET all bookingid's , Update a booking with that id, Verify with GET request that it is updated")
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
@allure.title("TC-03 GET ALL BOOKING, GET SINGLE ID, UPDATEIT , VERIFY USING GET")
@allure.description("GET an existing booking from GET all bookingid's , Update a booking with that id, Verify with GET request that it is updated")
@pytest.mark.integration
def test_get_all_booking_id():
    url = "https://restful-booker.herokuapp.com/booking/"
    response = requests.get(url=url)
    response_data = response.json()
    assert response.status_code == 200
@allure.title("TC-03 GET ALL BOOKING, GET SINGLE ID, UPDATEIT , VERIFY USING GET")
@allure.description("GET an existing booking from GET all bookingid's , Update a booking with that id, Verify with GET request that it is updated")
@pytest.mark.integration
def test_get_single_booking_id():
    url = "https://restful-booker.herokuapp.com/booking/19/"
    response = requests.get(url=url)
    response_data = response.json()
    assert response.status_code == 200
    assert response_data["bookingid"] == 19

@allure.title("TC-03 GET ALL BOOKING, GET SINGLE ID, UPDATEIT , VERIFY USING GET")
@allure.description("GET an existing booking from GET all bookingid's , Update a booking with that id, Verify with GET request that it is updated")
@pytest.mark.integration
def test_put_single_booking():
    cookies = "token="+create_token()
    url = "https://restful-booker.herokuapp.com/booking/19/"
    payload = {'firstname': 'Mammooty', 'lastname': 'K', 'totalprice': 111, 'depositpaid': True, 'bookingdates': {'checkin': '2018-01-01', 'checkout': '2019-01-01'}, 'additionalneeds': 'Breakfast'}
    headers = {"Content-Type":"application/json", "Cookie":cookies}
    response = requests.put(url=url, headers=headers, json=payload)
    response_data = response.json()
    assert response_data["firstname"] == "Mammooty"
    assert response.status_code == 200
@allure.description("GET an existing booking from GET all bookingid's , Update a booking with that id, Verify with GET request that it is updated")
@pytest.mark.integration
def test_get_single_booking_id():
    url = "https://restful-booker.herokuapp.com/booking/19/"
    response = requests.get(url=url)
    response_data = response.json()
    assert response_data["firstname"] == "Mammooty"
    assert response.status_code == 200
    print(response_data)


