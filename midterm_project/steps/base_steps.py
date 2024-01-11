from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy
from midterm_project.pages import base_page as bp
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class CommonLogic:
    wait: WebDriverWait = None

    @staticmethod
    def __open_page(driver: WebDriver, page_locator: str):
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, bp.open_menu_vg_aid).click()
        CommonLogic.wait.until(ec.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, page_locator))).click()

    @staticmethod
    def open_cart(driver: WebDriver):
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, bp.cart_vg_aid).click()

    @staticmethod
    def open_catalog(driver: WebDriver):
        CommonLogic.__open_page(driver, bp.catalog_vg_aid)

    @staticmethod
    def open_webview(driver: WebDriver):
        CommonLogic.__open_page(driver, bp.webview_vg_aid)

    @staticmethod
    def open_geo_location(driver: WebDriver):
        CommonLogic.__open_page(driver, bp.geo_location_vg_aid)

    @staticmethod
    def open_drawing(driver: WebDriver):
        CommonLogic.__open_page(driver, bp.drawing_vg_aid)

    @staticmethod
    def open_reset_app(driver: WebDriver):
        CommonLogic.__open_page(driver, bp.reset_app_state_vg_aid)

    @staticmethod
    def open_fingerprint(driver: WebDriver):
        CommonLogic.__open_page(driver, bp.finger_print_vg_aid)

    @staticmethod
    def open_login(driver: WebDriver):
        CommonLogic.__open_page(driver, bp.log_in_vg_aid)

    @staticmethod
    def open_logout(driver: WebDriver):
        CommonLogic.__open_page(driver, bp.log_out_vg_aid)

    @staticmethod
    def open_api_calls(driver: WebDriver):
        CommonLogic.__open_page(driver, bp.api_calls_vg_aid)
