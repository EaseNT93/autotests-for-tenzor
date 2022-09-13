from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .BaseApp import BasePage


class YandexLocators():
    SEARCH_FIELD = (By.CSS_SELECTOR, '[name = "text"]')
    SEARCH_FIELD_ITEMS = (By.CSS_SELECTOR, '.mini-suggest__item:nth-child(1)')
    NAVIGATION_BAR = (By.CSS_SELECTOR, '.container__services')
    SEARCH_RESULT_LIST = (By.ID, 'search-result')
    SEARCH_RESULT_ITEMS = (By.CSS_SELECTOR, '#search-result .Path .Link')
    SUGGEST_MENU = (By.CSS_SELECTOR, '.mini-suggest__overlay_visible')
    IMAGES_BUTTON = (By.CSS_SELECTOR, '[data-id="images"]')
    FIRST_IMAGES_CATEGORY = (
        By.CSS_SELECTOR, '.PopularRequestList-Item:nth-child(1)')
    FIRST_IMAGES = (By.CSS_SELECTOR, '.serp-item__thumb:nth-child(1)')
    NEXT_BUTTON = (By.CSS_SELECTOR, '.CircleButton_type_next')
    PREVIOUS_BUTTON = (By.CSS_SELECTOR, '.CircleButton_type_prev')
    OPENED_IMAGE_PRM = (By.CSS_SELECTOR, '.Modal_visible')
    IMAGE_SRC = (By.CSS_SELECTOR, '.MMImage-Origin')


class SearchHelper(BasePage):

    def enter_word_into_search_field(self, word: str) -> 'WebElement':
        search_field = self.find_element(
            YandexLocators.SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def press_enter_into_search_field(self) -> None:
        search_field = self.find_element(
            YandexLocators.SEARCH_FIELD, time=2)
        search_field.click()
        search_field.send_keys(Keys.ENTER)

    def get_attribute_from_elements(self, locator, attribute: str) -> list:
        all_list = self.find_elements(locator, time=2)
        result = []
        for elem in all_list:
            result.append(elem.get_attribute(attribute))
        return result
