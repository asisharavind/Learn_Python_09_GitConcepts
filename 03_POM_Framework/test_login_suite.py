import pytest
from selenium import webdriver
from login_page import LoginPage


# --- PYTEST FIXTURE (Live Chrome Launcher) ---
@pytest.fixture
def driver1():
    """SETUP: Opens a live Chrome browser window before each test, closes it after."""
    print("\n--> [SETUP] Launching Chrome Browser...")
    browser = webdriver.Chrome()
    browser.maximize_window()

    yield browser  # Hands control over to the executing test case

    print("--> [TEARDOWN] Closing Chrome Browser...")
    browser.quit()


# --- TEST CASES ---

def test_successful_login_validation(driver1):
    """TC1: Opens real Chrome, sets timeout via property setter, logs in, and verifies URL redirect."""
    login_pg = LoginPage(driver1)
    
    # Using Property Setter assignment syntax
    login_pg.wait_timeout = 10  
    
    login_pg.open_login_url()

    # Live UI Action
    login_pg.perform_login("student", "Password123")

    # Property Getter used inside assertion
    assert "logged-in-successfully" in login_pg.current_page_url


def test_invalid_login_validation(driver1):
    """TC2: Opens real Chrome, tries invalid password, verifies URL stays on login page."""
    login_pg = LoginPage(driver1)
    login_pg.open_login_url()

    # Live UI Action
    login_pg.perform_login("student", "WrongPassword")

    # Property Getter used inside assertion
    assert "practice-test-login" in login_pg.current_page_url


def test_timeout_setter_guard(driver1):
    """TC3: Validates setter guard fallback when assigning a negative wait timeout."""
    login_pg = LoginPage(driver1)

    # Attempting invalid assignment -> Setter guard forces value to 5s
    login_pg.wait_timeout = -15  

    # Property Getter assertion confirms corrected value
    assert login_pg.wait_timeout == 5