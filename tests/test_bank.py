import time
import allure

from .page.base_page import BasePage
from .page.login_page import LoginPage

@allure.title('Проверка работы финансовых операций "Harry Potter"')
def test_transactions_customer_user(browser):
    page = LoginPage(browser)
    page.open_page('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
    page.login_customer_user_by_name('Harry Potter')
    time.sleep(5)
