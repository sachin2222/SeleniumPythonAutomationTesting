import pytest


@pytest.fixture(scope="class")
def setup():
    print("fixture setup")
    yield
    print("last execution steps")


# data-Driven Testing
@pytest.fixture()
def data():
    return [1, 2, 3, 4, 5]


@pytest.fixture(params=[("sachin", "sharma"), "Python-Automation Tester"])
def user_info(request):
    return request.param
