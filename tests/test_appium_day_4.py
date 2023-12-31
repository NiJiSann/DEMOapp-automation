from appium_day_4 import gestures_checkboxes_keyboard as gck


class TestGesturesCheckboxesKeyboard:
    def test_find_username_password_alert(self, get_driver_with_api_demos):
        assert gck.find_username_password_alert(get_driver_with_api_demos) == 0

    def test_try_type_and_clear(self, get_driver_with_api_demos):
        assert gck.try_type_and_clear(get_driver_with_api_demos) == 0

    def test_use_clipboard(self, get_driver_with_api_demos):
        assert gck.use_clipboard(get_driver_with_api_demos) == 0

    def test_accept_alert(self, get_driver_with_api_demos):
        assert gck.accept_alert(get_driver_with_api_demos) == 0

    def test_find_selection_mode(self, get_driver_with_api_demos):
        assert gck.find_selection_mode(get_driver_with_api_demos) == 0

    def test_tap_on_random_element(self, get_driver_with_api_demos):
        assert gck.tap_on_random_element(get_driver_with_api_demos) == 0

    def test_long_press(self, get_driver_with_api_demos):
        assert gck.long_press(get_driver_with_api_demos) == 0

    def test_tick_all_elem(self, get_driver_with_api_demos):
        assert gck.tick_all_elem(get_driver_with_api_demos) == 0
