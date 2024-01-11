from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from midterm_project.pages import api_calls_page as acp


class ApiCalls:
    wait: WebDriverWait = None

    @staticmethod
    def __try_find_element(driver: WebDriver, api_calls_subpage: str, element_to_find: str) -> int:
        driver.find_element(AppiumBy.XPATH, api_calls_subpage).click()
        try:
            ApiCalls.wait.until(ec.visibility_of_element_located((AppiumBy.XPATH, element_to_find)))
            return 0
        except:
            return 1

    @staticmethod
    def get_eu_dc_item(driver: WebDriver) -> int:
        return ApiCalls.__try_find_element(driver, acp.eu_dc_vg_xpath, acp.list_item_xpath)

    @staticmethod
    def get_us_dc_item(driver: WebDriver) -> int:
        return ApiCalls.__try_find_element(driver, acp.us_dc_vg_xpath, acp.list_item_xpath)

    @staticmethod
    def get_err401(driver: WebDriver) -> int:
        return ApiCalls.__try_find_element(driver, acp.err401_vg_xpath, acp.unauthorized_tv_xpath)

    @staticmethod
    def get_err404(driver: WebDriver) -> int:
        return ApiCalls.__try_find_element(driver, acp.err404_vg_xpath, acp.not_found_tv_xpath)
