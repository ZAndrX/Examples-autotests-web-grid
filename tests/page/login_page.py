import allure
from .base_page import BasePage
from .locators import BankingProjectLoginPage, BankingProjectCustomerPage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    @allure.step('Выбор авторизации клиентов')
    def select_customer_login(self):
        self.wait_clickable_element(BankingProjectLoginPage.button_customer_login).click()

    @allure.step('Выбор пользователя по имени')
    def select_user_by_name(self, name):
        self.wait_clickable_element(BankingProjectCustomerPage.form_select_user).click()
        self.wait_clickable_element((By.XPATH, f'//option[contains(text(), "{name}")]')).click()

    @allure.step('Подтверждения авторизации')
    def submit_login(self):
        self.wait_element_present(BankingProjectCustomerPage.button_login).click()

    @allure.step('Авторизация пользователя по имени')
    def login_customer_user_by_name(self, name: str):
        self.select_customer_login()
        self.select_user_by_name(name)
        self.submit_login()
