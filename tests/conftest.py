import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox or edge")
    parser.addoption('--browser_version', action='store', default='113.0',
                     help="Choose browser version")
    parser.addoption('--fib', action='store', default=10,
                     help="Choose fibonacci number")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser_version = request.config.getoption("browser_version")
    fib = request.config.getoption("fib")
    capabilities = {
        "browserName": browser_name,
        "browserVersion": browser_version
    }
    browser = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=capabilities
    )

    yield browser, fib
    browser.close()
    browser.quit()
