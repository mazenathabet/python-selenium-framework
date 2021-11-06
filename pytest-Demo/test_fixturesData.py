# data driven and parameterization can be done with return statements in tuple format
# when you define fixture to class only will run once before class is initiated and at the end
# for printing HTML report use -> py.test --html=report.html -v -s
import pytest


@pytest.mark.usefixtures("data_load")
class TestExampleTwo:

    def test_fixture_demo(self, data_load):
        print(data_load)
        print(data_load[0])
        print(data_load[1])
        print(data_load[2])
