from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as WDwait
from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self, web_driver, url: str):
        self.driver = web_driver
        self.url = url

    def find_element(self, locator, time=10):
        except_result = EC.presence_of_element_located(locator)
        error_msg = f'Cant find element by {locator}'
        return WDwait(self.driver, time).until(except_result,
                                               message=error_msg)

    def find_elements(self, locator, time=10):
        except_result = EC.presence_of_all_elements_located(locator)
        error_msg = f'Cant find elements by {locator}'
        return WDwait(self.driver, time).until(except_result,
                                               message=error_msg)

    def click_on_element(self, locator):
        self.find_element(locator).click()

    def open(self):
        self.driver.get(self.url)

    def check_exists_element(self, locator):
        try:
            self.find_element(locator)
        except NoSuchElementException:
            return False
        return True

    def switch_current_window(self):
        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)
