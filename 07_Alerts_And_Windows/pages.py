from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AlertsPage:
    """Encapsulates locators and actions for https://the-internet.herokuapp.com/javascript_alerts"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.url = "https://the-internet.herokuapp.com/javascript_alerts"

        # Locators
        self.JS_ALERT_BTN = (By.XPATH, "//button[text()='Click for JS Alert']")
        self.JS_CONFIRM_BTN = (By.XPATH, "//button[text()='Click for JS Confirm']")
        self.JS_PROMPT_BTN = (By.XPATH, "//button[text()='Click for JS Prompt']")
        self.RESULT_TEXT = (By.ID, "result")

    def load(self):
        self.driver.get(self.url)

    def trigger_js_alert_and_accept(self):
        self.wait.until(EC.element_to_be_clickable(self.JS_ALERT_BTN)).click()
        alert = self.wait.until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
        return alert_text

    def trigger_js_confirm_and_dismiss(self):
        self.wait.until(EC.element_to_be_clickable(self.JS_CONFIRM_BTN)).click()
        alert = self.wait.until(EC.alert_is_present())
        alert_text = alert.text
        alert.dismiss()
        return alert_text

    def trigger_js_prompt_and_send_keys(self, input_text):
        self.wait.until(EC.element_to_be_clickable(self.JS_PROMPT_BTN)).click()
        alert = self.wait.until(EC.alert_is_present())
        alert_text = alert.text
        alert.send_keys(input_text)
        alert.accept()
        return alert_text

    def get_result_text(self):
        return self.driver.find_element(*self.RESULT_TEXT).text


class WindowsPage:
    """Encapsulates locators and actions for https://the-internet.herokuapp.com/windows"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.url = "https://the-internet.herokuapp.com/windows"

        # Locators
        self.CLICK_HERE_LINK = (By.LINK_TEXT, "Click Here")
        self.HEADING_TEXT = (By.TAG_NAME, "h3")

    def load(self):
        self.driver.get(self.url)

    def open_new_window_and_switch(self):
        parent_handle = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable(self.CLICK_HERE_LINK)).click()

        # Wait for tab to open and switch context
        self.wait.until(EC.number_of_windows_to_be(2))
        all_handles = self.driver.window_handles
        child_handle = [h for h in all_handles if h != parent_handle][0]

        self.driver.switch_to.window(child_handle)
        return parent_handle, child_handle

    def get_heading_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.HEADING_TEXT)).text

    def close_current_tab_and_switch_to(self, target_handle):
        self.driver.close()
        self.driver.switch_to.window(target_handle)