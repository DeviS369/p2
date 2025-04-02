import pytest
from pages.login_page import LoginPage
from test_data.test_data import TestData

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
    assert login_page.is_logged_in(), "Login failed with valid credentials"

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.login(TestData.VALID_USERNAME, TestData.INVALID_PASSWORD)
    assert login_page.get_error_message() == TestData.INVALID_LOGIN_ERROR, "Invalid login error message not displayed"
