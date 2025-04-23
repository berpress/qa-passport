import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.passport_page_2 import PassportPage2
from pages.passport_page_3 import PassportPage3


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://berpress.github.io/ui-passport-demo/",
                     help="url")


@pytest.fixture(scope="session")
def passport_page(request):
    url = request.config.getoption("--url")
    # driver
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    passport_page = PassportPage2(driver)
    yield passport_page
    driver.quit()

@pytest.fixture(scope="session")
def passport_page_4(request):
    url = request.config.getoption("--url")
    # driver
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    passport_page = PassportPage3(driver)
    yield passport_page
    driver.quit()