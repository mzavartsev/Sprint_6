from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from Sprint_6.links import links


class OrderPage:
    name_field = [By.CSS_SELECTOR, "[placeholder = '* Имя']"]
    surname_field = [By.CSS_SELECTOR, "[placeholder = '* Фамилия']"]
    adress_field = [By.CSS_SELECTOR, "[placeholder = '* Адрес: куда привезти заказ']"]
    metro_field = [By.CSS_SELECTOR, "[placeholder = '* Станция метро']"]
    phone_field = [By.CSS_SELECTOR, "[placeholder = '* Телефон: на него позвонит курьер']"]

    def __init__(self, driver):
        self.driver = driver
    def test_name(self):
        self.driver.find_element(*self.name_field).send_keys('12123')
        sleep(3)


driver = webdriver.Chrome()
driver.get()