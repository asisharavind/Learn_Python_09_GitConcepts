from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from base_page import BasePage
import time


class InventoryPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ADD_BACKPACK_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")

    # Locators for Cart
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def login_to_app(self, username: str = "standard_user", password: str = "secret_sauce"):
        self.navigate_to()
        time.sleep(1)
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        time.sleep(1)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        time.sleep(1)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        time.sleep(2)

    def add_bag_to_carts(self):
        self.driver.find_element(*self.ADD_BACKPACK_BTN).click()
        time.sleep(2)

    def go_to_cart(self):
        """Clicks the top-right shopping cart container."""
        self.driver.find_element(*self.CART_ICON).click()
        time.sleep(2)

    @property
    def item_in_cart_name(self) -> str:
        """GETTER: Reads the item title text displayed on the cart page."""
        return self.driver.find_element(*self.CART_ITEM_NAME).text