from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from midterm_project.pages import webview_page as wp


class WebView:
    @staticmethod
    def go_to_google(driver: WebDriver) -> int:
        wait = WebDriverWait(driver, 10)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, wp.url_ed_aid).send_keys('https://www.google.com')
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, wp.go_to_site_vg_aid).click()
        try:
            wait.until(ec.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, wp.webview_screen_aid)))
            return 0
        except:
            return 1
