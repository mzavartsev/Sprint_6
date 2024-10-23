from selenium import webdriver
import allure
from pages.main_page import MainPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.base_page_locators import BasePageLocators
from links import *

class TestClicksOnLogos(MainPage):
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(base_url)

    @allure.title("Нажатие на логотип сайта")
    @allure.description("Проверка перехода на основную страницу при клике на логотип сайта")
    @allure.link(order_url, name='https://qa-scooter.praktikum-services.ru/order')
    def test_click_scooter_logo(self):
        self.driver.get(order_url)
        self.click_to_element(BasePageLocators.scooter_logo)
        assert "https://qa-scooter.praktikum-services.ru/" == self.driver.current_url

    @allure.title("Нажатие на логотип яндекса")
    @allure.description("Проверка перехода на yandex dzen при клике на логотип yandex")
    @allure.link(base_url, name='https://qa-scooter.praktikum-services.ru/')
    def test_click_yandex_logo(self):
        self.driver.get(base_url)
        self.click_to_element(BasePageLocators.yandex_logo)
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located
                                             (BasePageLocators.yandex_dzen_find_button))
        assert "dzen.ru/" in self.driver.current_url

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
