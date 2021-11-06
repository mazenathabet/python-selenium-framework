# Inheritance that my child class can have all the properties and method that are in the parent class and use them
from OOP import Calculator
class ChildClass(Calculator):
    num3 = 200
    
    def __init__(self):
        Calculator.__init__(self, 2, 3)

    def complete_data(self):
        return self.num3 + self.num1 + self.multiply_nums()  # num3-> 200, num1->100,multiply->2*3+100 =106 ->406

child = ChildClass()
print(child.complete_data())
