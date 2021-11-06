# Object oriented programming
# Classes are user defined blueprint or prototype
# Class have methods/functions and class variables, instance, constructor
class Calculator:
    num1 = 100  # class variables
    num2 = 200  # class variables

    # constructor is a method that is automatically called when you create an object of that class
    # default constructor __init__ is a keyword to create a constructor in python, the default constructor
    # is automatically called when creating an object
    # new keyword is not required as it was in JAVA
    def __init__(self, c, d):
        # these variables are instance variables and not class variables
        self.firstNum = c  # instance variable
        self.secondNum = d  # instance variable
        print("I am called automatically when object is created ")

    def add_numbers(self, a, b):
        print("adding with passed parameters")
        print(a + b)

    # YOU CAN NEVER CALL THE VARIABLES WITH ITS NAME WITHOUT SELF IN PYTHON
    def add_numbers_with_self(self):
        print("adding with self.variable")
        print(self.num1 + Calculator.num2)

    def multiply_nums(self):
        return self.firstNum * self.secondNum + Calculator.num1


cal = Calculator(10, 3)  # syntax to create object in python
cal2 = Calculator(5, 6)
cal.add_numbers(5, 10)  # calling the method
cal.add_numbers_with_self()
print(cal.multiply_nums())  # 130 because the instance variables are 10*3 and plus class variable 100
print(cal.num1)  # calling a class variable and it will always be 100 because its class variable
