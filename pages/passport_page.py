from selenium.webdriver.common.by import By


class PassportPage:
    def __init__(self, driver):
        self.driver = driver

    def add_passport(self, name_text:str,
                     last_name_text: str,
                     date_text: str,
                     about_text: str):
        name = self.driver.find_element(By.ID, "firstName")
        last_name = self.driver.find_element(By.ID, "lastName")
        date = self.driver.find_element(By.ID, "birthDate")
        about = self.driver.find_element(By.ID, "about")
        btn_save = self.driver.find_element(By.XPATH, "//button[@data-test='submit-button']")
        # действия
        name.send_keys(name_text)
        last_name.send_keys(last_name_text)
        date.send_keys(date_text)
        about.send_keys(about_text)
        btn_save.click()