from selenium.webdriver.common.by import By


class PassportLocators:
    NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    DATE = (By.ID, "birthDate")
    ABOUT = (By.ID, "about")
    SAVE_BUTTON = (By.XPATH, "//button[@data-test='submit-button']")