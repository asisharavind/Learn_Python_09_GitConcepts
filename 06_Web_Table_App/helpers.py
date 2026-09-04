from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Helpers:
    @staticmethod
    def wait_and_click(driver: WebDriver, locator: tuple, timeout: int = 10):
        wait = WebDriverWait(driver, timeout)
        element = wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @staticmethod
    def wait_and_type(driver: WebDriver, locator: tuple, text: str, timeout: int = 10):
        wait = WebDriverWait(driver, timeout)
        element = wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    @staticmethod
    def wait_for_text(driver: WebDriver, locator: tuple, timeout: int = 10) -> str:
        wait = WebDriverWait(driver, timeout)
        element = wait.until(EC.visibility_of_element_located(locator))
        return element.text