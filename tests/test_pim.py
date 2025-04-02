import pytest
from pages.login_page import LoginPage
from pages.pim_page import PIMPage
from test_data.test_data import TestData

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
