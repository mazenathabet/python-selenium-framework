# this is a comment line
# to formal CTRL+ALT+ENTER

# variables in python don't have return type
# you don't need to mention the data type when declaring the variables

Str = "mazen"  # string
Int = 3  # int
Float = 0.2  # double
Boolean = True  # boolean
print(Str)
print(Int)
print(Float)
print(Boolean)

# you can assign multiple variables in one line even if they are different data types
b, c, a, d = 1, 5.6, "String", True
print(b)
print(c)
print(a)
print(d)

# if you want to print string and int together in other programming languages it cant be done
# with concatenating the string and int like that -> print("value is " + z) but in python there is another way
z = 10
a = "string"
Float = 0.3
Boolean = True
# this is the way to concatenate 2 different data types in python
"{} {}".format("value is", z)
print("{} {}".format("value is", z))
# to know the variable data type we use this method
print(type(z))
print(type(a))
print(type(Float))
print(type(Boolean))

# you can check all the python data type from this url -> https://www.w3schools.com/python/python_datatypes.asp
# - Numeric
# int -> 20
# float -> 20.5
# complex -> 1j
# - String -> str
# - List
# - Tuple
# - Dictionary
