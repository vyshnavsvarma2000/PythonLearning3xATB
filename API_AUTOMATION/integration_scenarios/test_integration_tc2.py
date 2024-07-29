import pytest
import allure
import requests

@allure.title("TC-02 CREATE BOOKING, DELETE IT AND VERIFY")
@allure.description("Create a booking, Delete the booking with that ID, Verify with a GET request that it should not exist")
@pytest.mark.integration
def test_create_booking_delete_verify(create_token):
    base_url = "https://restful-booker.herokuapp.com/booking/"
    headers = {"Content-Type": "application/json"}

    # Create a booking
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

    # Delete the booking
    delete_url = base_url + str(bookingid)
    cookies = {"token": create_token}
    delete_response = requests.delete(url=delete_url, cookies=cookies)
    assert delete_response.status_code == 201  # The response should be 201 Created on successful deletion

    # Verify the delete operation
    get_response = requests.get(url=delete_url)
    assert get_response.status_code == 404  # The response should be 404 Not Found
