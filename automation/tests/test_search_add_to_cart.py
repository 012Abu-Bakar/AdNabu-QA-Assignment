
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from automation.utils.driver_factory import create_driver, quit_driver
from automation.config import STORE_URL, STORE_PASSWORD, PRODUCT_NAME

def login_to_store(driver, wait):

    # Locators
    shopify_logo = (
        By.XPATH,
        "//div[@class='hero']//*[local-name()='svg']"
    )

    store_name = (
        By.XPATH,
        "//div[@class='content']//h2//*[text()='adnabu-store']"
    )

    store_password = (By.ID, "password")

    submit_password_btn = (
        By.XPATH,
        "//button[text()='Enter']"
    )

    login_validate = (
        By.XPATH,
        "//h1[@class='header__heading']//*[text()='adnabu-store']"
    )

    # Validate logo
    logo = wait.until(
        EC.visibility_of_element_located(shopify_logo)
    )

    assert logo.is_displayed(), "Logo not displayed"

    # Validate store name
    name = wait.until(
        EC.visibility_of_element_located(store_name)
    )

    assert name.is_displayed(), "Store name not displayed"

    print("Website opened successfully")


    # Enter password
    password = wait.until(
        EC.visibility_of_element_located(store_password)
    )

    password.send_keys(STORE_PASSWORD)

    # Click submit
    submit_btn = wait.until(
        EC.element_to_be_clickable(submit_password_btn)
    )

    submit_btn.click()

    # Validate login
    login_header = wait.until(
        EC.visibility_of_element_located(login_validate)
    )

    assert login_header.is_displayed(), "Login header not displayed"

    print("Store login successful")

def search_product(driver, wait, product_name):

    search_icon = (
        By.XPATH,
        "//summary[contains(@aria-label,'Search')]"
    )

    search_input = (
        By.XPATH,
        "//input[@type='search']"
    )

    search_btn = wait.until(
        EC.element_to_be_clickable(search_icon)
    )

    search_btn.click()

    search_box = wait.until(
        EC.visibility_of_element_located(search_input)
    )

    search_box.send_keys(product_name)


def open_first_product(driver, wait):

    first_product = (
        By.XPATH,
        "(//a[contains(@href,'products')])[1]"
    )

    product = wait.until(
        EC.element_to_be_clickable(first_product)
    )

    product.click()


def add_product_to_cart(driver, wait):

    add_to_cart_btn = (
        By.XPATH,
        "//button[contains(@id,'ProductSubmitButton-')]"
    )

    add_cart = wait.until(
        EC.element_to_be_clickable(add_to_cart_btn)
    )

    add_cart.click()


def verify_product_added(driver, wait):

    cart_item = (
        By.XPATH,
        "//table[@class='cart-items']//tbody//td//a[text()='The Collection Snowboard: Oxygen']"
    )

    added_product = wait.until(
        EC.visibility_of_element_located(cart_item)
    )

    assert added_product.is_displayed(), "Product not added to cart"

    print("Product added to cart successfully")


def test_search_and_add_to_cart():

    driver = create_driver()

    wait = WebDriverWait(driver, 10)

    try:

        driver.get(STORE_URL)

        login_to_store(driver, wait)

        search_product(driver, wait, PRODUCT_NAME)

        open_first_product(driver, wait)

        add_product_to_cart(driver, wait)

        verify_product_added(driver, wait)

    finally:
        quit_driver(driver)