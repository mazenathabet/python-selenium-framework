# If Statement
greeting = "good morning"
if greeting == "good morning":
    print("True")
else:
    print("condition not matches")
print("string out of the if statement")
############################################
a = 3
if a > 2:
    print("true")
else:
    print("false")
#############################################
# Loops
# iterate over a list
obj = [2, 3, 4, 12, 100]
for index in obj:
    print("{} {}".format("value is ", index))
    print(index + 1)
    print(index * 5)

# sum of first natural numbers 1+2+3+4+5 = 15
# if we set range it will iterate over range(i,j) -> it will go until item j-1
# it will print from 1 to 5
# summation = 0
# summation = 0+1 = 1
# summation = 1+2 = 3
# summation = 3+3 = 6
# summation = 6+4 = 10
# summation = 10+5 = 15
summation = 0
for j in range(1, 6):  # in java -> for(i=0;i<5;i+=)
    summation = summation + j
    print(summation)
print("************************")
for k in range(1, 10, 2):  # in java -> for(i=0;i>10;i+2) -> output 1,3,5,7,9
    print(k)
print("************************")
for i in range(10):  # it will print from 0 index to i-1
    print(i)
