pytest_plugins = [
    "tests.fixtures.get_fibonacci_number",
    "tests.fixtures.browser"
]


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox or edge")
    parser.addoption('--browser_version', action='store', default='113.0',
                     help="Choose browser version")
    parser.addoption('--url', action='store', default='http://localhost:4444',
                     help="Choose url grid")
    parser.addoption('--fib', action='store', default=10,
                     help="Choose fibonacci number")



