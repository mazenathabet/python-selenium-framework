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

import pytest


# if i want to run the fixture only once before the class and not before each test case
# if there is no scope so it will be like = Before/AfterMethod
# we just edit the scope of it = Before/AfterClass in Java

@pytest.fixture(scope="class")
def setup():
    print("i will be executed first")
    yield
    print("i will be executed last")


@pytest.fixture()
def data_load():
    print("user profile data is being created")
    return ["mazen", "ahmed", "mazenathabet@gmail.com"]


@pytest.fixture(params=[("chrome", "mazen", "ahmed"), ("firefox", "male"), "edge"])
def cross_browser(request):
    return request.param
