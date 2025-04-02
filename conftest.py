import pytest
from selenium import webdriver
from data import TestData

@pytest.fixture
def driver():
    """Fixture to setup and teardown Selenium WebDriver."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(TestData.BASE_URL)
    yield driver
    driver.quit()
