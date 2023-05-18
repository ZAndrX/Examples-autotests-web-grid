import allure
from .page.login_page import LoginPage
from .page.user_page import UserPage
from .tools.generate_date import generate_fibonacci_number
from hamcrest import assert_that, equal_to


@allure.title('Проверка работы финансовых операций "Harry Potter"')
def test_transactions_customer_user(browser):
    """
        1) Использовать Python/Java, подключить библиотеку Selenium Webdriver;
        2) С помощью Selenium открыть браузер, открыть страницу страницу
        https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login;
        3) Авторизоваться пользователем «Harry Potter»;
        4) Вычислить N-е число Фибоначчи, где N - это текущий день месяца + 1.
        Пример: сегодня 08.02.2023, 9-е чисто Фибоначчи равно 21;
        5) Выполнить пополнение счета (Deposit) на сумму равную вычисленному в
        п.4 числу;
        6) Выполнить списание со счета (Withdraw) на сумму равную вычисленному
        в п.4 числу;
        7) Выполнить проверку баланса - должен быть равен нулю;
        8) Открыть страницу транзакций и проверить наличие обеих транзакций;
        9) Сформировать файл формата csv, в который выгрузить данные о проведенных транзакциях;
        10) Оформить сформированный файл как вложение к отчету allure.
    """
    browser, n = browser
    page = LoginPage(browser)
    page.open_page('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
    page.login_customer_user_by_name('Harry Potter')

    page = UserPage(browser)
    fib = generate_fibonacci_number(n)
    page.deposit_account(fib)
    page.withdrawl_account(fib)
    assert_that(page.get_balance(), equal_to('0'))

    transactions = page.get_table_transactions()
    page.transactions_is_present(transactions, fib)

    page.attach_transactions(name_file='transactions.csv', table_dict=transactions)
