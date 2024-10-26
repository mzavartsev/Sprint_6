from selenium import webdriver
import allure
from pages.main_page import MainPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.base_page_locators import BasePageLocators
from links import *

class TestClicksOnLogos(MainPage):

    @allure.title("Нажатие на логотип сайта")
    @allure.description("Проверка перехода на основную страницу при клике на логотип сайта")
    @allure.link(ORDER_URL, name='https://qa-scooter.praktikum-services.ru/order')
    def test_click_scooter_logo(self, driver_start):
        self.click_to_element(BasePageLocators.scooter_logo, driver_start)
        assert BASE_URL == driver_start.current_url

    @allure.title("Нажатие на логотип яндекса")
    @allure.description("Проверка перехода на yandex dzen при клике на логотип yandex")
    @allure.link(BASE_URL, name='https://qa-scooter.praktikum-services.ru/')
    def test_click_yandex_logo(self, driver_start):
        self.click_to_element(BasePageLocators.yandex_logo, driver_start)
        driver_start.switch_to.window(driver_start.window_handles[1])
        WebDriverWait(driver_start, 10).until(expected_conditions.visibility_of_element_located
                                             (BasePageLocators.yandex_dzen_find_button))
        assert "dzen.ru/" in driver_start.current_url

