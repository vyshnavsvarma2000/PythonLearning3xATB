#Integration Scenarios
# 1) Verify that create-booking -> patch request -> Verify that firstname is updated

import pytest
import allure
import requests


@allure.title("TC-01 CREATE BOOKING, PARTIAL UPDATE IT AND VERIFY")
@allure.description("Verify that create-booking -> patch request -> Verify that firstname is updated")
@pytest.mark.integration
def test_create_and_patch_booking(create_booking, create_token):
    # Define URLs and headers
    base_url = "https://restful-booker.herokuapp.com/booking/"
    headers = {"Content-Type": "application/json"}

    # Create booking
    booking_url = base_url
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

    # Partial update booking
    patch_url = base_url + str(bookingid)
    cookies = {"token": create_token}
    patch_payload = {
        "firstname": "Vishal",
        "lastname": "S Varma"
    }
    patch_response = requests.patch(url=patch_url, headers=headers, cookies=cookies, json=patch_payload)
    assert patch_response.status_code == 200

    # Verify the update
    get_url = patch_url
    response = requests.get(url=get_url, headers=headers)
    response_data = response.json()
    assert response_data["firstname"] == "Vishal"
    print(response_data)
    assert response.status_code == 200


