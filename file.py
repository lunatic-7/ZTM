# File I/O ---> It means file Input/Output

# It means, I want you to input something from the outside world, and output something into the outside world.
# For ex. We sometimes want to write a script to input an image and output a compressed version of it.

# So, I have created a txt file and written something in it. Now we will access it.

my_file = open('test.txt')
print(my_file)  # This will simply give this file's information.

print(my_file.read())  # This will read the file, whatever written in it.
my_file.seek(0)  # 0 is just an index from where we want to start.
print(my_file.read())
print(my_file.read())  # This will give nothing, a vacant line, bc reading file is file reading,
# with cursor, asa we reach the end of reading, we have finished it now when we call it again to read
# it is already in the end. So, it just reads the vacant spaces, but however if we want our line to
# print twice we have to use a seek function. Just like in upper case.
my_file.seek(0)
print(my_file.readline())  # This reads the line one by one.
print(my_file.readline())  # This reads the line one by one.
print(my_file.readline())  # This reads the line one by one.
my_file.seek(0)
print(my_file.readlines())  # This will read all lines and put them in a list.

my_file.close()  # Just to close the file.

# Standard and better way to open a file, So, that we don't need to close it like before is:

with open('test.txt') as my_file2:  # It will simply read the file bc open has a default
    print(my_file2.readlines())  # parameter which is mode = 'r'. Just for reading.

# with open('test.txt', mode='r+') as my_file2:  # This r+ means read and write, but we don't more often
#     text = my_file2.write('Hey I m Don.')  # use this bc it overwrites all our texts.
#     print(text)

# To not to overwrite we use mode = 'a'. It means append.

with open('test.txt', mode='a') as my_file2:  # This appends whatever we write in the end. But be careful
    text = my_file2.write('Heyooooooo!')  # It will keep on appending all the time, whenever we run this file.
    print(text)

# We also have mode = 'w', for writing but it overwrites all our texts.

# Let's open a file which doesn't exist. If we try to do r+ in that file, it will give an error,
# but if we use w, it will create that txt file and write whatever we want

# with open('sad.txt', mode='r+') as my_file3:
#     text = my_file3.write(':(:(')
#     print(text)

with open('app/sad.txt', mode='w') as my_file3:
    text = my_file3.write(':(:(')
    print(text)

# How to handle file IO errors:

try:
    with open('sad.txt', mode='r') as my_file3:
        print(my_file3.read())
except FileNotFoundError as err:
    print("file doesn't exist ")

