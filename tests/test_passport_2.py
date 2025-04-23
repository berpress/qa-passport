import time

from selenium import webdriver

from pages.passport_page import PassportPage
from pages.passport_page_2 import PassportPage2

URL = "https://berpress.github.io/ui-passport-demo/"

class TestPassport2:
    def test_passport_add_valid_data(self):
        """
        1. Добаваляем валидные данные
        """
        # открываем страницу
        driver = webdriver.Chrome()
        driver.get(url=URL)
        # добавляем данные
        passport_page = PassportPage2(driver)
        passport_page.add_passport(name_text="Иван",
                                   last_name_text="Иванов",
                                   date_text="11.03.2019",
                                   about_text="about")
        time.sleep(4)
        driver.quit()

    def test_passport_add_minimal_name(self):
        """
        1. Добаваляем валидные данные, имя 2 символа
        """
        # открываем страницу
        driver = webdriver.Chrome()
        driver.get(url=URL)
        # добавляем данные
        passport_page = PassportPage2(driver)
        passport_page.add_passport(name_text="Ив",
                                   last_name_text="Иванов",
                                   date_text="11.03.2019",
                                   about_text="about")
        time.sleep(4)
        driver.quit()


    def test_passport_add_invalid_name(self):
        """
        1. Добаваляем валидные данные, имя 1 символа
        """
        # открываем страницу
        driver = webdriver.Chrome()
        driver.get(url=URL)
        # добавляем данные
        passport_page = PassportPage2(driver)
        passport_page.add_passport(name_text="И",
                                   last_name_text="Иванов",
                                   date_text="11.03.2019",
                                   about_text="about")
        time.sleep(4)
        driver.quit()
