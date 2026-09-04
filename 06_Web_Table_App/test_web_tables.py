import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from web_table_page import WebTablePage

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--guest")
    chrome_options.add_argument("--disable-save-password-bubble")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")

    browser = webdriver.Chrome(options=chrome_options)
    browser.maximize_window()
    yield browser

    browser.quit()

def test_search_existing_user(driver):
    table_pg = WebTablePage(driver)
    table_pg.navigate_to()
    
    # 1. Search for existing user "Cierra"
    table_pg.search_text("Cierra")
    
    # 2. Assert filtered row data contains expected email
    assert "cierra@example.com" in table_pg.get_table_data

def test_add_new_user_and_verify(driver):
    table_pg = WebTablePage(driver)
    table_pg.navigate_to()
    
    # 1. Add new entry via popup modal
    table_pg.add_user("Aarav", "Ind", "aarav@test.com", "28", "95000", "QA")
    
    # 2. Search for newly added user
    table_pg.search_text("Aarav")
    
    # 3. Assert user exists in the updated web table
    assert "aarav@test.com" in table_pg.get_table_data

def test_verify_4th_row_user_details(driver):
    table_pg = WebTablePage(driver)
    table_pg.navigate_to()

    # 1. Define expected test data
    fname, lname, email, age, salary, dept = "test", "user", "testuser@gmail.com", "38", "11000", "QA"

    # 2. Add user via modal
    table_pg.add_user(fname, lname, email, age, salary, dept)

    # 3. Read details specifically from the 4th row (index 4)
    row_data = table_pg.get_row_details(4)

    # 4. Assert every field in order [First Name, Last Name, Age, Email, Salary, Department]
    assert row_data[0] == fname
    assert row_data[1] == lname
    assert row_data[2] == age
    assert row_data[3] == email
    assert row_data[4] == salary
    assert row_data[5] == dept