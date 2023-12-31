from appium.options.common import AppiumOptions
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.webelement import WebElement


def back_home(times, driver):
    for i in range(times):
        driver.back()


def set_common_capabilities(driver_opts: AppiumOptions):
    driver_opts.set_capability("udid", "emulator-5554")
    driver_opts.set_capability("appium:automationName", "UiAutomator2")
    driver_opts.set_capability("appium:platformName", "android")
    driver_opts.set_capability("appium:deviceName", "Pixel_3a_API_34_extension_7_x86_64")
    driver_opts.set_capability("browserName", "")


def swipe_to_element(driver: WebDriver, by: str, locator: str, text: str):
    fail_count = 0
    while fail_count < 10:
        try:
            driver.swipe(150, 1000, 150, 500, 500)
            if driver.page_source.__contains__(text):
                return driver.find_element(by, locator)
        except:
            fail_count += 1
            continue



def get_center_of_elem(elem: WebElement):
    loc = elem.location
    size = elem.size
    c_x = loc['x'] + size['width'] * 0.5
    c_y = loc['y'] + size['height'] * 0.5
    return tuple((int(c_x), int(c_y)))
