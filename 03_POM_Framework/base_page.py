from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    """PARENT CLASS: Controls live browser interactions using Selenium."""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.base_url = "https://practicetestautomation.com"
        self._wait_timeout = 10  # Internal backing store variable

    # --- PROPERTY GETTER & SETTER GUARD FOR TIMEOUT ---
    @property
    def wait_timeout(self) -> int:
        """GETTER: Returns current implicit wait setting."""
        return self._wait_timeout

    @wait_timeout.setter
    def wait_timeout(self, seconds: int):
        """SETTER GUARD: Safely updates browser wait timeout."""
        if seconds <= 0:
            print(f"--> [GUARD TRIGGERED] Invalid timeout ({seconds}s). Setting safe default to 5s.")
            seconds = 5

        self._wait_timeout = seconds
        self.driver.implicitly_wait(seconds)  # Applies directly to active Chrome driver
        print(f"--> [SELENIUM] Applied implicit wait timeout: {seconds}s")

    # --- REUSABLE BASE ACTIONS ---
    def navigate_to(self, endpoint: str):
        """Launches the URL inside the active Chrome window."""
        full_url = f"{self.base_url}/{endpoint.strip('/')}"
        print(f"--> [SELENIUM] Navigating browser to: {full_url}")
        self.driver.get(full_url)