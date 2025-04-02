class TestData:
    BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    # Login Credentials
    VALID_USERNAME = "Admin"
    VALID_PASSWORD = "admin123"
    INVALID_PASSWORD = "wrongpassword"

    # Expected Error Messages
    INVALID_LOGIN_ERROR = "Invalid credentials"

    # Employee Data
    NEW_EMPLOYEE = {"first_name": "John", "last_name": "Doe", "employee_id": "12345"}
    EDIT_EMPLOYEE = {"employee_id": "12345", "first_name": "Johnny"}
    DELETE_EMPLOYEE = {"employee_id": "12345"}
