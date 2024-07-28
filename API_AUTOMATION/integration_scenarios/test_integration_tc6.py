import pytest
import allure
import requests

# 6) Trying to Update on a deleted id
@allure.title("TC-06  DELETE A DELETED ID")
@allure.description("Trying to Update on a deleted id")
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
@allure.title("TC-06  DELETE A DELETED ID")
@allure.description("Trying to Update on a deleted id")
@pytest.mark.integration
def test_delete_booking():
    booking_url = "https://restful-booker.herokuapp.com/booking/19/"
    cookies = "token="+create_token()
    headers = {"Content-Type": "application/json", "Cookie": cookies}
    response = requests.delete(url=booking_url, headers=headers)
    assert response.status_code == 404