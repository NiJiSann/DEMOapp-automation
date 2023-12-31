from appium_day_2 import controll_adv_ui as cui
from helper_methods import back_home


class TestAppiumUI:
    def test_find_create_btn(self, get_driver_with_api_demos):
        res = cui.find_create_btn(get_driver_with_api_demos)
        assert res[0] == "Success"
        back_home(res[1], get_driver_with_api_demos)

    def test_find_arabic_text(self, get_driver_with_api_demos):
        res = cui.find_arabic_text(get_driver_with_api_demos)
        assert res[0] == "Success"
        back_home(res[1], get_driver_with_api_demos)

    def test_find_fingerpaint_page(self, get_driver_with_api_demos):
        res = cui.find_fingerpaint_page(get_driver_with_api_demos)
        assert res[0] == "Success"
        back_home(res[1], get_driver_with_api_demos)

    def test_find_vibrate_btn(self, get_driver_with_api_demos):
        res = cui.find_vibrate_btn(get_driver_with_api_demos)
        assert res[0] == "Success"
        back_home(res[1], get_driver_with_api_demos)

    def test_find_selection_mode_page(self, get_driver_with_api_demos):
        res = cui.find_selection_mode_page(get_driver_with_api_demos)
        assert res[0] == "Success"
        back_home(res[1], get_driver_with_api_demos)

    def test_find_activate_items_page(self, get_driver_with_api_demos):
        res = cui.find_activate_items_page(get_driver_with_api_demos)
        assert res[0] == "Success"
        back_home(res[1], get_driver_with_api_demos)

    def test_find_picker_page(self, get_driver_with_api_demos):
        res = cui.find_picker_page(get_driver_with_api_demos)
        assert res[0] == "Success"
        back_home(res[1], get_driver_with_api_demos)


class TestAppiumUIAttribute:
    def test_check_create_btn_clickable(self, get_driver_with_api_demos):
        res = cui.check_create_btn_clickable(get_driver_with_api_demos)
        assert res[0] == "Success"
        back_home(res[1], get_driver_with_api_demos)

    def test_check_arabic_text_clickable(self, get_driver_with_api_demos):
        res = cui.check_arabic_text_clickable(get_driver_with_api_demos)
        assert res[0] == "Success"
        back_home(res[1], get_driver_with_api_demos)

    def test_check_finger_paint_is_enabled(self, get_driver_with_api_demos):
        res = cui.check_finger_paint_is_enabled(get_driver_with_api_demos)
        assert res[0] == "Success"
        back_home(res[1], get_driver_with_api_demos)

    def test_check_vibrate_btn_clickable(self, get_driver_with_api_demos):
        res = cui.check_vibrate_btn_clickable(get_driver_with_api_demos)
        assert res[0] == "Success"
        back_home(res[1], get_driver_with_api_demos)


def test_get_elem_with_en_text(get_driver_with_api_demos):
    assert cui.get_elem_with_en_text(get_driver_with_api_demos) == 2
