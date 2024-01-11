import pytest
from midterm_project.steps.base_steps import CommonLogic
from midterm_project.steps.api_calls_steps import ApiCalls
from midterm_project.steps.drawing_steps import Drawing
from midterm_project.steps.end_2_end_steps import End2End
from midterm_project.steps.geo_location_steps import Location
from midterm_project.steps.login_steps import Login
from midterm_project.steps.reset_app_steps import Reset
from midterm_project.steps.webview_steps import WebView
from selenium.webdriver.support.ui import WebDriverWait
from pytest_check import check
from midterm_project import err_messages as em
from midterm_project import data


class TestApiCalls:

    def test_api_calls_setup(self, get_driver_with_demo_app):
        wait = WebDriverWait(get_driver_with_demo_app, 10)
        ApiCalls.wait = wait
        CommonLogic.wait = wait
        CommonLogic.open_api_calls(get_driver_with_demo_app)

    def test_get_err404(self, get_driver_with_demo_app):
        with check:
            assert ApiCalls.get_err404(get_driver_with_demo_app) == 0

    def test_get_err401(self, get_driver_with_demo_app):
        with check:
            assert ApiCalls.get_err401(get_driver_with_demo_app) == 0

    def test_us_dc_item(self, get_driver_with_demo_app):
        with check:
            assert ApiCalls.get_us_dc_item(get_driver_with_demo_app) == 0

    def test_eu_dc_item(self, get_driver_with_demo_app):
        with check:
            assert ApiCalls.get_eu_dc_item(get_driver_with_demo_app) == 0


class TestDrawing:
    def test_drawing_setup(self, get_driver_with_demo_app):
        wait = WebDriverWait(get_driver_with_demo_app, 10)
        CommonLogic.wait = wait
        CommonLogic.open_drawing(get_driver_with_demo_app)

    def test_draw(self, get_driver_with_demo_app):
        with check:
            assert Drawing.draw(get_driver_with_demo_app) == 0

    def test_clear_draw(self, get_driver_with_demo_app):
        with check:
            assert Drawing.clear_draw(get_driver_with_demo_app) == 0


class TestEnd2End:
    def test_end2end_setup(self, get_driver_with_demo_app):
        wait = WebDriverWait(get_driver_with_demo_app, 10)
        CommonLogic.wait = wait
        End2End.wait = wait
        Login.wait = wait
        CommonLogic.open_login(get_driver_with_demo_app)
        Login.log_in(get_driver_with_demo_app, 'bob@example.com', '10203040')

    def test_add_item_to_cart(self, get_driver_with_demo_app):
        with check:
            assert End2End.add_item_to_cart(get_driver_with_demo_app) == 0

    @pytest.mark.parametrize(['address_data', 'expected_result'],
                             [(data.address_data_1, 1),
                              (data.address_data_2_correct, 0)])
    def test_fill_address(self, get_driver_with_demo_app, address_data, expected_result):
        with check:
            assert End2End.fill_address(get_driver_with_demo_app, **address_data) == expected_result

    @pytest.mark.parametrize(['card_data', 'expected_result'],
                             [(data.card_data_1, 1),
                              (data.card_data_2, 1),
                              (data.card_data_3, 1),
                              (data.card_data_4, 1),
                              (data.card_data_5, 1),
                              (data.card_data_6, 1),
                              (data.card_data_7_correct, 0)
                              ])
    def test_fill_payment(self, get_driver_with_demo_app, card_data, expected_result):
        with check:
            assert End2End.fill_payment(get_driver_with_demo_app, **card_data) == expected_result

    def test_check_address_payment(self, get_driver_with_demo_app):
        with check:
            assert End2End.check_address_payment(get_driver_with_demo_app,  **data.data_to_check) == 0

    def test_order_completion(self):
        with check:
            assert End2End.order_completion() == 0


class TestLocation:

    def test_location_setup(self, get_driver_with_demo_app):
        wait = WebDriverWait(get_driver_with_demo_app, 10)
        CommonLogic.wait = wait
        CommonLogic.open_geo_location(get_driver_with_demo_app)

    @pytest.mark.parametrize(['longitude', 'latitude', 'expected_result'],
                             [(20, 20, 0),
                              (25, 25, 0),
                              (30, 30, 0)])
    def test_device_location(self, get_driver_with_demo_app, longitude, latitude, expected_result):
        with check:
            assert Location.device_location(get_driver_with_demo_app, longitude, latitude) == expected_result


class TestLogin:
    def test_login_setup(self, get_driver_with_demo_app):
        wait = WebDriverWait(get_driver_with_demo_app, 10)
        CommonLogic.wait = wait
        Login.wait = wait
        CommonLogic.open_login(get_driver_with_demo_app)

    @pytest.mark.parametrize(['username', 'password', 'expected_result'],
                             [('qwerty@sync.xyz', '12345', em.wrong_input_err_message),
                              ('alice@example.com', '10203040', em.locked_user_err_message),
                              ('bob@example.com', '10203040', 0)])
    def test_login(self, get_driver_with_demo_app, username, password, expected_result):
        with check:
            assert Login.log_in(get_driver_with_demo_app, username, password) == expected_result

    def test_logout(self, get_driver_with_demo_app):
        with check:
            CommonLogic.open_logout(get_driver_with_demo_app)
            assert Login.log_out(get_driver_with_demo_app) == 0

    def test_turn_on_fingerprint(self,  get_driver_with_demo_app):
        with check:
            assert Login.turn_on_fingerprint(get_driver_with_demo_app) == 0

    def test_login_fingerprint(self, get_driver_with_demo_app):
        with check:
            assert Login.log_in_fingerprint(get_driver_with_demo_app) == 0


class TestResetApp:
    def test_reset_app(self, get_driver_with_demo_app):
        wait = WebDriverWait(get_driver_with_demo_app, 10)
        CommonLogic.wait = wait
        End2End.wait = wait
        End2End.add_item_to_cart(get_driver_with_demo_app)
        CommonLogic.open_reset_app(get_driver_with_demo_app)
        with check:
            assert Reset.reset_app(get_driver_with_demo_app) == 0


class TestWebView:
    def test_go_to_google(self, get_driver_with_demo_app):
        wait = WebDriverWait(get_driver_with_demo_app, 10)
        CommonLogic.wait = wait
        CommonLogic.open_webview(get_driver_with_demo_app)
        with check:
            assert WebView.go_to_google(get_driver_with_demo_app) == 0
