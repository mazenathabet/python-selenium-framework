# any pytest file should start with test_ or end with _test
# pytest method names should start with test_
# any code should be wrapped in method only
# to run the test in cmd go to the path and type py.test
# or py.test -v for more info in the results
# or py.test -v -s to see the printed data in the console
# run specific file from CMD py.test test_demo1.py -v
# -k stands for method name execution, -s logs in output, -v stands for more info
# run test cases if only they have "credit_card" text in the method name -> py.test -k credit_card -v -s
# marks in pytest are like tags in cucumber -> py.test -m smoke -v -s
# you can mark ( tag ) tests @pytest.mark.smoke and then run with -m smoke -v -s
# you can skip tests with the @pytest.mark.skip
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_first_program():
    msg = "hello"
    assert msg == "hi", "Test failed because strings do match"


@pytest.mark.xfail
def test_second_credit_card(setup):
    a = 4
    b = 6
    assert a + 2 == 6, "addition do not match"
    print("im in the test demo 1")


def test_cross_browser(cross_browser):
    print(cross_browser)
