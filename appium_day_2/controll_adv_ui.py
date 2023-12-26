from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy


def find_create_btn(driver: WebDriver):
    try:
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Content").click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Storage").click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "External Storage").click()
        driver.find_element(AppiumBy.XPATH, "(//android.widget.Button[@content-desc=\"Create\"])[3]")
        return "Success", 3
    except Exception as e:
        print(e)
        return "Fail", 0


def find_arabic_text(driver: WebDriver):
    try:
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Text").click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Unicode").click()
        driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id=\"android:id/text1\" and @text=\"عربي\"]")
        return "Success", 2
    except Exception as e:
        print(e)
        return "Fail", 0


def find_fingerpaint_page(driver: WebDriver):
    try:
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Graphics").click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "FingerPaint").click()
        driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id=\"android:id/content\"]/android.view.View")
        return "Success", 2
    except Exception as e:
        print(e)
        return "Fail", 0


def find_vibrate_btn(driver: WebDriver):
    try:
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "OS").click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Morse Code").click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Vibrate")
        return "Success", 2
    except Exception as e:
        print(e)
        return "Fail", 0


def find_selection_mode_page(driver: WebDriver):
    try:
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Views").click()
        driver.swipe(500, 1500, 500, 500, 400)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Lists").click()
        driver.swipe(500, 1500, 500, 1000, 400)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "15. Selection Mode").click()
        return "Success", 3
    except Exception as e:
        print(e)
        return "Fail", 0


def find_activate_items_page(driver: WebDriver):
    try:
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Views").click()
        driver.swipe(500, 1500, 500, 500, 400)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Lists").click()
        driver.swipe(500, 1500, 500, 1000, 400)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "17. Activate items").click()
        return "Success", 3
    except Exception as e:
        print(e)
        return "Fail", 0


def find_picker_page(driver: WebDriver):
    try:
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Views").click()
        driver.swipe(500, 1500, 500, 500, 400)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Picker").click()
        return "Success", 2
    except Exception as e:
        print(e)
        return "Fail", 0


# region check attributes
def check_create_btn_clickable(driver: WebDriver):
    try:
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Content").click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Storage").click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "External Storage").click()
        elem = driver.find_element(AppiumBy.XPATH, "(//android.widget.Button[@content-desc=\"Create\"])[3]")
        if elem.get_attribute("clickable") == 'false':
            raise AttributeError
        return "Success", 3
    except Exception as e:
        print(e)
        return "Fail", 0


def check_arabic_text_clickable(driver: WebDriver):
    try:
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Text").click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Unicode").click()
        elem = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id=\"android:id/text1\" and @text=\"عربي\"]")
        if elem.get_attribute("clickable") == 'false':
            raise AttributeError
        return "Success", 2
    except Exception as e:
        print(e)
        return "Fail", 0


def check_finger_paint_is_enabled(driver: WebDriver):
    try:
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Graphics").click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "FingerPaint").click()
        elem = driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id=\"android:id/content\"]/android.view.View")
        if not elem.is_enabled():
            raise AttributeError
        return "Success", 2
    except Exception as e:
        print(e)
        return "Fail", 0


def check_vibrate_btn_clickable(driver: WebDriver):
    try:
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "OS").click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Morse Code").click()
        elem = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Vibrate")
        if elem.get_attribute("clickable") == 'false':
            raise AttributeError
        return "Success", 2
    except Exception as e:
        print(e)
        return "Fail", 0

# endregion


# region XPATH
def get_elem_with_en_text(driver: WebDriver):
    try:
        elems = driver.find_elements(AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "en")]')
        return len(elems)
    except Exception as e:
        print(e)
        return 0
# endregion

