import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Initialize Chrome driver session
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    yield driver
    
    # Teardown: Close all windows and end session
    driver.quit()