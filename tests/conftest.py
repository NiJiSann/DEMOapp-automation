import pytest
from appium.options.common import AppiumOptions
from appium import webdriver


@pytest.fixture(scope="session")
def get_driver():
    driver_opts = AppiumOptions()
    driver_opts.set_capability("appium:app", "C:\\Users\\sabro\\Downloads\\ApiDemos-debug\\ApiDemos-debug.apk")
    driver_opts.set_capability("udid", "emulator-5554")
    driver_opts.set_capability("appium:automationName", "UiAutomator2")
    driver_opts.set_capability("appium:platformName", "android")
    driver_opts.set_capability("appium:deviceName", "Pixel_3a_API_34_extension_7_x86_64")
    driver_opts.set_capability("browserName", "")
    return webdriver.Remote("http://127.0.0.1:4723", options=driver_opts)
