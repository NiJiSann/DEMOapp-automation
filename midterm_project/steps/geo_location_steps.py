import time

from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy
from midterm_project.pages import geo_location_page as glp
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Location:
    @staticmethod
    def device_location(driver: WebDriver, longitude: float, latitude: float) -> int:
        try:
            wait = WebDriverWait(driver, 10)
            wait.until(ec.element_to_be_clickable((AppiumBy.ID, glp.allow_location_btn_id))).click()
        except:
            pass
        time.sleep(1)
        driver.set_location(longitude, latitude)
        time.sleep(5)
        longitude_val = float(driver.find_element(AppiumBy.ACCESSIBILITY_ID, glp.longitude_tv_aid).text)
        latitude_val = float(driver.find_element(AppiumBy.ACCESSIBILITY_ID, glp.latitude_tv_aid).text)
        if longitude - 1 < longitude_val < longitude + 1 and latitude - 1 < latitude_val < latitude + 1:
            return 0
        return 1
