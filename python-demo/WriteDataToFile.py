# write data into a file
# file = open('file3.txt')
# file.close()
# we can use this keyword instead and we will not need to close the file after the reading or writing
# we will not need the file.close() anymore
# with open('files3.txt', 'r') as file -> the file will be opened in read-mode -> by default its read-mode
# with open('files3.txt', 'w') as file -> the file will be opened in write-mode
##########################################################################
# read the file and store all the lines in list
# reverse the list
# write the reversed list back to the file
with open('file2.txt', 'r') as reader:
    content = reader.readlines()  # [dog,cat,elephant,monkey,horse]
    reversed(content)  # [horse,monkey,elephant,cat,dog]
    print(reversed(content))
    with open('file2.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
