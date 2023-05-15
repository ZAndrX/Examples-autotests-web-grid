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

    def wait_element_present(self, locator: tuple[str, str], timeout: int = 5) -> WebElement:
        """
        Ожидание элемента на странице по локатору
        :param locator: Локатор элемента
        :param timeout: Максимальное время ожидания появления элемента
        :return: Элемент найденный по локатору на странице
        """
        return Wait(self.browser, timeout).until(expected_conditions.presence_of_element_located(locator))

    def get_text(self, locator: tuple[str, str], timeout: int = 5) -> str:
        """
        Получение текста элемента
        :param locator: Локатор элемента
        :param timeout: Максимальное время ожидания появления элемента
        :return: Текст элемента
        """
        el = self.wait_element_present(locator)
        return el.text

