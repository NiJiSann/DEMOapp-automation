from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from helper_methods import get_center_of_elem
import Locators


def zoom_image(driver: WebDriver):
    wait = WebDriverWait(driver, 10)
    try:
        wait.until(ec.element_to_be_clickable((AppiumBy.ID, Locators.allow_all))).click()
        wait.until(ec.element_to_be_clickable((AppiumBy.ID, Locators.free_trail))).click()
    except:
        pass

    download_btn = wait.until(ec.presence_of_element_located((AppiumBy.XPATH, Locators.download_folder)))
    driver.tap([get_center_of_elem(download_btn)])
    wait.until(ec.element_to_be_clickable((AppiumBy.XPATH, Locators.image))).click()
    wait.until(ec.presence_of_element_located((AppiumBy.ID, Locators.image_view)))
    size = driver.get_window_size()
    win_half_width = size['width'] * 0.5
    win_half_height = size['height'] * 0.5

    action_1 = TouchAction(driver)
    action_2 = TouchAction(driver)
    m_action = MultiAction(driver)

    action_1.long_press(x=win_half_width - 50, y=win_half_height).move_to(x=win_half_width - 200, y=win_half_height).wait(500).release()
    action_2.long_press(x=win_half_width + 50, y=win_half_height).move_to(x=win_half_width + 200, y=win_half_height).wait(500).release()
    m_action.add(action_1, action_2)
    m_action.perform()
    return 0

