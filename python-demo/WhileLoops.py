# While loops
i = 4
while i < 1:  # it will not go inside the loop because the condition is false
    print(i)
while i > 1:  # it will keep running until the condition is false if we do not put a code to make the condition false
    print(i)
    i = i - 1  # we have to make a code to make the condition false unless our loop will run forever
print("While loop execution is done ")
print("**********************************")
j = 4
while j > 1:
    if j != 3:
        print(j)
    j = j - 1
print("While loop execution is done ")
print("********************************************")
x = 10
while x > 1:
    if x == 9:  # if x equals to 9 it will stop that specific iteration and continue the rest
        x = x - 1
        continue
    if x == 3:
        break
    print(x)
    x = x - 1
print("While loop execution is done ")
print("**************************")
