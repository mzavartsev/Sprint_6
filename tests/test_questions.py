from selenium import webdriver
import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from links import *

class TestQuestions(MainPage):
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(base_url)

    @allure.title("Сколько это стоит? И как оплатить?")
    @allure.description("Проверка отображения ответа на вопрос 'Сколько это стоит? И как оплатить?'")
    def test_check_what_is_the_price(self):
        self.scroll_to_element(MainPageLocators.what_is_the_price)
        self.click_to_element(MainPageLocators.what_is_the_price)
        assert "400 рублей" in self.get_text_from_element(MainPageLocators.what_is_the_price_answer)

    @allure.title("Хочу сразу несколько самокатов! Так можно?")
    @allure.description("Проверка отображения ответа на вопрос 'Хочу сразу несколько самокатов! Так можно?'")
    def test_check_is_it_possible_to_order_several_scooters(self):
        self.scroll_to_element(MainPageLocators.is_it_possible_to_order_several_scooters)
        self.click_to_element(MainPageLocators.is_it_possible_to_order_several_scooters)
        assert ("один заказ — один самокат" in self.get_text_from_element
        (MainPageLocators.is_it_possible_to_order_several_scooters_answer))

    @allure.title("Как рассчитывается время аренды?")
    @allure.description("Проверка отображения ответа на вопрос 'Как рассчитывается время аренды?'")
    def test_check_how_is_rental_time_calculated(self):
        self.scroll_to_element(MainPageLocators.how_is_rental_time_calculated)
        self.click_to_element(MainPageLocators.how_is_rental_time_calculated)
        assert ("Отсчёт времени аренды начинается с момента" in self.get_text_from_element
        (MainPageLocators.how_is_rental_time_calculated_answer))

    @allure.title("Можно ли заказать самокат прямо на сегодня?")
    @allure.description("Проверка отображения ответа на вопрос 'Можно ли заказать самокат прямо на сегодня?'")
    def test_check_is_it_possible_to_order_a_scooter_for_today(self):
        self.scroll_to_element(MainPageLocators.is_it_possible_to_order_a_scooter_for_today)
        self.click_to_element(MainPageLocators.is_it_possible_to_order_a_scooter_for_today)
        assert ("Только начиная с завтрашнего дня" in self.get_text_from_element
        (MainPageLocators.is_it_possible_to_order_a_scooter_for_today_answer))

    @allure.title("Можно ли продлить заказ или вернуть самокат раньше?")
    @allure.description("Проверка отображения ответа на вопрос 'Можно ли продлить заказ или вернуть самокат раньше?'")
    def test_check_is_it_possible_to_extend_the_order(self):
        self.scroll_to_element(MainPageLocators.is_it_possible_to_extend_the_order)
        self.click_to_element(MainPageLocators.is_it_possible_to_extend_the_order)
        assert ("Пока что нет!" in self.get_text_from_element
        (MainPageLocators.is_it_possible_to_extend_the_order_answer))

    @allure.title("Вы привозите зарядку вместе с самокатом?")
    @allure.description("Проверка отображения ответа на вопрос 'Вы привозите зарядку вместе с самокатом?'")
    def test_check_do_you_bring_a_charger(self):
        self.scroll_to_element(MainPageLocators.do_you_bring_a_charger)
        self.click_to_element(MainPageLocators.do_you_bring_a_charger)
        assert ("не понадобится" in self.get_text_from_element
        (MainPageLocators.do_you_bring_a_charger_answer))

    @allure.title("Можно ли отменить заказ?")
    @allure.description("Проверка отображения ответа на вопрос 'Можно ли отменить заказ?'")
    def test_check_is_it_possible_to_cancel_an_order(self):
        self.scroll_to_element(MainPageLocators.is_it_possible_to_cancel_an_order)
        self.click_to_element(MainPageLocators.is_it_possible_to_cancel_an_order)
        assert ("Да, пока самокат не привезли" in self.get_text_from_element
        (MainPageLocators.is_it_possible_to_cancel_an_order_answer))

    @allure.title("Я жизу за МКАДом, привезёте?")
    @allure.description("Проверка отображения ответа на вопрос 'Я жизу за МКАДом, привезёте?'")
    def test_check_i_live_outside_the_MRR(self):
        self.scroll_to_element(MainPageLocators.i_live_outside_the_MRR)
        self.click_to_element(MainPageLocators.i_live_outside_the_MRR)
        assert ("Всем самокатов! И Москве, и Московской области" in self.get_text_from_element
        (MainPageLocators.i_live_outside_the_MRR_answer))

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
