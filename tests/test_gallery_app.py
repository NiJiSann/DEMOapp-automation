from appium_day_4 import zoom_gallery


def test_zoom_image(get_driver_with_gallery):
    assert zoom_gallery.zoom_image(get_driver_with_gallery) == 0
