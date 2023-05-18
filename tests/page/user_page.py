import time
import allure
from selenium.common import StaleElementReferenceException
from .base_page import BasePage
from .locators import BankingProjectAccount, BankingProjectTransactions
from hamcrest import assert_that, equal_to
from ..tools.allure import attach_table


class UserPage(BasePage):
    @allure.step('Нажатие на кнопку "Deposit"')
    def select_deposit(self) -> None:
        self.wait_clickable_element(BankingProjectAccount.button_deposit).click()

    @allure.step('Нажатие на кнопку "Withdrawl"')
    def select_withdrawl(self) -> None:
        self.wait_clickable_element(BankingProjectAccount.button_withdrawl).click()

    @allure.step('Нажатие на кнопку "Transactions"')
    def select_transactions(self) -> None:
        self.wait_clickable_element(BankingProjectAccount.button_transactions).click()

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

    @allure.step('Получение транзакций в словарь')
    def get_table_transactions(self) -> list[dict]:
        """
        Преобразование транзакций в словарь
        :return: Словарь с данными таблицы table_to_dict
        """
        self.select_transactions()
        self.wait_element_present(BankingProjectTransactions.table_headers)
        return self.table_to_dict(locator_table=BankingProjectTransactions.table, locator_headers=BankingProjectTransactions.table_headers)

    @allure.step('Прикрепление csv файла')
    def attach_transactions(self, name_file: str, table_dict: list[dict]) -> None:
        """
        :param table_dict: Словарь с данными таблицы table_to_dict
        :param name_file: Имя файла
        """
        attach_table(table_dict, name_file)

    @allure.step('Проверка, что транзакции произошли')
    def transactions_is_present(self, table_dict: list[dict], n) -> None:
        """
        Проверка, что транзакции произошли
        :param table_dict: Словарь с данными таблицы table_to_dict
        :param n: Количество единиц в операциях
        """
        deposit_list = self.search_in_table_dict(table_dict=table_dict, regex_dict={'Amount': str(n), 'Transaction Type': 'Debit'})
        withdrawl_list = self.search_in_table_dict(table_dict=table_dict, regex_dict={'Amount': str(n), 'Transaction Type': 'Credit'})
        assert_that(len(deposit_list), equal_to(1))
        assert_that(len(withdrawl_list), equal_to(1))
