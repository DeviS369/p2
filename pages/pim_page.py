from selenium.webdriver.common.by import By

class PIMPage:
    def __init__(self, driver):
        self.driver = driver

    PIM_MENU = (By.XPATH, '''//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a''') 
    ADD_BUTTON = (By.XPATH, '''//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button''')
    FIRST_NAME_FIELD = (By.NAME, "firstName")
    LAST_NAME_FIELD = (By.NAME, "lastName")
    SAVE_BUTTON = (By.XPATH, '''//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]''')
    SUCCESS_MESSAGE = (By.XPATH, "//p[contains(text(), 'Successfully')]")

    def navigate_to_pim(self):
        """Navigate to PIM module."""
        self.driver.find_element(*self.PIM_MENU).click()

    def add_employee(self, employee_data):
        """Add a new employee."""
        self.navigate_to_pim()
        self.driver.find_element(*self.ADD_BUTTON).click()
        self.driver.find_element(*self.FIRST_NAME_FIELD).send_keys(employee_data["first_name"])
        self.driver.find_element(*self.LAST_NAME_FIELD).send_keys(employee_data["last_name"])
        self.driver.find_element(*self.SAVE_BUTTON).click()

    def is_employee_added(self):
        """Verify if employee was added successfully."""
        return self.driver.find_element(*self.SUCCESS_MESSAGE).is_displayed()

    def edit_employee(self, employee_data):
        """Edit an existing employee (Implementation Needed)"""
        pass

    def is_employee_edited(self):
        """Verify if employee was edited successfully (Implementation Needed)"""
        pass

    def delete_employee(self, employee_data):
        """Delete an existing employee (Implementation Needed)"""
        pass

    def is_employee_deleted(self):
        """Verify if employee was deleted successfully (Implementation Needed)"""
        pass
