from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from helpers import Helpers
import time

class HerokuApp:
    REMOVE_BUTTON = (By.XPATH, "//button[text()='Remove']")
    ENABLE_BUTTON = (By.XPATH, "//button[text()='Enable']")
    MESSAGE_TEXT = (By.ID, "message")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.base_url = "https://the-internet.herokuapp.com/dynamic_controls"

    def navigate_to(self, endpoint: str = ""):
        if endpoint:
            full_url = f"{self.base_url.rstrip('/')}/{endpoint.strip('/')}"
        else:
            full_url = self.base_url.rstrip('/')

        self.driver.get(full_url)
        time.sleep(2)

    def click_remove(self):
        Helpers.wait_and_click(self.driver, self.REMOVE_BUTTON)

    def click_enable(self):
        Helpers.wait_and_click(self.driver, self.ENABLE_BUTTON)

    @property
    def capture_text(self) -> str:
        """GETTER: Explicitly waits for the dynamic message to load, then returns text."""
        return Helpers.wait_for_text(self.driver, self.MESSAGE_TEXT)