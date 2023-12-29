from appium_day_3 import actions_waits_management as awm


class TestActionsWaitAppManagement:
    def test_find_dialog_win(self, get_driver):
        assert awm.find_dialog_win(get_driver) == 0

    def test_scroll_down(self, get_driver):
        assert awm.scroll_down(get_driver) == 0

    def test_move_app_to_bg(self, get_driver):
        assert awm.move_app_to_bg(get_driver) == 0

    def test_fill_password_name(self, get_driver):
        assert awm.fill_password_name(get_driver) == 0

    def test_wait_progress_dialog(self, get_driver):
        assert awm.wait_progress_dialog(get_driver) == 0
