import pytest
from appium.options.common import AppiumOptions
from appium import webdriver


@pytest.fixture(scope="session")
def get_driver():
    app_package_name = 'io.appium.android.apis'

    driver_opts = AppiumOptions()
    driver_opts.set_capability("appium:app", "C:\\Users\\sabro\\Downloads\\ApiDemos-debug\\ApiDemos-debug.apk")
    driver_opts.set_capability("udid", "emulator-5554")
    driver_opts.set_capability("appium:automationName", "UiAutomator2")
    driver_opts.set_capability("appium:platformName", "android")
    driver_opts.set_capability("appium:deviceName", "Pixel_3a_API_34_extension_7_x86_64")
    driver_opts.set_capability("browserName", "")
    driver = webdriver.Remote("http://127.0.0.1:4723", options=driver_opts)
    if driver.is_app_installed(app_package_name):
        print('\nStarting tests...\n')
    else:
        print('\nPackage not installed. Please install testing application\n')
        return
    yield driver
    print('\n\nTerminating application...')
    driver.terminate_app(app_package_name)
    print('\nUninstalling application...')
    driver.remove_app(app_package_name)
    print('\nEnding tests...')
