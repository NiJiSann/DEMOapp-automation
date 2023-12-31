import pytest
from appium.options.common import AppiumOptions
from appium import webdriver
from helper_methods import set_common_capabilities
from appium.options.android import UiAutomator2Options


@pytest.fixture(scope="session")
def get_driver_with_api_demos():
    driver_opts = AppiumOptions()
    driver_opts.set_capability("appium:app", "C:\\Users\\sabro\\Downloads\\ApiDemos-debug\\ApiDemos-debug.apk")
    set_common_capabilities(driver_opts)
    return webdriver.Remote("http://127.0.0.1:4723", options=driver_opts)


@pytest.fixture(scope="session")
def get_driver_with_gallery():
    capabilities = dict(
        platformName='Android',
        automationName='uiautomator2',
        deviceName='Android',
        appPackage='com.simplemobiletools.gallery',
        appActivity='.activities.MainActivity',
        language='en',
        locale='US'
    )
    options = UiAutomator2Options().load_capabilities(capabilities)
    return webdriver.Remote("http://127.0.0.1:4723", options=options)


@pytest.fixture(scope="session")
def setup_api_demos(get_driver_with_api_demos):
    app_package_name = 'io.appium.android.apis'
    driver = get_driver_with_api_demos
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
