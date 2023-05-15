import time

import allure
from selenium.common import StaleElementReferenceException

from .base_page import BasePage
from .locators import BankingProjectAccount


class UserPage(BasePage):
    @allure.step('нажатие на кнопку "Deposit"')
    def select_deposit(self) -> None:
        self.wait_clickable_element(BankingProjectAccount.button_deposit).click()

    @allure.step('нажатие на кнопку "Withdrawl"')
    def select_withdrawl(self) -> None:
        self.wait_clickable_element(BankingProjectAccount.button_withdrawl).click()

    @allure.step('Ввод количества единиц для операции')
    def input_amount(self, n: int) -> None:
        time.sleep(1)
        while True:
            try:
                el = self.wait_clickable_element(BankingProjectAccount.input)
                el.send_keys(str(n))
                break
            except StaleElementReferenceException:
                time.sleep(1)

    @allure.step('Подтверждение операции')
    def submit_transaction(self) -> None:
        while True:
            try:
                el = self.wait_clickable_element(BankingProjectAccount.button_submit)
                el.click()
                break
            except StaleElementReferenceException:
                time.sleep(1)

    @allure.step('Пополнение счета пользователя')
    def deposit_account(self, n: int) -> None:
        """
        Пополнение счета пользователя
        :param n: Количество единиц для пополнения
        :return:
        """
        self.select_deposit()
        self.input_amount(n)
        self.submit_transaction()
        self.select_deposit()

    @allure.step('Вывод со счета пользователя')
    def withdrawl_account(self, n: int) -> None:
        """
        Вывод со счета пользователя
        :param n: Количество единиц для вывода
        :return:
        """
        self.select_withdrawl()
        self.input_amount(n)
        self.submit_transaction()
        self.select_withdrawl()

    @allure.step('Получение единиц баланса')
    def get_balance(self) -> str:
        """
        Получение единиц баланса
        :return: Количество единиц баланса
        """
        return self.get_text(BankingProjectAccount.balance)
