# Eroor Handiling --> It allows us to continue running our program even after an error.

# So, we can have two types of errors here, one ValueEroor (when we write any letter instead of digits)
# and other ZeroDivisionError when we pass 0 for age. So, to prevent them we are gonna use Try and Except.

while True: # So, this is necessary to prompt user again for age, after he errors the programm.
    try:
        age = int(input('Tell me your age, I\'ll divide it by 5! '))
        print(100/age)
        # raise Exception('Hey cut it out!!!') # Like this we can error out our programm. We don't use it much often. 
    except ValueError:
        print('Please enter a number!')
    except ZeroDivisionError:
        print('Please enter a number greater than 0!')
    else:
        print('Thank you!')
        break # This break is necessary here, to break the program, after user enters a valid value.
    finally: # This finally will get printed always, It is sometimes useful to detect how many times
        print('finally you are done!') # a user tried to log in etc.


def add(num1, num2):
    try:
        return num1/num2
    except (TypeError, ZeroDivisionError) as err: # We can write errors together like this as well,
        print(f'Ooops! {err}') # This as err will describe the error itself in a good way, It isn't
# necessary to write err only, we can write anything in place of err, it's just a notation we usually use.
print(add(1, '2'))