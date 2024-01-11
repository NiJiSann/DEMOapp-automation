import time

from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from midterm_project.pages import log_in_page as lip
from midterm_project.pages import finger_print_page as fp
from midterm_project import err_messages as em
from midterm_project.steps.base_steps import CommonLogic


class Login:
    wait: WebDriverWait = None
    @staticmethod
    def log_in(driver: WebDriver, username: str, password: str):
        elem = driver.find_element(AppiumBy.ACCESSIBILITY_ID, lip.username_et_aid)
        elem.clear()
        elem.send_keys(username)
        elem = driver.find_element(AppiumBy.ACCESSIBILITY_ID, lip.password_et_aid)
        elem.clear()
        elem.send_keys(password)

        driver.find_element(AppiumBy.ACCESSIBILITY_ID, lip.login_vg_aid).click()

        if driver.page_source.__contains__(em.wrong_input_err_message):
            return em.wrong_input_err_message
        elif driver.page_source.__contains__(em.locked_user_err_message):
            return em.locked_user_err_message
        time.sleep(2)
        if driver.page_source.__contains__('Checkout') or driver.page_source.__contains__('Products'):
            return 0
        return 1

    @staticmethod
    def log_out(driver: WebDriver):
        Login.wait.until(ec.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        try:
            Login.wait.until(ec.alert_is_present())
            alert = driver.switch_to.alert
            alert.accept()
        except:
            pass

        if driver.page_source.__contains__("Login") or driver.page_source.__contains__("FingerPrint"):
            return 0

        return 1

    @staticmethod
    def turn_on_fingerprint(driver: WebDriver):
        CommonLogic.open_fingerprint(driver)
        switch = Login.wait.until(ec.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, fp.biometrics_sw_aid)))
        if switch.get_attribute('checked') == 'false':
            switch.click()
        try:
            Login.wait.until(ec.element_to_be_clickable((AppiumBy.ID, fp.cancel_fingerprint_btn_id))).click()
        except:
            pass
        time.sleep(2)
        return 0

    @staticmethod
    def log_in_fingerprint(driver: WebDriver):
        CommonLogic.open_login(driver)
        Login.wait.until(ec.element_to_be_clickable((AppiumBy.ID, fp.cancel_fingerprint_btn_id)))
        driver.finger_print(1)
        if driver.page_source.__contains__("Login") or driver.page_source.__contains__("FingerPrint"):
            return 0
        return 1

