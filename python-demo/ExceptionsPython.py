ItemsInCart = 0
# 2 items will be added to cart

# if ItemsInCart != 2:
#     raise Exception("products carts count not matching")
if ItemsInCart != 2:
    pass
# or you can user assertions to fail the test if the condition is not true
assert (ItemsInCart == 0)
##########################################################################
# Try , Catch
# if you writing a code and your code may fail
# but you don't want your test case to stop when you come across this failure
# you can wrap this specific code in try block , your test will be sent to catch block

try:
    with open('notExist.txt', 'r') as reader:
        print(reader.read())
except Exception as e:
    print("Some how i reached to this block because its a failure in try block")
    # to print the python exception
    print(e)
# finally -> it will run no matter if there is failure or pass in your testcases
finally:
    print("I am a finally keyword so i always run whether its a failure or pass")  # like delete all the cookies
