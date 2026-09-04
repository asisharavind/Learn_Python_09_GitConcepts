from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
    """PARENT CLASS: Handles core browser interactions."""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.base_url = "https://www.saucedemo.com"
        self._wait_timeout = 10

    @property
    def wait_timeout(self) -> int:
        return self._wait_timeout

    @wait_timeout.setter
    def wait_timeout(self, seconds: int):
        if seconds <= 0:
            seconds = 5
        self._wait_timeout = seconds
        self.driver.implicitly_wait(seconds)

    def navigate_to(self,endpoint: str = ""):
        full_url = f"{self.base_url}/{endpoint.strip('/')}"
        self.driver.get(full_url)

    @property
    def current_url(self) -> str:
        return self.driver.current_url