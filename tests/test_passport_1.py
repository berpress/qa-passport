import time

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://berpress.github.io/ui-passport-demo/"

class TestPassport:
    def test_passport_add_valid_data(self):
        """
        1. Добаваляем валидные данные
        """
        # открываем страницу
        driver = webdriver.Chrome()
        driver.get(url=URL)
        # находим элементы
        name = driver.find_element(By.ID, "firstName")
        last_name = driver.find_element(By.ID, "lastName")
        date = driver.find_element(By.ID, "birthDate")
        about = driver.find_element(By.ID, "about")
        btn_save = driver.find_element(By.XPATH, "//button[@data-test='submit-button']")
        # действия
        name.send_keys('Иван')
        last_name.send_keys('Иванов')
        date.send_keys('11.03.2000')
        about.send_keys('QA ABOUT')
        btn_save.click()
        time.sleep(7)
        driver.quit()

    def test_passport_add_minimal_name(self):
        """
        1. Добаваляем валидные данные, имя 2 символа
        """
        # открываем страницу
        driver = webdriver.Chrome()
        driver.get(url=URL)
        # находим элементы
        name = driver.find_element(By.ID, "firstName")
        last_name = driver.find_element(By.ID, "lastName")
        date = driver.find_element(By.ID, "birthDate")
        about = driver.find_element(By.ID, "about")
        btn_save = driver.find_element(By.XPATH, "//button[@data-test='submit-button']")
        # действия
        name.send_keys('Ив')
        last_name.send_keys('Иванов')
        date.send_keys('11.03.2000')
        about.send_keys('QA ABOUT')
        btn_save.click()
        time.sleep(7)
        driver.quit()


    def test_passport_add_invalid_name(self):
        """
        1. Добаваляем валидные данные, имя 1 символа
        """
        # открываем страницу
        driver = webdriver.Chrome()
        driver.get(url=URL)
        # находим элементы
        name = driver.find_element(By.ID, "firstName")
        last_name = driver.find_element(By.ID, "lastName")
        date = driver.find_element(By.ID, "birthDate")
        about = driver.find_element(By.ID, "about")
        btn_save = driver.find_element(By.XPATH, "//button[@data-test='submit-button']")
        # действия
        name.send_keys('И')
        last_name.send_keys('Иванов')
        date.send_keys('11.03.2000')
        about.send_keys('QA ABOUT')
        btn_save.click()
        time.sleep(7)
        driver.quit()
