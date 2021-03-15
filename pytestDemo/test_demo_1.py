import pytest


@pytest.mark.smoke
def test_firstTestCase():
    print("First Test Method")


@pytest.mark.smoke
def test_secondTestCase():
    print("Second Test method")


@pytest.mark.skip
def test_third():
    assert "hello" == "hello", "Test Case Failed"
    print("Test Case Passed")
