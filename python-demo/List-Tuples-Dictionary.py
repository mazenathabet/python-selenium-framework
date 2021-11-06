# lists is more like arrays in any another programming languages
# - List -> ordered sequence of some data vales in [ ]
# list in python can have different data types together
# Lists Use -> [ ]
values = [1, 2, 3.4, "mazen", 1000, True]
print(type(values))
print(values)
print(values[0])
print(values[1])
print(values[2])
print(values[3])
print(values[4])
# print(values[5]) will return error -> list index out of range
# print last index
print(values[-1])  # 1000
# if i want to get sub of values in the middle from 1 to before the 3 index
print(values[1:3])  # 2,3.4
# if i want to insert new value in the list in 4th index
values.insert(4, "ahmed")
print(values)
# to add value in the end of the list
values.append("end")
print(values)
# update the value on specific index
values[3] = "MAZEN"
print(values)
# delete the first index
del values[0]
print(values)
#################################################################
# Tuples are the same as Lists but they are IMMUTABLE and if we set the values we CAN NOT modify  them
# Tuples Use -> ( )
val = (1, 4.5, "mazen", 2, True)
print(type(val))
print(val)
print(val[1])
print(val[1:4])
# val[1] = 2 # returns -> tuple' object does not support item assignment
########################################################################################################
# Dictionary is key value pair in java we call it hashmap
# Dictionary Use -> { }
# there is no specific rule of which comes first but we can assign the key as string or int {key:value}

Dict = {"fName": 1, 2: "lName", "age": True, "c": "d"}

print(type(Dict))
print(Dict)
# print specific value using the key
print(Dict[2])
print(Dict["age"])
print(Dict["c"])
print(Dict["fName"])

# add dictionary data at run time
dict = {}  # empty dictionary
dict["firstname"] = "Mazen"
dict["lastName"] = "Ahmed"
dict["age"] = 29
dict["gender"] = "male"

print(dict)
print(dict["firstname"])
print(dict["lastName"])
print(dict["age"])
print(dict["gender"])
