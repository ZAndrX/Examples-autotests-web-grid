import pytest
from selenium import webdriver


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
