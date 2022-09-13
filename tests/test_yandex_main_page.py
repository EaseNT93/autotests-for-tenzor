from pages.YandexPages import SearchHelper
from pages.YandexPages import YandexLocators as YaLoc


def test_yandex_search_page(browser):
    url = 'https://yandex.ru/'
    page = SearchHelper(browser, url)
    page.open()
    assert page.check_exists_element(YaLoc.SEARCH_FIELD)
    page.enter_word_into_search_field('Тензор')
    assert page.check_exists_element(YaLoc.SUGGEST_MENU)
    page.press_enter_into_search_field()
    finded_url_list = page.get_attribute_from_elements(
        YaLoc.SEARCH_RESULT_ITEMS, 'href')
    assert 'tensor.ru' in finded_url_list[0]
