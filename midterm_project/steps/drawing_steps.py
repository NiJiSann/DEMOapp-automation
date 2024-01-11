import io
from PIL import Image
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy
from midterm_project.pages import drawing_page as dp


class Drawing:
    @staticmethod
    def draw(driver: WebDriver) -> int:
        draw_color = (226, 35, 26, 255)
        size = driver.get_window_size()
        win_half_width = size['width'] * 0.5
        win_half_height = size['height'] * 0.5
        driver.tap([(win_half_width, win_half_height-5)], 20)
        driver.tap([(win_half_width, win_half_height+5)], 20)
        driver.tap([(win_half_width-5, win_half_height)], 20)
        driver.tap([(win_half_width+5, win_half_height)], 20)
        driver.tap([(win_half_width, win_half_height)], 20)
        screenshot = driver.get_screenshot_as_png()
        image_stream = io.BytesIO(screenshot)
        img = Image.open(image_stream)
        pix = img.load()
        if pix[win_half_width, win_half_height] == draw_color:
            return 0
        return 1

    @staticmethod
    def clear_draw(driver: WebDriver) -> int:
        clear_color = (255, 217, 217, 255)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, dp.clear_vg_ait).click()
        size = driver.get_window_size()
        win_half_width = size['width'] * 0.5
        win_half_height = size['height'] * 0.5
        screenshot = driver.get_screenshot_as_png()
        image_stream = io.BytesIO(screenshot)
        img = Image.open(image_stream)
        pix = img.load()
        if pix[win_half_width, win_half_height] == clear_color:
            return 0
        return 1
