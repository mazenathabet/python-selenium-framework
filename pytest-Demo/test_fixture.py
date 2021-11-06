# fixture
# fixture is more like pre condition and post conditions in junit
# we declare a function with @pytest.fixture() and then we have to call it as parameter in the test
# we want it to be executed before and after
# any code after yield -> will be executed after the test case
# results as below
# i will be executed first
# i will execute steps in fixture method
# i will be executed last
# if we want to set one file to have our fixture we need to create conftest.py file and put the method in there
# it will apply to all tests with test_  and it will apply to all the tests specific folder where we created conftest
# @pytest.fixture()
# def setup():
#     print("i will be executed first")
#     yield
#     print("i will be executed last")


import pytest

# if we want to apply the fixture to all the methods instead of passing it in every method we create a class
# and set the @pytest.mark.usefixtures("setup") and set the name of the fixture in that parameter


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixture_demo(self):
        print("i will execute steps in fixture method")

    def test_fixture_demo1(self):
        print("i will execute steps in fixture method")

    def test_fixture_demo2(self):
        print("i will execute steps in fixture method")

    def test_fixture_demo3(self):
        print("i will execute steps in fixture method")
