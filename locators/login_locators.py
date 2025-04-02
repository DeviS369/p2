from selenium.webdriver.common.by import By

class LoginLocators:
    USERNAME = (By.ID, "txtUsername")
    PASSWORD = (By.ID, "txtPassword")
    LOGIN_BUTTON = (By.ID, "btnLogin")
    ERROR_MESSAGE = (By.ID, "spanMessage")
