from appium_day_3 import actions_waits_management as awm


class TestActionsWaitAppManagement:
    def test_find_dialog_win(self, setup_api_demos):
        assert awm.find_dialog_win(setup_api_demos) == 0

    def test_scroll_down(self, setup_api_demos):
        assert awm.scroll_down(setup_api_demos) == 0

    def test_move_app_to_bg(self, setup_api_demos):
        assert awm.move_app_to_bg(setup_api_demos) == 0

    def test_fill_password_name(self, setup_api_demos):
        assert awm.fill_password_name(setup_api_demos) == 0

    def test_wait_progress_dialog(self, setup_api_demos):
        assert awm.wait_progress_dialog(setup_api_demos) == 0
