from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from midterm_project.steps.base_steps import CommonLogic
from midterm_project.pages import cart_page as cp


class Reset:
    @staticmethod
    def reset_app(driver: WebDriver):
        wait = WebDriverWait(driver, 10)
        wait.until(ec.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        wait.until(ec.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        driver.back()
        CommonLogic.open_cart(driver)
        try:
            wait.until(ec.presence_of_element_located((AppiumBy.XPATH, cp.no_items_tv_xpath)))
            return 0
        except:
            return 1

