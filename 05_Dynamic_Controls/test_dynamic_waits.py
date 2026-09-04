import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from hero_kuapp import HerokuApp


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


def test_click_remove(driver):
    hero_kuapp_pg = HerokuApp(driver)
    hero_kuapp_pg.navigate_to()
    hero_kuapp_pg.click_remove()

    assert hero_kuapp_pg.capture_text == "It's gone!"


def test_click_enable(driver):
    hero_kuapp_pg = HerokuApp(driver)
    hero_kuapp_pg.navigate_to()
    hero_kuapp_pg.click_enable()

    assert hero_kuapp_pg.capture_text == "It's enabled!"