from selenium.webdriver.common.by import By


class BankingProjectLoginPage:
    button_customer_login = (By.CSS_SELECTOR, 'button[ng-click="customer()"]')
    button_bank_manager_login = (By.CSS_SELECTOR, 'button[ng-click="manager()"]')


class BankingProjectCustomerPage:
    form_select_user = (By.CSS_SELECTOR, '#userSelect')
    button_login = (By.CSS_SELECTOR, 'button[type="submit"]')
