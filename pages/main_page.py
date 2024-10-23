import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.order_page_locators import OrderPageLocators

class MainPage:

    @allure.step('Находим элемент {locator}')
    def find_element_with_wait(self, locator):
        element = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return element

    @allure.step('Кликаем по элементу {locator}')
    def click_to_element(self, locator):
        self.find_element_with_wait(locator).click()

    @allure.step('Скролим до элемента {locator}')
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Получаем текст элемента {locator}')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text
