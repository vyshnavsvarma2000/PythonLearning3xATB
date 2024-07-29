import pytest
import allure
import requests


# 6) Trying to Update on a deleted id

@allure.title("TC-06  UPDATE ON  A DELETED ID")
@allure.description("Trying to Update on a deleted id")
@pytest.mark.integration
def test_update_deleted_booking(create_token):
    booking_url = "https://restful-booker.herokuapp.com/booking/"
    headers = {"Content-Type": "application/json"}
    # step1 - create a booking
    payload = {
        "firstname": "Fake",
        "lastname": "User",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-04-01"
        },
        "additionalneeds": "Breakfast"
    }
    created_response = requests.post(url=booking_url, headers=headers, json=payload)
    assert created_response.status_code in [201, 200]
    created_response_data = created_response.json()
    assert created_response_data["bookingid"] is not None, "Unfortunately it is empty"
    bookingid = created_response_data["bookingid"]

    # step2 delete the booking
    delete_url = booking_url + str(bookingid)
    cookies = {"token": create_token}
    delete_response = requests.delete(url=delete_url, cookies=cookies)
    assert delete_response.status_code in [201, 200, 204], "Invalid status code"

    # step 3 verify that it is deleted
    get_response = requests.get(url=delete_url)
    assert get_response.status_code == 404
