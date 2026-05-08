from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import logging


def create_driver():
    options = Options()
    # options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.maximize_window()
    print("Driver initialized successfully")
    return driver

def quit_driver(driver):

    if driver is not None:
        print("Closing browser")
        logging.info("Closing browser")

        driver.quit()
        print("Browser closed successfully")