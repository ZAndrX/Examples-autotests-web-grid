import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    capabilities = {
        "browserName": "chrome"
    }
    browser = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=capabilities
    )

    yield browser
    browser.close()
    browser.quit()
