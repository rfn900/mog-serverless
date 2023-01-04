import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os

# import os


def get_mediavine_revenue(period: str):
    service = Service(executable_path=ChromeDriverManager().install())
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(service=service, options=options)

    # USERNAME = os.environ.get("MEDIAVINE_USERNAME")
    # URL = os.environ.get("MEDIAVINE_USERNAME")
    # PASSWORD = os.environ.get("MEDIAVINE_PASSWORD")
    url = "https://reporting.mediavine.com/"
    browser.get(url)

    USERNAME = os.environ.get("MEDIAVINE_USERNAME")
    PASSWORD = os.environ.get("MEDIAVINE_PASSWORD")

    time.sleep(1.5)

    input_username = browser.find_element(by=By.NAME, value="email-")
    input_password = browser.find_element(by=By.NAME, value="password-")
    btn = browser.find_elements(by=By.TAG_NAME, value="button")

    time.sleep(1.75)
    input_username.send_keys(USERNAME)
    input_password.send_keys(PASSWORD)
    time.sleep(1)

    btn[1].click()
    time.sleep(4)
    time_range_btn = browser.find_element(by=By.ID, value="button--range")
    time.sleep(0.75)

    time_range_btn.click()

    last_month_option = browser.find_element(by=By.ID, value="option-Last Month--range")

    time.sleep(0.75)

    last_month_option.click()

    time.sleep(0.75)

    table_footer = browser.find_element(by=By.TAG_NAME, value="tfoot")

    footer_cells = table_footer.find_elements(by=By.TAG_NAME, value="td")

    time.sleep(0.5)

    ammount: str = footer_cells[2].get_attribute("innerText")

    return ammount
