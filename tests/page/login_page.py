import allure
from .base_page import BasePage
from .locators import BankingProjectLoginPage, BankingProjectCustomerPage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    @allure.step('Выбор авторизации клиентов')
    def select_customer_login(self) -> None:
        self.wait_clickable_element(BankingProjectLoginPage.button_customer_login).click()

    @allure.step('Выбор пользователя по имени из выпадающего списка')
    def select_user_by_name(self, name: str) -> None:
        """
        Выбор пользователя из выпадающего списка
        :param name: Имя пользователя
        """
        self.wait_clickable_element(BankingProjectCustomerPage.form_select_user).click()
        self.wait_clickable_element(BankingProjectCustomerPage(name).option_user_from_dropdown).click()

    @allure.step('Подтверждения авторизации')
    def submit_login(self) -> None:
        self.wait_element_present(BankingProjectCustomerPage.button_login).click()

    @allure.step('Авторизация пользователя по имени')
    def login_customer_user_by_name(self, name: str) -> None:
        """
        1) Выбрать авторизацию для клиентов;
        2) Выбрать пользователя из выпадающего списка;
        3) Нажать на кнопку "Login"
        :param name: Имя пользователя
        """
        self.select_customer_login()
        self.select_user_by_name(name)
        self.submit_login()
