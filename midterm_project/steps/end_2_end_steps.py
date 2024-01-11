import random
import time

from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from midterm_project.pages import cart_page, item_page, catalog_page, address_page, checkout_page, review_page
from midterm_project.steps.base_steps import CommonLogic
from midterm_project import keys


class End2End:
    wait: WebDriverWait = None

    @staticmethod
    def add_item_to_cart(driver: WebDriver):
        item_amount = 2
        driver.find_element(AppiumBy.XPATH, catalog_page.catalog_first_item_xpath).click()
        End2End.wait.until(ec.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, item_page.red_color_vg_aid))).click()
        plus = driver.find_element(AppiumBy.ACCESSIBILITY_ID, item_page.counter_plus_vg_aid)
        for i in range(item_amount):
            plus.click()
            time.sleep(1)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, item_page.add_to_cart_vg_aid).click()
        CommonLogic.open_cart(driver)
        try:
            End2End.wait.until(ec.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, item_page.red_color_vg_aid)))
            amount_in_cart = driver.find_element(AppiumBy.XPATH, cart_page.count_vg_xpath).text
            if int(amount_in_cart) == item_amount + 1:
                driver.find_element(AppiumBy.ACCESSIBILITY_ID, cart_page.checkout_vg_aid).click()
                return 0
        except Exception as e:
            print(e)
            pass
        return 1

    @staticmethod
    def fill_address(driver: WebDriver, **kwargs):
        elem = driver.find_element(AppiumBy.ACCESSIBILITY_ID, address_page.name_et_aid)
        elem.clear()
        elem.send_keys(kwargs[keys.full_name])
        elem = driver.find_element(AppiumBy.ACCESSIBILITY_ID, address_page.address_et_aid)
        elem.clear()
        elem.send_keys(kwargs[keys.address1])
        elem = driver.find_element(AppiumBy.ACCESSIBILITY_ID, address_page.city_et_aid)
        elem.clear()
        elem.send_keys(kwargs[keys.city])
        elem = driver.find_element(AppiumBy.ACCESSIBILITY_ID, address_page.zip_et_aid)
        elem.clear()
        elem.send_keys(kwargs[keys.zip_code])
        elem = driver.find_element(AppiumBy.ACCESSIBILITY_ID, address_page.country_et_aid)
        elem.clear()
        elem.send_keys(kwargs[keys.country])

        driver.find_element(AppiumBy.ACCESSIBILITY_ID, address_page.payment_vg_aid).click()

        if driver.page_source.__contains__("Please provide"):
            return 1
        return 0

    @staticmethod
    def fill_payment(driver: WebDriver, **kwargs):
        elem = driver.find_element(AppiumBy.ACCESSIBILITY_ID, checkout_page.name_et_aid)
        elem.clear()
        elem.send_keys(kwargs[keys.card_name])
        elem = driver.find_element(AppiumBy.ACCESSIBILITY_ID, checkout_page.card_et_aid)
        elem.clear()
        elem.send_keys(kwargs[keys.card_num])
        elem = driver.find_element(AppiumBy.ACCESSIBILITY_ID, checkout_page.exp_date_et_aid)
        elem.clear()
        elem.send_keys(kwargs[keys.exp_date])
        elem = driver.find_element(AppiumBy.ACCESSIBILITY_ID, checkout_page.code_et_aid)
        elem.clear()
        elem.send_keys(kwargs[keys.security_code])

        driver.find_element(AppiumBy.ACCESSIBILITY_ID, checkout_page.review_vg_aid).click()

        if driver.page_source.__contains__("Value looks invalid."):
            return 1
        return 0

    @staticmethod
    def check_address_payment(driver: WebDriver, **kwargs):
        if driver.page_source.__contains__(kwargs[keys.full_name]) and \
                driver.page_source.__contains__(kwargs[keys.address1]) and \
                driver.page_source.__contains__(kwargs[keys.country]) and \
                driver.page_source.__contains__(kwargs[keys.city]) and \
                driver.page_source.__contains__(kwargs[keys.zip_code]) and \
                driver.page_source.__contains__(kwargs[keys.card_num]) and \
                driver.page_source.__contains__(kwargs[keys.card_name]) and \
                driver.page_source.__contains__(kwargs[keys.security_code]) and \
                driver.page_source.__contains__(kwargs[keys.exp_date]):
            driver.find_element(AppiumBy.ACCESSIBILITY_ID, review_page.place_order_vg_aid).click()
            return 0
        return 0

    @staticmethod
    def order_completion():
        try:
            End2End.wait.until(ec.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, review_page.continue_vg_aid)))
            return 0
        except:
            return 1
