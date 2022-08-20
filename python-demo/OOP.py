# Object-oriented programming
# Classes are user defined blueprint or prototype
# Class have methods/functions and class variables, instance, constructor
class Calculator:
    num1 = 100  # class variables
    num2 = 200  # class variables
    """
    # constructor is a method that is automatically called when you create an object of that class
    # default constructor __init__ is a keyword to create a constructor in python, the default constructor
    # is automatically called when creating an object
    # new keyword is not required as it was in JAVA
    # __init__ method is not required BUT is generally used to send default state of object when it is created
    # The __init__ method is the first method for a class
    # The word constructor is another word that can be used to refer to the __init__ method
    # self  - self-referencing variable
    # Used to reference the object that is constructed by the init method 
    
    """
    def __init__(self, first_number, second_number):
        """
        these variables are instance variables and not class variables
        initialize attributes to be used in/available for all class methods in this class,
        and for class objects created by this class
        """
        self.first_number = first_number  # instance variable
        self.second_number = second_number  # instance variable
        print("I am called automatically when object is created ")

    def add_numbers(self, a, b):
        print("adding with passed parameters")
        print(a + b)

    # YOU CAN NEVER CALL THE VARIABLES WITH ITS NAME WITHOUT SELF IN PYTHON
    def add_numbers_with_self(self):
        print("adding with self.variable")
        print(self.num1 + Calculator.num2)

    def multiply_nums(self):
        return self.first_number * self.second_number + Calculator.num1


cal = Calculator(10, 3)  # syntax to create object in python
cal2 = Calculator(5, 6)
cal.add_numbers(5, 10)  # calling the method
cal.add_numbers_with_self()
print(cal.multiply_nums())  # 130 because the instance variables are 10*3 and plus class variable 100
print(cal.num1)  # calling a class variable, and it will always be 100 because its class variable
