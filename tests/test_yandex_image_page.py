from pages.YandexPages import SearchHelper
from pages.YandexPages import YandexLocators as YaLoc


def test_yandex_image_page(browser):
    url = 'https://yandex.ru/'
    page = SearchHelper(browser, url)
    page.open()
    page.check_exists_element(YaLoc.IMAGES_BUTTON)
    page.click_on_element(YaLoc.IMAGES_BUTTON)
    page.switch_current_window()
    assert 'yandex.ru/images/' in browser.current_url
    page.click_on_element(YaLoc.FIRST_IMAGES_CATEGORY)
    assert page.check_exists_element(YaLoc.SEARCH_FIELD_ITEMS)
    page.click_on_element(YaLoc.FIRST_IMAGES)
    page.check_exists_element(YaLoc.OPENED_IMAGE_PRM)
    first_img_src = page.get_attribute_from_elements(YaLoc.IMAGE_SRC, 'src')
    page.click_on_element(YaLoc.NEXT_BUTTON)
    page.check_exists_element(YaLoc.OPENED_IMAGE_PRM)
    page.click_on_element(YaLoc.PREVIOUS_BUTTON)
    current_img_src = page.get_attribute_from_elements(YaLoc.IMAGE_SRC, 'src')
    assert first_img_src == current_img_src
