from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def find_dialog_win(driver: WebDriver):
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'App').click()
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Alert Dialogs').click()
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'OK Cancel dialog with ultra long message').click()
    return 0


def scroll_down(driver: WebDriver):
    driver.swipe(500, 1200, 500, 400, 300)
    driver.swipe(500, 1200, 500, 400, 300)
    driver.swipe(500, 1200, 500, 400, 300)
    driver.find_element(AppiumBy.ID, 'android:id/button1').click()
    return 0


def move_app_to_bg(driver: WebDriver):
    driver.background_app(1)
    return 0


def fill_password_name(driver: WebDriver):
    wait = WebDriverWait(driver, 20)
    text_entry_dialog = wait.until(ec.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Text Entry dialog')))
    text_entry_dialog.click()
    driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="io.appium.android.apis:id/username_edit"]').send_keys('qwerty')
    driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="io.appium.android.apis:id/password_edit"]').send_keys('12345678')
    driver.find_element(AppiumBy.ID, 'android:id/button1').click()
    return 0


def wait_progress_dialog(driver: WebDriver):
    wait = WebDriverWait(driver, 20)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Progress dialog').click()
    wait.until(ec.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'List dialog')))
    list_dialog = wait.until(ec.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'List dialog')))
    list_dialog.click()
    driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="Command four"]').click()
    return 0
