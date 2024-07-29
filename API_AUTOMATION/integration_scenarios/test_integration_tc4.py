#Integration Scenarios
# 4) Create a booking and delete it

import pytest
import requests
import allure


@allure.title("TC-04 Create a Booking and Delete It")
@allure.description("Create a booking and delete it, then verify the deletion")
@pytest.mark.integration
def test_create_booking_delete(create_token):
    base_url = "https://restful-booker.herokuapp.com/booking/"
    headers = {"Content-Type": "application/json"}

    # Payload for creating a booking
    payload = {
    "firstname": "Test",
    "lastname": "Varma",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2024-01-01",
        "checkout": "2024-04-01"
    },
    "additionalneeds": "Breakfast"
}

    # Step 1: Create a booking
    create_response = requests.post(url=base_url, headers=headers, json=payload)
    assert create_response.status_code in [201, 200], "Failed to create booking"

    create_response_data = create_response.json()
    print("Create Booking Response:", create_response_data)

    # Verify the booking creation
    assert 'bookingid' in create_response_data, "Booking ID is missing in the response"
    assert create_response_data["booking"]["firstname"] == "Test", "First name is incorrect"
    assert create_response_data["booking"]["lastname"] == "Varma", "Last name is incorrect"

    bookingid = create_response_data["bookingid"]

    # Step 2: Delete the booking
    delete_url = base_url + str(bookingid)
    cookies = {"token": create_token}
    delete_response = requests.delete(url=delete_url, cookies=cookies)
    assert delete_response.status_code in [200, 201], "Failed to delete booking"

    # Step 3: Verify the booking deletion
    get_response = requests.get(url=delete_url)
    assert get_response.status_code == 404, "Booking was not deleted successfully"
