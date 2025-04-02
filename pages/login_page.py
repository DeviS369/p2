from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button") 
    ERROR_MESSAGE = (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]")
    def login(self, username, password):
        """Perform login action."""
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)
        time.sleep(3)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        time.sleep(4)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        time.sleep(4)
    def get_error_message(self):
        """Retrieve error message after failed login."""
        return self.driver.find_element(*self.ERROR_MESSAGE).text

    def is_logged_in(self):
        """Check if login was successful (by looking for dashboard element)."""
        return "dashboard" in self.driver.current_url
