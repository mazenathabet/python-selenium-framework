fruits = ["apple", "orange", "pears", "cherries", "grapes"]

for fruit in fruits:
    print(f'Would you like {fruit} ?')
    print('Would you like {} ?'.format(fruit))
    print("{} {}".format("The fruit is ", fruit))

for number in range(1, 11):  # 1 is starting number , 11 is the ending number and is not included 'will print 1 to 10'
    print(f'The number is {number}')

temp_f = 40
while temp_f > 32:
    print(f'The water is {temp_f} degrees')
    # temp_f -= 1
    temp_f = temp_f - 1
"""
Loop control
Break 
end the loop ,go to the next statement in the program (outside the loop) 
Continue 
skips current part of the loop, moves to the next part of the loop
Pass
skips any part of the loop where "pass" appears, best used for testing code 

"""
temp_f = 40
while temp_f > 32:
    print("The water is {} degrees.".format(temp_f))
    temp_f -= 1
    if temp_f == 33:
        break
        # the line when temp_f is 33 the loop will break
for number in range(1, 11):
    if number == 7:
        print("We're skipping number 7.")
        continue
    print('This is the number {}.'.format(number))
    # the line when number is 7 will be skipped and move to the next line
for number in range(1, 11):
    if number == 3:
        pass
    # the line when number is 3 will be passed and not executed
    else:
        print("The number is {}.".format(number))

on = True
off = False
