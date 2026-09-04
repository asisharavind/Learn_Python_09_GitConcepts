from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from base_page import BasePage


class LoginPage(BasePage):
    """CHILD CLASS: Interacts with actual input boxes and buttons on the login page."""

    # Real HTML element locators from practicetestautomation.com
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_BUTTON = (By.ID, "submit")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_login_url(self):
        """Navigates Chrome to the login page."""
        self.navigate_to("practice-test-login/")

    def perform_login(self, username: str, secret_pass: str):
        """Finds text boxes using tuple unpacking (*), types credentials, and clicks Submit."""
        print(f"--> [SELENIUM] Entering username: {username}")
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

        print(f"--> [SELENIUM] Entering password...")
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(secret_pass)

        print(f"--> [SELENIUM] Clicking Submit button...")
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    @property
    def current_page_url(self) -> str:
        """GETTER: Returns active URL directly from Chrome."""
        return self.driver.current_url