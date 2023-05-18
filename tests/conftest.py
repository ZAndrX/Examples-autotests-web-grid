import pytest
from selenium import webdriver
from .tools.generate_date import generate_fibonacci_number


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox or edge")
    parser.addoption('--browser_version', action='store', default='113.0',
                     help="Choose browser version")
    parser.addoption('--url', action='store', default='http://localhost:4444',
                     help="Choose url grid")
    parser.addoption('--fib', action='store', default=10,
                     help="Choose fibonacci number")


@pytest.fixture(scope="function")
def get_fib(request):
    fib = int(request.config.getoption("fib"))
    return generate_fibonacci_number(fib)


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser_version = request.config.getoption("browser_version")
    url = request.config.getoption("url")
    options = webdriver.ChromeOptions()
    options.set_capability("browserName", browser_name)
    options.set_capability("browserVersion", browser_version)
    browser = webdriver.Remote(
        command_executor=f'{url}/wd/hub',
        options=options
    )

    yield browser
    browser.quit()
