import random

from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from helper_methods import swipe_to_element, get_center_of_elem, back_home
import Locators


def find_username_password_alert(driver: WebDriver):
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'App').click()
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Alert Dialogs').click()
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Text Entry dialog').click()
    wait = WebDriverWait(driver, 10)
    wait.until(ec.alert_is_present())
    if driver.page_source.__contains__('username') and driver.page_source.__contains__('password'):
        return 0


def try_type_and_clear(driver: WebDriver):
    wait = WebDriverWait(driver, 10)
    wait.until(ec.alert_is_present())
    username_tv = driver.find_element(AppiumBy.XPATH, Locators.username_tv)
    username_tv.send_keys('qwerty')
    if username_tv.text == '':
        return 1
    username_tv.clear()
    if username_tv.text != '':
        return 1
    return 0


def use_clipboard(driver: WebDriver):
    clipboard_val = '123456'
    driver.set_clipboard_text(clipboard_val)
    username_tv = driver.find_element(AppiumBy.XPATH, Locators.username_tv)
    username_tv.send_keys(driver.get_clipboard_text())
    if username_tv.text != clipboard_val:
        return 1
    return 0


def accept_alert(driver: WebDriver):
    alert = driver.switch_to.alert
    password_tv = driver.find_element(AppiumBy.XPATH, Locators.password_tv)
    password_tv.send_keys('qwerty')
    alert.accept()
    return 0


def find_selection_mode(driver: WebDriver):
    back_home(3, driver)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Views').click()
    swipe_to_element(driver, AppiumBy.ACCESSIBILITY_ID, 'Lists', 'Lists').click()
    swipe_to_element(driver, AppiumBy.ACCESSIBILITY_ID, '15. Selection Mode', '15. Selection Mode').click()
    return 0


def tap_on_random_element(driver: WebDriver):
    elements = driver.find_elements(AppiumBy.XPATH, Locators.any_ctv)
    random_ctv = elements[random.randint(0, len(elements))]
    driver.tap([get_center_of_elem(random_ctv)])
    for element in elements:
        if element.get_attribute('checked') == 'true':
            return 1
    return 0


def long_press(driver: WebDriver):
    elements = driver.find_elements(AppiumBy.XPATH, Locators.any_ctv)
    random_ctv = elements[random.randint(0, len(elements))]
    driver.tap([get_center_of_elem(random_ctv)], 1000)
    if random_ctv.get_attribute('checked') != 'true':
        return 1
    return 0


def tick_all_elem(driver: WebDriver):
    elements = driver.find_elements(AppiumBy.XPATH, Locators.any_ctv)
    random_ctv = elements[random.randint(0, len(elements))]
    driver.tap([get_center_of_elem(random_ctv)], 100)
    for element in elements:
        element.click()
    driver.back()
    for element in elements:
        if element.get_attribute('checked') == 'true':
            return 1
    return 0

