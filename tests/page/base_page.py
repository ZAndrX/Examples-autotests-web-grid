import allure
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.remote.webdriver import WebElement


class BasePage:
    def __init__(self, browser: webdriver.Remote):
        self.browser = browser

    @allure.step('Открытие страницы в браузере')
    def open_page(self, url: str) -> None:
        """
        Открытие страницы в браузере
        :param url: Адрес страницы
        """
        self.browser.get(url)

    @allure.step('Ожидание кликабельности элемента')
    def wait_clickable_element(self, locator: tuple[str, str], timeout: int = 5) -> WebElement:
        """
        Ожидание кликабельности элемента на странице по локатору
        :param locator: Локатор элемента
        :param timeout: Максимальное время ожидания кликабельности элемента
        :return: Кликабельный элемент найденный по локатору на странице
        """
        return Wait(self.browser, timeout).until(
            expected_conditions.element_to_be_clickable(locator)
        )

    @allure.step('Ожидание появления элемента')
    def wait_element_present(self, locator: tuple[str, str], timeout: int = 5) -> WebElement:
        """
        Ожидание элемента на странице по локатору
        :param locator: Локатор элемента
        :param timeout: Максимальное время ожидания появления элемента
        :return: Элемент найденный по локатору на странице
        """
        return Wait(self.browser, timeout).until(expected_conditions.presence_of_element_located(locator))

    @allure.step('Получение текста элемента')
    def get_text(self, locator: tuple[str, str], timeout: int = 5) -> str:
        """
        Получение текста элемента
        :param locator: Локатор элемента
        :param timeout: Максимальное время ожидания появления элемента
        :return: Текст элемента
        """
        el = self.wait_element_present(locator, timeout)
        return el.text

    @allure.step('Преобразование таблицы в словарь')
    def table_to_dict(self, locator_table: tuple[str, str], locator_headers: tuple[str, str],
                      number_first_line: int = 1) -> list[dict]:
        """
        Преобразование таблицы на страницы в словарь
        :param locator_table: Локатор таблицы
        :param locator_headers: Локатор заголовков
        :param number_first_line: Номер первой строки с данными
        :return: Лист из словаря, ключи которого соответствуют заголовкам
        """
        self.wait_element_present(locator_table)
        header_elements = self.browser.find_elements(*locator_headers)
        headers = []
        for header_element in header_elements:
            headers.append(header_element.text)

        result = []
        lines = self.browser.find_elements(locator_table[0], locator_table[1] + ">tbody>tr")
        for i in range(number_first_line - 1, len(lines)):
            row = self.browser.find_elements(locator_table[0], f"{locator_table[1]}>tbody>tr:nth-child({i + 1})>td")
            tmp_result = {}
            for j in range(len(headers)):
                tmp_result[headers[j]] = row[j].text
            result.append(tmp_result)
        return result

    @allure.step('Поиск по словарю значений в table_dict')
    def search_in_table_dict(self, table_dict, regex_dict):
        result = []
        for line_dict in table_dict:
            is_match = True
            for key_regex, value_regex in regex_dict.items():
                try:
                    if line_dict[key_regex] != value_regex:
                        is_match = False
                        break
                except KeyError:
                    is_match = False
                    break
            if is_match:
                result.append(line_dict)
        return result
