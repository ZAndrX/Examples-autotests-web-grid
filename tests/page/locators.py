from selenium.webdriver.common.by import By


class BankingProjectLoginPage:
    button_customer_login = (By.CSS_SELECTOR, 'button[ng-click="customer()"]')
    button_bank_manager_login = (By.CSS_SELECTOR, 'button[ng-click="manager()"]')


class BankingProjectCustomerPage:
    form_select_user = (By.CSS_SELECTOR, '#userSelect')
    button_login = (By.CSS_SELECTOR, 'button[type="submit"]')

    def __init__(self, name):
        self.option_user_from_dropdown = (By.XPATH, f'//option[contains(text(), "{name}")]')


class BankingProjectAccount:
    balance = (By.CSS_SELECTOR, '.center>strong:nth-child(2)')
    button_transactions = (By.CSS_SELECTOR, 'button[ng-click="transactions()"]')
    button_deposit = (By.CSS_SELECTOR, 'button[ng-click="deposit()"]')
    button_withdrawl = (By.CSS_SELECTOR, 'button[ng-click="withdrawl()"]')
    input = (By.CSS_SELECTOR, 'input[type="number"]')
    button_submit = (By.CSS_SELECTOR, 'button[type="submit"]')


class BankingProjectTransactions:
    table = (By.CSS_SELECTOR, ".table")
    table_headers = (By.CSS_SELECTOR, ".table>thead>tr:nth-child(1)>td")
