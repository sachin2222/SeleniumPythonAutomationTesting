import pytest


@pytest.mark.smoke
# @pytest.mark.xfail   it will not Reported whatever the test case status is.
def test_fourthTestCase():
    print("Fourth Test Method")
