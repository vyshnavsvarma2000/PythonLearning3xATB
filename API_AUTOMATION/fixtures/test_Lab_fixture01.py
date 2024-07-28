import pytest
import allure

@allure.title("#TC-0 Smoke Test")
@allure.description("Verify that 2-2 = 0")
@pytest.mark.smoke
def test_sub0():
    assert 2 - 2 == 0

@allure.title("#TC-1 Regression  Test")
@allure.description("Verify that 3-3= 0")
@pytest.mark.regression
def test_sub1():
    assert 3 - 3 == 0
@allure.title("#TC-2 Smoke Test")
@allure.description("Verify that 4-4 = 0")
@pytest.mark.smoke
def test_sub2():
    assert 4 - 4 == 0
@allure.title("#TC-3 Smoke Test")
@allure.description("Verify that 5-5 = 0")
@pytest.mark.skip(reason="not working , skip")
def test_sub3():
    assert 5 - 5 == 0
@allure.title("#TC-4 Sanity Test")
@allure.description("Verify that 0-0 = 0")
@pytest.mark.sanity
def test_sub4():
    assert 0 - 0 == 0
