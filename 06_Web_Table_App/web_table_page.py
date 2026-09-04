import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from helpers import Helpers


class WebTablePage:
    # URL & Locators
    URL = "https://demoqa.com/webtables"
    SEARCH_BOX = (By.ID, "searchBox")
    ADD_BUTTON = (By.ID, "addNewRecordButton")

    # Registration Form Modal Locators
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    AGE = (By.ID, "age")
    SALARY = (By.ID, "salary")
    DEPARTMENT = (By.ID, "department")
    SUBMIT_BTN = (By.ID, "submit")

    # Table Content
    TABLE_BODY = (By.XPATH, "//tbody")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def navigate_to(self):
        """Navigates to the WebTables page."""
        print(f"\n--> [NAVIGATE] Opening URL: {self.URL}")
        self.driver.get(self.URL)
        time.sleep(2)

    def add_user(self, fname, lname, email, age, salary, dept):
        """Fills out and submits the registration form modal."""
        print(f"\n--> [ACTION] Clicking 'Add' button to open registration form...")
        Helpers.wait_and_click(self.driver, self.ADD_BUTTON)
        time.sleep(1)

        print(f"--> [FORM] Filling details for: {fname} {lname} ({email})")
        Helpers.wait_and_type(self.driver, self.FIRST_NAME, fname)
        time.sleep(1)
        Helpers.wait_and_type(self.driver, self.LAST_NAME, lname)
        time.sleep(1)
        Helpers.wait_and_type(self.driver, self.EMAIL, email)
        time.sleep(1)
        Helpers.wait_and_type(self.driver, self.AGE, age)
        time.sleep(1)
        Helpers.wait_and_type(self.driver, self.SALARY, salary)
        time.sleep(1)
        Helpers.wait_and_type(self.driver, self.DEPARTMENT, dept)
        time.sleep(1)

        print(f"--> [ACTION] Submitting form...")
        Helpers.wait_and_click(self.driver, self.SUBMIT_BTN)
        time.sleep(1)

    def search_text(self, text):
        """Types search query into the search box."""
        print(f"\n--> [SEARCH] Searching web table for query: '{text}'")
        Helpers.wait_and_type(self.driver, self.SEARCH_BOX, text)
        time.sleep(1)

    @property
    def get_table_data(self) -> str:
        """Fetches entire text content of the table body."""
        print("\n--> [READ] Fetching entire table text content...")
        return Helpers.wait_for_text(self.driver, self.TABLE_BODY)

    def get_row_details(self, row_index: int) -> list[str]:
        """Reads all column cell texts from a specific 1-based row index in <tbody>."""
        print(f"\n--> [READ] Extracting cell values specifically from Row {row_index}...")
        row_xpath = (By.XPATH, f"//tbody/tr[{row_index}]/td")
        cells = self.driver.find_elements(*row_xpath)
        row_data = [cell.text.strip() for cell in cells]
        print(f"--> [DATA] Row {row_index} cells extracted: {row_data}")
        return row_data