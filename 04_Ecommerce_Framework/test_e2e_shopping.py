import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from inventory_page import InventoryPage

@pytest.fixture
def driver():
    chrome_options = Options()
    
        # 1. Use Guest Mode (Disables password saving/leak checks without triggering corporate extension policies)
    chrome_options.add_argument("--guest")

    # 2. Disable standard UI popups & info bars
    chrome_options.add_argument("--disable-save-password-bubble")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")

    # 3. Suppress internal password settings
    chrome_options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        },
    )

    # 4. Launch driver
    print("\n--> [SETUP] Launching Chrome Browser...")
    browser = webdriver.Chrome(options=chrome_options)
    browser.maximize_window()
    yield browser

    print("--> [TEARDOWN] Closing Chrome Browser...")
    browser.quit()

def test_successful_login_to_saucedemo(driver):
    invPage = InventoryPage(driver)
    invPage.wait_timeout = 10
    invPage.login_to_app()

    assert "inventory" in invPage.current_url


def test_add_bag_to_cart(driver):
    invPage = InventoryPage(driver)
    invPage.wait_timeout = 10

    # 1. Log in to dashboard
    invPage.login_to_app()

    # 2. Add backpack to cart
    invPage.add_bag_to_carts()

    # 3. Navigate to Cart page
    invPage.go_to_cart()

    # 4. Assert item is on cart page
    assert "cart.html" in invPage.current_url
    assert invPage.item_in_cart_name == "Sauce Labs Backpack"