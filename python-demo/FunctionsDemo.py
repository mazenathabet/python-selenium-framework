# In Python or any other programming language, Function is group of related statements that perform a specific task
# keyword for functions is def
# a function declaration
def greet_me():
    print("Good morning")
# calling the function
greet_me()
##############################
# Parametrized function
def send_hi(name):
    print("Good Morning " + name)
send_hi("Mazen Ahmed")
################################
def add_integers(a, b):
    print(a + b)
add_integers(10, 5)
###############################
def multiply_integers(a, b):
    print(a * b)
multiply_integers(10, 5)
##############################
# with return the value
def multiply_integers(a, b):
    return a * b
print(multiply_integers(2, 3))
