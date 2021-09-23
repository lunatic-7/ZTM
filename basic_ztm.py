                                 #       PART (1) BASIC

# Fundamental data types

# int => these mean simply integers. eg 2, 10, 99, 9823982 etc.
# float => these mean decimal numbers. eg 2.8, 637.0809, 0.1 etc.

# By writing type, it gives us the type of resultant. Python also calc.
# like us it first solve the bracket eg 2+4 = 6 and now it tells abt.
# the type of 6. It is integer (int).
print(type(2 + 4)) # this = 6 (So, it is an int.)
print(2 - 4)
print(2 * 4)
print(type(2 / 4)) # this = 0.5 (So, it is a float.)
print(type(2 + 0.5)) # int + float = float
print(type(2.7 + 0.9)) # float + float = float
print(2 ** 4) # this means 2 ki shakti 4
print(5 / 4)  # this is division but it doesn't get rounded off.
print(5 // 4) # this is division and gets rounded off.
print(6 % 4) # this gives remainder

# Math functions

print(round(2.3)) # round func. means round off
print(round(2.7))
print(abs(-77)) # this abs function simply act as mode.

# Operator precedence (Kya pehle hoga like BODMAS)

# Python follows PEMDMAS
# (), **, *, /, //, %, +, -
print((2 + 3) * 3 + 2)

# Just like int and str there is a function called bin(). It means binary.
# It returns the binary version of a number.

print(bin(7)) # It will be 0b111
# Let's convert this bin back to int.
print(int('0b111', 2)) # 2 represents the base, it means base 2.

# Variables = It is just a name (whatever name we assign) in which we can
# store some data.

age = 190
user_age = 190/4
print(user_age)

# Some general convention of varible.

# 1. snake_case
# 2. start with lowercase or underscores
# 3. letters, numbers, underscores
# 4. case sensitive
# 5. don't overwrite key words

# Constants =  If we write a variable in UPPERCASE it is reffered to as constant.
# Although we can overwrite them but it's not a good practise.

ME = "wasif"
print(ME)

a,b,c = 1,2,3 # just an another way to store a variable.
print(a)
print(b)
print(c)

# Statement and Expression

iq = 100
user_iq = 100/4
print(user_iq)

# So, here 100/4 is an expression. A Expression is which gives us a value in return.
# And user_iq = 100/4 is an statement. A Statement is an entire line of code,
# which performs some sort of action.

# Augmented assignment order =  It is just a short-hand of writing a code.  Eg:

some_value = 7
# some_value = some_value + 3 # This isn't a good practise.
some_value += 3 # this is good practise.
print(some_value)

# Strings
# Anything stored in a 'single quote', "double quote" or '''three single quotes'''

user_name = "Wasif"
user_name_2 = 'Nadeem'
long_string = '''
WOW
O O
---
''' # triple single strings are often used for long codes.
print(long_string)

# String concatenation = It is just addition of strings.

print("hello" + " " + "Wasif")

# Type conversion = It is just conversion of differnt function such as str() into int()

a = str(100)
b = int(a)
c = type(b)
print(c)
# A short way to write upper code :
print(type(int(str(100))))

# Escape sequence

# To avoid quotes problems. We add \ before that, It simply tells
# whatever comes after that is a string.
# \t = this means tab.
# \n = this means new line.
weather = '\tIt\'s \"kind of\" sunny!\n Hope you have a good day!'
print(weather)

# Formatted strings =  Just a better way of string concatenation.

customer = "John"
age_1 = 77
print("hi {}. You are {} years old.".format(customer, age_1))
print("hi {1}. You are {0} years old.".format(customer, age_1)) # Here, we changed positions.
# Upper method isn't better tho.
print(f"hi {customer}. You are {age_1} years old.") # This is better method.

# String indexes

username = "wasif786"
        #   01234567     (these are just the positions of letters.)
print(username[0])
# [start:stop:stepover]
print(username[0:5])
print(username[0:7:1])
print(username[0:7:2])
print(username[::2])
print(username[-1])
print(username[::-1])

# Immutable = String indexes are immutable (it's means we can't change them.
# But we can still change the entire string. )

selfish = "01234567"
# selfish[0] = 8 # We can't just do this. IMMUTABLE
# print(selfish)
selfish = "89772728" # We still can do this.
print(selfish)

# Build-in function and Methods

greet = "hellooo"
print(len(greet))  # Here, len is a function which counts the no. of chractrs.
print(greet[:len(greet)])

# These are some methods...
quote = "to be or not to be"
print(quote.upper())
print(quote.lower())
print(quote.capitalize())
print(quote.find("be"))
print(quote.replace("be", "me"))

# Boolens (These are True or False)
# In binary 1 represents True and 0 represents False
print(bool(1))
print(bool(0))
print(bin(True))
print(bin(False))

# Lists = It is a place, where we store a set of items or information.

amazon_cart = ["notebook", "pen", "laptop", "apple"]
print(amazon_cart)

# List slicing (Same like string slicing)

print(amazon_cart[0:3])

# Unlike strings Lists are mutable
amazon_cart[0] = "gum"
print(amazon_cart)

# Here, comes an important concept.
new_cart = amazon_cart[:] # If we write like this [:], it means we are copying amazon_cart.
new_cart[0] = "printer"
print(new_cart)
print(amazon_cart)

newest_cart = amazon_cart # It we simply write this we are not copying but modfying amazon_cart as well.
newest_cart[0] = "pencil"
print(newest_cart)
print(amazon_cart)

# Matrix = It is a way to describe a 2-D list or multi-dimensional list.
# (These are often used in machine learning.)

matrix = [
        [1, 7, 3],
        [2, 0, 9],
        [7, 8, 6]
]

print(matrix[0][1]) # To print 2nd item of 1st row.
print(matrix[1][2]) # To print 3rd item of 2st row.
print(matrix[2][0]) # To print 1st item of 3rd row.

# List Methods

basket = [1,2,3,4,5,6,7]
print(len(basket)) # it prints the actual length (human length).

# adding

new_list = basket.append(100) # Append adds anything in the end of a list.
print(basket) # IMP. Append does's produce a value. It just changes in place
print(new_list) # So, this gives NONE

new_list_2 = basket.insert(4, 70) # We can insert a value anywhere in a list.
print(basket)
print(new_list_2) # Same case with insert.

new_list_3 = basket.extend([60, 70]) # It just extends our list.
print(basket)
print(new_list_2) # Same case with extend.

# removing

new_list_4 = basket.pop() # It removes anything from end.
basket.pop(0) # It removes according to index as well.
print(basket)
print(new_list_4) # It gives us the removed value.

new_list_5 = basket.remove(5) # It takes the value which we wnat to remove.
print(basket)
print(new_list_2) # Same case with remove.

new_list_6 = basket.clear() # It empties our list.
print(basket)
print(new_list_6) # Same case with clear.

storage = ['a', 'b', 'x', 'c', 'd', 'e', 'd']
print(storage.index('d')) # It's just tells first position of d.
print(storage.count("d")) # It tells how many times an item occurs in a list.

print('x' in storage) # It is True
print("i" in "Hi i am here.") # It is True

print(sorted(storage)) # This function arranges in alphabetical order.
# This makes the copy of storage. It doesn't actually modifies the storage.
print(storage) # It comes as it is.

new_storage = storage.sort() # This method arranges in alphabetical order.
# It modifies the list in place. Doesn't provide a value.
print(storage)
print(new_storage) # It gives None

new_storage_2 = storage.reverse() # It simply reverses the storage.
print(storage)
print(new_storage_2) # Same case with reverse.

print(list(range(1,100))) # To generate a list 1 to 99.

sentence = ' ' # Join is used to change a list into a string.
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'casanova', '...'])
print(new_sentence)

# list unpacking

w,x,y, *other, z = [1,2,3,4,5,6,7,8,9]
# Like this we can unpack the list however we want.
print(w)
print(x)
print(y)
print(other)
print(z)

# None = It just tells the absence of anything.

weapons = None
print(weapons)

# Dictionary =  A dictionary is unordered key value pair.

dictionary = {
        "a" : [1,2,3],
        "b" : "hello",
        "x" : True
} # Here a b and c are keys and [1,2,3] "hello" and True are their values resp.

print(dictionary)
print(dictionary["a"])
print(dictionary["a"][1]) # To access 2 from the list inside dictionary.

my_list = [
       {
        "a" : [1,2,3],
        "b" : "hello",
        "x" : True
},
        {
        "a" : [4,5,6],
        "b" : "hello",
        "x" : True
} 
]

print(my_list)
print(my_list[0]["a"][2]) # To access 3 from 1st dictionary inside list.

# When to use dictionary or list

# We will get to know that by experience but some key points are:
# A list is ordered but a dictionary is unordered.
# A dictionary can store up a large amt. of data than a list.

yay = {
        123 : [1,2,3],
        True : 'hello',
        'unit' : 'okay',
        'bg' : 'b+'
        # {"hi"} : True # We can't use a list as a key for dictionary.
        # bc lists are mutable and dictionary keys don't want to be mutable.
}

print(yay)

# Dictionary methods

# Let's say we don't know if a keyword exists in a dictionary or not. eg
# print(yay['age']) # This will give an error as age keyword doesn't exists
# in yay. And we don't want errors. So, we will use get method.

print(yay.get('age', 70)) # So, here we use get it will see if age exists in yay 
# or not and if not it will return the default value, which we have set to 70 here.

# Just an another way to create dictionary (not often used)

user = dict(name = 'johncena')
print(user)

# Another way to check if a key or value exists in a dictionary or not.

print(123 in yay.keys())
print('hello' in yay.values())

yay2 = yay.copy() # Here we copied yay in yay2
print(yay2)
yay.clear() # It clears the dictionary
print(yay)

print(yay2.pop(123)) # It gives value of popped key and it removes that key and value.
print(yay2)
print(yay2.popitem()) # It randomly pops any item from the dictionary.

print(yay2.update({'bg' : 'O-'})) # So, it has updated bg to O-
print(yay2)

# Tuple = Tuples are nothing just immutable lists.
# So, why tuple when we have list, So, as we can't change a tuple so it is
# more secure and more predictable and above all it works faster than a list.

my_tuple = (1,2,3,4,5,5)
print(3 in my_tuple) # yes, we can do this
print(my_tuple[0]) # We can also do this
# my_tuple[1] = 7 # This will give an error as tuples are immutable.

# Tuple has only two methods, count and index
print(my_tuple.count(5)) # It will count numbers of times 5 occur.
print(my_tuple.index(3)) # It will tell position of 3
print(len(my_tuple)) # To see length of our tuple.

# Set = A set is an unordered collection of unique objects.

my_set = {1,2,3,4,5,5}
print(my_set) # It won't print that extra 5.
my_set.add(100) # This will be added
my_set.add(3) # But this won't as it already exists.
print(my_set)

# print(my_set[0]) # This will give an error bc set don't support indexing.
new_set = my_set.copy()
print(new_set)
my_set.clear()
print(my_set) # Only this will be cleared not the copy of it.
print(new_set)

yo = [1,2,3,4,5,5]
print(set(yo)) # to change a list into a set.

# Methods in sets =  They are quite similar like vein diagrams.

i_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

print(i_set.difference(your_set)) # It simply tells the difference in sets.
print(i_set.intersection(your_set)) # It simply gives intersection.
print(i_set & your_set) # Just an another way to write intersection.
print(i_set.union(your_set)) # It simply gives union.
print(i_set | your_set) # Just an another way to write union.
print(i_set.isdisjoint(your_set)) # This simply check if there is nothing in common.
print(i_set.issubset(your_set)) # This check if i_set is subset of your_set.
print(i_set.issuperset(your_set)) # This check if i_set is superset pf your_set.
i_set.difference_update(your_set) # difference_update permenantly modifies the set unlike difference.
print(i_set)

# Conditional logic

is_old = True
is_licenced = True
# As both are true if part will be printed.
if is_old and is_licenced:
        print("You are old enough and you have licence as well! YAY!")
else:
        print("Sorry, you can't drive.")

print('okoko')

# Truthy and Falsy

# All values are considered "truthy" except for the following, which are "falsy":

# None
# False
# 0
# 0.0
# 0j
# decimal.Decimal(0)
# fraction.Fraction(0, 1)
# [] - an empty list
# {} - an empty dict
# () - an empty tuple
# '' - an empty str
# b'' - an empty bytes
# set() - an empty set
# an empty range, like range(0)
# objects for which
# obj.__bool__() returns False
# obj.__len__() returns 0

is_old_enough = '70'
is_experienced = 'yes'
# As both are truthy value if part will be printed.
if is_old and is_licenced:
        print("You are old enough and you have licence as well! YAY!")
else:
        print("Sorry, you can't drive.")

# Ternary operators (It is just a shorcut of writing if elif and else statements...)

# condition_if_True if condition else codition_if_False

is_friend = False
can_message = "message allowed!" if is_friend else "cannot message."
print(can_message)

# Logical operators
# (<, >, ==, <=, >=, != and, or, not) These are some often used logical operators.

print(3 < 2)
print(3 > 2)
print(3 == 2)
print(2 >= 2)
print(2 >= 3)
print(3 != 2) # This means not equal to.
print(not(True))
print(not(False))
print(not(1 == 1)) # As 1 = 1 so it will be True and there is a not so finally False.

# Why is it so???

print("a" > "b") # It is False
print('a' > 'A') # It is True

# It is because of ASCII Table, ASCII (Listeni/ˈæski/ ass-kee),
# abbreviated from American Standard Code for Information Interchange,
# is a character encoding standard. ASCII codes represent text in computers,
# telecommunications equipment, and other devices.
# Most modern character-encoding schemes are based on ASCII,
# although they support many additional characters.
# when comparing characters using the < or > Python converts it to an integer.
# To check ASCII values of chr :

print(ord('a')) # 97
print(chr(97)) # a
print(ord('b')) # 98
print(chr(98)) # b
print(ord("A")) # 65
print(chr(65)) # A

# is vs ==

print(True == 1) # True is Truthy and 1 is also Truthy so True
print('1' == 1) # Str and int aren't equal. False
print([] == 1) # [] is falsy and 1 is Truthy so False
print (10 == 10.0) # float changes to int and they are equal so True
print([] == []) # Both are Falsy so True

# Unlike ==, is literally sees things
print(True is 1) # True isn't eq to 1 so False
print('1' is 1) # They aren't eq so False
print([] is 1) # They aren't eq so False
print (10 is 10.0) # They aren't equal so False
print([] is []) # List might be same, but they are stored in different
# places, so they will always be False.

# For loop

for item in "zero to mastery": # Here, Zero to Mastery is iterable (which will be looped)
        print(item)

for item in (1,2,3,4,5): # So, what is happening here, Python first interprets first loop,
        for x in ['a', 'b', 'c']: # and gives 1, then moves to 2nd loop and gives a, here,
                print(item, x) # it will stay in 2nd loop and finish it 1st before moving to
                # 1st loop again, bc there is no further loops. 
                # These are called nested for loop.
# The output will be like:
# 1 a
# 1 b
# 1 c
# 2 a
# 2 b
# ....... and so on...

# Iterable => list, dictionary, tuple, set, string
# Remember --> int items can't be iterated.

# Now let's iterate a dictionary

player = {
        'name' : 'Golem',
        'age' : 5007,
        'can_swim' : False
}

for item in player: # So, this will only give keys of the dictionary
        print(item)
# We will need to use some methods to get value and both as well.

for item in player.items(): # It will give a tuple of keys and values.
        print(item)

for item in player.keys(): # To get keys only
        print(item)

for item in player.values(): # To get values only
        print(item)
# Let's say we don't want tuple in return when we use items()

for key, value in player.items(): # We can do like this.
        print(key, value)

# Range = Range creates a special kind of object that we can iterate over.

print(range(10)) # print(range(0, 10)) They both are same will give same output range(0, 10)

# Range are mostly used in for loop.

for _ in range(10): # This will loop from 0 to 10
        print(_)

for _ in range(0, 10, -1): # This won't be printed as we can never reach 10 by subtracting 
        print(_) # -1 from 0.

for _ in range(10, 0, -1): # But we can do like this if we want to loop backwards
        print(_) # That -1 is necesarry here.

for _ in range(0, 10, 2): # We can do stepover like this.
        print(_) 

# This is a fast way to create lists.
for _ in range(7): # This tells the list to loop over 7 times
        print(list(range(10))) # This prints a list from 0 to 10.

# Enumerate = It is used to count the index of the item which we are looping.

for i in enumerate('hellllloooo'): # This will give a tuple of counting of charters.
        print(i)

for i, chr in enumerate("hellloooo"): # This will give them without tuple.
        print(i, chr)

for i, chr in enumerate(range(100)): # This will print a range of 100 with their index
        print(i, chr)

# Let us try to find the position of 77 tho, we know it would be 77 only.
for i, chr in enumerate(range(100)):
        if chr == 50:
                print(f"position of your chr is {i}")

# While loop

# i = 0
# while i < 50: 
#         print(i) # So, this will run an infinte loop which we never want
# bc it is potentially dangerous for our programm, it can crash our program.
# So, to prevent it from happening, we use a break statement in the end.

i = 0
while i < 50:
        print(i)
        break # Like this

# To print till 50
i = 0
while i < 50:
        i += 1
        print(i)
else: # We can use else statement as well with while loop. But else won't work if we use
        print("Your work is done!") # a break before it.

# When to use while and when to use for loop!

# While loop is powerful and we should use that when we have to loop over and over
# again, but we have to be careful with that to not to enconter an infinte loop,
# whereas for loop is more simpler to use.

my_num = [1,2,3]
for item in my_num:
        print(item)

# To get the same output from while loop, do like this

i = 0
while i < len(my_num):
        i += 1
        print(i)

# break, continue and pass

while True:
        response = input("Say something: ")
        if (response == 'bye'): # If someone type bye this infinite loop stops.
                break

i = 0
while i < len(my_num):
        i += 1
        continue # It will print nothing bc as soon as it seen continue it moves
        print(i) # back to the loop again and keeps doing that until loop ends.
        # So, it never actually reached the print statement.

my_num = [1,2,3]
for item in my_num:
        # Let's say we don't know what to do in this loop yet, we are still thinking
        # abt. it, and if we leave the loop like this, it will give an error. which 
        # we never want. So, we will use pass
        pass # Pass is useless tho, but it should be often used in for loop only.

# Functions = We create functions to call them anytime in our programm.
# It maintains our code DRY (Do not repeate same code to to call same thing.)

def say_hello(): # def means we are defining function named say_hello here.
        print("helllllllllloooooo!!!") # This gets stored in the memory of python.

say_hello() # Now, like this we can call our function anytime in our programm.
# and remember these brackets are necessary they tell interpreter to call the function.

print(say_hello) # This will tell the location of memory where show_hello is stored.

# Parameters and Arguments

# Parameters -> These are used while defining a function.
# Arguments -> These are used while calling a function.

def greet_emo(name, emoji): # here, name and emoji are parameters.
        print(f"helooooooooooo! {name} {emoji}")

# Arguments

# Positional arguments
greet_emo('Wasif', '😜')
greet_emo('😜', 'Ray') 
greet_emo('Casanova...', '😜')

# Keyword arguments (These aren't good practise)

greet_emo(emoji='😜', name='LOL')

# Default parameters

def greet_emo_2(name='Darth Lord', emoji='👿'): # here, name and emoji are parameters. 
                                           # And their values are default.
        print(f"helooooooooooo! {name} {emoji}")

# Now, If we mistakingly forget to call parameters, it won't give an Error,
# Which is pretty good. It will print the default arguments.

greet_emo_2()
greet_emo_2('Faith')

# Return

def add(num1, num2):
        num1 + num2

print(add(10, 5)) # It will give none, as we haven't returned the function yet!

def add_1(num1, num2):
        return num1 + num2

print(add_1(10, 5)) # This will give the sum
total = add_1(10, 5)
print(total)
print(add_1(10, total))
print(add_1(10, add_1(10, 5)))
print(add_1(10, add_1(10, total)))

# What is a good function?

# Should do one thing really well.
# Should return something.

def summer(num1, num2):
        def another_func(n1, n2):
                return n1 + n2
        return another_func(num1, num2)
        # These aren't going to be printed, asa we return a function it exits the function.
        return 5 
        print('hello')

total = summer(10, 5)
print(total)

# Docstring => It is just like a comment for function

def test(a):
        ''' This is a docstring, here we can provide the info. abt. what this function does,
        eg: this function tests and print param a'''
        print(a)

test('!!!')
help(test) # This help function tells us what a function do.
print(test.__doc__) # This __doc__ method works same as help function.

# Clean code 

# This isn't a clean code:
# We can clean this code like, we don't really need elif part, we can simply write else:
# return False. and if we see, we don't really need else as well, if we remove one
# indent of return False, bc this return False is only going to be printed when
# the condition is false. and finally we don't even need return True or return False,
# and if as well instead we can write return num % 2 == 0. Python interpreter will,
# itself change them to boolean
def is_even(num):
        if num % 2 == 0:
                return True
        elif num % 2 != 0:
                return False

print(is_even(50))

# This is clean code.
def is_even_cleaned(num):
        return num % 2 == 0

print(is_even_cleaned(71))

# *args --> arguments **kwargs --> keyword arguments

# def super_func(args):
        # return sum(args)

# print(super_func(1,2,3,4,5)) # So, this is gonna give an error as args can only store
# one variable but we are giving it 5.

# To accept more than one parameters we have to write like this *args

def super_func(age, *args, name = 'wasif', **kwargs):
        print(age)
        print(name)
        print(args) # let's see, so, this gives a tuple (1,2,3,4,5)
        print(kwargs) # let's see, so, this returns a dictionary, like {'no1' : 5 ...}
        total = 0
        for items in kwargs.values(): # Here, we are taking values from dictionary of kwargs.
                total += items 
        return sum(args) + total

print(super_func(17, 1,2,3,4,5, no1 = 5, no2 = 10))

# RULE = parameters, *args, default parameters, **kwargs

# Walrus operator (new feature)

a = 'hellooooooooo'

if (len(a) > 10):  # We can do this with walrus oprator as well.
        print(f"too long {len(a)} elements!")

if ((n := len(a) > 10)):
        print(f"too long {len(a)} elements!")

while ((m := len(a)) > 1): # It just defines a variable m with len(a)
        print(m)
        a = a[:-1]

print(a)

# Scope --> What variables do I have access to?
# ex: If some variable is inside a function then we can't directly call it by print.
# It's like when we create a function we create a new universe, which we haven't the 
# access of until we (print) are present in that universe.
# If some variable is outside function, then it is in global scope, we can access
# it anytime like:
imo = "not use" # This imo is in global scope
print(imo)

# def some_func():
#         hun = 100 # This isn't global scope

# print(hun) # This will give an error, bc this hasn't access to any variable named 
# hun. bc hun is inside a function we can still access it if we give an indent here.

