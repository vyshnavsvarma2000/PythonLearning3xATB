#Integration Scenarios
# 3) GET an existing booking from GET all bookingid's , Update a booking with that id, Verify with GET request that it is updated

import pytest
import allure
import requests


@allure.title("TC-03 GET ALL BOOKING, GET SINGLE ID, UPDATEIT , VERIFY USING GET")
@allure.description("GET an existing booking from GET all bookingid's , Update a booking with that id, Verify with GET request that it is updated")
@pytest.mark.integration
def test_get_update_verify_booking(create_token):
    base_url = "https://restful-booker.herokuapp.com/booking/"
    headers = {"Content-Type":"application/json"}

    #step1- GET ALL Booking ids

    all_bookings_url = base_url
    response = requests.get(url=all_bookings_url)
    assert response.status_code == 200
    all_bookings = response.json()
    # Ensure there are bookings available
    assert len(all_bookings) > 0, "No bookings found"
    #Extracting the 1st booking id
    bookingid = all_bookings[0]["bookingid"]

    #Step2 - Update the booking
    update_url = base_url + str(bookingid)
    cookies = {"token": create_token}
    payload =  {
        "firstname": "UpdatedName",
        "lastname": "UpdatedLastName"
    }
    update_response = requests.patch(url=update_url, headers=headers, cookies=cookies, json=payload)
    assert update_response.status_code == 200

    # Step 3: Verify the update
    get_response = requests.get(url=update_url)
    assert get_response.status_code == 200
    get_response_data = get_response.json()

    assert get_response_data["firstname"] == "UpdatedName", "First Name was not updated"
    assert get_response_data["lastname"] == "UpdatedLastName", "Last Name was not Updated"






