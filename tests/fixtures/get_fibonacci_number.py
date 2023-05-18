import pytest
from ..tools.generate_date import generate_fibonacci_number


@pytest.fixture(scope="function")
def get_fib(request):
    fib = int(request.config.getoption("fib"))
    return generate_fibonacci_number(fib)
