import pytest


@pytest.mark.usefixtures("user_info")
class TestExample:

    def test_fixture_demo(self, user_info):
        print("fixture steps1")
        print(user_info)
