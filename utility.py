# We have created these modules, so that we can call them anytime, in any of our python programm, by writing
# import utility.

print(__name__) # This wil tell the location or name of this modules, in the file in which it is 
# being imported.

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2