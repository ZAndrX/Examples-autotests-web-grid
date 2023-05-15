import time
from .page.base_page import BasePage


def test_open_page(browser):
    page = BasePage(browser)
    page.open_page('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
    time.sleep(5)
