#Integration Scenarios
# 5) Invalid creation -  Enter a wrong payload or JSON


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
    assert response.status_code == 500
    print(response)
