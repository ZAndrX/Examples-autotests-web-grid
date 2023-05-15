import allure
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


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
