import pytest
from appium.options.common import AppiumOptions
from appium import webdriver
from helper_methods import set_common_capabilities


@pytest.fixture(scope="session")
def get_driver_with_demo_app():
    driver_opts = AppiumOptions()
    apk = "C:\\Users\\sabro\\Downloads\\Android-MyDemoAppRN.1.3.0.build-244\\Android-MyDemoAppRN.1.3.0.build-244.apk"
    driver_opts.set_capability("appium:app", apk)
    set_common_capabilities(driver_opts)
    return webdriver.Remote("http://127.0.0.1:4723", options=driver_opts)

