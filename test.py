import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.pim_page import PIMPage
from data import TestData

def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(TestData.BASE_URL)
    return driver

@pytest.fixture
def driver():
    driver = setup_driver()
    yield driver
    driver.quit()

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
    assert login_page.is_logged_in(), "Login failed with valid credentials"

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.login(TestData.VALID_USERNAME, TestData.INVALID_PASSWORD)
    assert login_page.get_error_message() == TestData.INVALID_LOGIN_ERROR, "Invalid login error message not displayed"

def test_add_employee(driver):
    login_page = LoginPage(driver)
    login_page.login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
    pim_page = PIMPage(driver)
    pim_page.add_employee(TestData.NEW_EMPLOYEE)
    assert pim_page.is_employee_added(), "Employee addition failed"

def test_edit_employee(driver):
    login_page = LoginPage(driver)
    login_page.login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
    pim_page = PIMPage(driver)
    pim_page.edit_employee(TestData.EDIT_EMPLOYEE)
    assert pim_page.is_employee_edited(), "Employee edit failed"

def test_delete_employee(driver):
    login_page = LoginPage(driver)
    login_page.login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
    pim_page = PIMPage(driver)
    pim_page.delete_employee(TestData.DELETE_EMPLOYEE)
    assert pim_page.is_employee_deleted(), "Employee deletion failed"
