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
@allure.title("TC-05 CREATE A BOOKING WITH INVALID JSON")
@allure.description("Enter a wrong payload or JSON")
@pytest.mark.integration
def test_create_booking():
    booking_url = "https://restful-booker.herokuapp.com/booking/"
    headers = {"Content-Type": "application/json"}
    payload = {}
    response = requests.post(url=booking_url, headers=headers, json=payload)
    assert response.status_code !=200
    print(response)
