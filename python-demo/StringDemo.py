name = "Mazen Ahmed"
gender = "male"
age = 29
first_name = "Mazen"
# print any char in the string starts with zero index
print(name[1])  # char with index 1 -> a
# print sub-String [starts from index:before index]
print(name[0:5])  # Mazen
# concatenate 2 strings
print(name + " is " + gender)
# concatenate int and string
print("{} {} {}".format(name + " is", age, "Years old"))
# check if a string is present in another string or not ( contains )
print(first_name in name)  # it is bool and returns true -> because Mazen Ahmed contains Mazen
# split string with the " " white space between them and put the parts into a list
var = name.split(" ")  # returns a list
print(var)
print(var[0])  # Mazen is index 0 in the list
print(var[1])  # Ahmed is index 1 in the list
# trim is basically to remove the white spaces in the beginning or at the end
# in python we use strip
str4 = "   great   "
print(str4.strip())
# remove only the beginning white spaces
print(str4.lstrip())  # L for left
# remove only the end white spaces
print(str4.rstrip())  # r for right
