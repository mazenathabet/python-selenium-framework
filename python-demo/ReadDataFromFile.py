# open() method is to open any text file with the path of the file as parameter
# if the class and the text file in the same location so just pass the name of the file
# if the class and the text file arent in the same location just pass the complete path where exactly this file located
# file = open('textfile.txt')
# as a good practice anytime you open the file make sure to close it after finishing with it
# because it may lead to memory leaks due to open up multiple files -> file.close()
# read method to read all the contents of the file -> print(file.read())
# print(file.read(14)) -> to read the first 14 letters
# read one single line at a time -> print(file.readline())
#############################################################
# print line by line using readLine method
file = open('textfile.txt')
line = file.readline()
while line != "":  # exit the loop only the readLine method reads blank line it means we are at the end of the file
    print(line)
    # it will store the lines data in teh line variable until it is blank and the condition is false
    line = file.readline()
file.close()
#############################################################################
# another way to read all the contents of a file
file2 = open('file2.txt')
# it will store all the lines in a list ->['dog\n', 'cat\n', 'elephant\n', 'monkey\n','horse']
# and iterate over each line of the lines and print it
LinesList = file2.readlines()
for line in LinesList:
    print(line)
file2.close()
