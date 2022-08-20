"""
 lists is more like arrays in any another programming languages
 List -> ordered sequence of some data vales in [ ]
 list in python can have different data types together
 can contain other collections ( lists, dictionaries, tuples) as list items
 mutable ( items can be added, removed, changed)
 maintain order ( can use index to find an item)
 Lists Use -> [ ]

    Methods to work with lists :

    append() - to add a new item to the list
    extend(another list) - to extend a list with another list
    remove(exact item match) - to remove the item with the exact name provided
    pop(index) - to remove an item with a specific index - index starts with zero in python
    pop(-1) - to remove the last item in the list - negative indexing -1 = last one , -2 = second last item
    sort() - sort method is only working with lists with liked type like int or strings
        and if we try to sort a mixed list we will get an error ( not supported between instances of 'int' and 'str')
        integers and float numbers can be sorted together with no error
    print("apple" in fruits) - will return true if the fruits list has "apple"
    and false if it doesn't have "apple"
    count() - will return with the count of specific item in the list and 0 if the list doesn't have the item
    index() - will return the index of the specified item

"""
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
# if I want to get sub of values in the middle from 1 to before the 3 index
print(values[1:3])  # 2,3.4
# if I want to insert new value in the list in 4th index
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
# Tuples are the same as Lists, but they are IMMUTABLE and if we set the values we CAN NOT modify  them
# Tuples Use -> ( )
val = (1, 4.5, "mazen", 2, True)
print(type(val))
print(val)
print(val[1])
print(val[1:4])
# val[1] = 2 # returns -> tuple' object does not support item assignment
########################################################################################################
"""
Dictionaries

Dictionary is key value pair in java we call it hashmap
Dictionary Use -> { } 
there is no specific rule of which comes first but we can assign the key as string or int {key:value} 
mutable - can be changed 
maintain order
curly braces contain keys and values keys and values separated by a colon 
and each other key value pair are separated by a comma 
    Methods to work with dictionary :
    get("key") - return the value of one of the keys in the dictionary
    items() - list the key,value in the dic to a ordered list 
    keys() - return all the keys in the dic
    popitem() - removes the last item in the dic
    update(dic) - update first dic with another dic
    
"""
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
# dict = {"firstname": "Mazen", "lastName": "Ahmed", "age": 29, "gender": "male"}
dict["firstname"] = "Mazen"
dict["lastName"] = "Ahmed"
dict["age"] = 29
dict["gender"] = "male"

print(dict)
print(dict["firstname"])
print(dict["lastName"])
print(dict["age"])
print(dict["gender"])
