import pytest

@pytest.fixture()
def create_token():
    return "abc"

@pytest.fixture()
def create_booking():
    return 123

def test_booking_token(create_token, create_booking):
    print("Token is",create_token)
    print("Booking id  is",create_booking)
