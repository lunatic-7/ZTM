# Functional Programming

# In functions unlike OOP, We store data and behaviour (function) seperately.

# Pure function --> It is those function in which if we give a specific input it would 
# give the same output always. It produces no side effects, it means it doesn't alter anything like
# variable etc, in global world.
# Pure function is good, to avoid bugs in our future programm.

# This is PURE function.
# new_list = [] # If we write new_list here, then it won't be a pure function. It may interact with the global scope.
def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    # print(new_list)  # If we write print statement then this won't be a pure function.
    return new_list
print(multiply_by2([1,2,3]))

# Some imp. functions used in functional programming.

# map, filter, zip and reduce

# map
# map(func, iterable) # writing convention of map, it loops over the iterable in the func provided.

ml = [1,2,3,4,5,6,7]
yl = [8,9,10,11,12,13,14]
tl = ['a', 'an', 'the', 'cas', 'ray', 'hey', 'alc']
def mp2(item):
    return item * 2

print(list(map(mp2, ml)))
print(ml) # and it does't modify the ml list.

# filter
# filter(func, iterable) # writing convention of filter, it loops over the iterable and filters and 
# returns it acc. to the function provided.

def only_odd(item):
    return item % 2 != 0  # This will give a boolean value.

print(list(filter(only_odd, ml)))
print(ml) # and it does't modify the ml list.

# zip
# zip(iterable, iterable, iterable, .............) # this is its writing convention. It can take 
# as many as iterables, and zips or combines them together in a tuple.

print(list(zip(ml, yl, tl)))
print(ml)

# reduce 
# It doesn't come as part of the python build-in function. So, to use it, we have to import it
# like this --> from functools import reduce
# reduce(func, data, initializer)

from functools import reduce

def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulator, ml, 0)) # So, here, 0 is the value of acc, it's initializer.
# it will run a loop of ml, and acc will start from 0 and will gets, added each time with item, and
# next time starts with the added value.
print(ml)

# lambda expression --> These are good for functions which we only need to use once.
# Sometimes lambda is also known as anonymous function.

# lambda param: action(param) # Writing convention.

lamda_list = [1,2,3,4,5]

print(list(map(lambda item: item * 3, lamda_list))) # To multiply each item with 3
print(list(filter(lambda item: item % 2 != 0, lamda_list))) # This will print odd values.
print(reduce(lambda acc, item: acc + item, lamda_list)) # This will give the total of the list.

# list, set and dictionary Comprehensions --> It is just a short way f acting upon these items. eg.

my_list = []

for chr in 'hellooo':
    my_list.append(chr)

print(my_list)

# To write this upper code in one line, we use list comprehensions like this:

# list comprehensions

my_list2 = [chr for chr in 'hellooo']
print(my_list2) # to append h, e, ....... in my_list2

my_list3 = [num for num in range(100)] # Print a list of 0 to 99
print(my_list3)
my_list4 = [num ** 2 for num in range(100)] # Each raise to the power too
print(my_list4)
my_list5 = [num ** 2 for num in range(100) if num % 2 == 0] # to print only evens for my_list4
print(my_list5)

# set comprehensions

my_list6 = {num for num in range(50)} # Just need to change bracket notation. Rest is same as list.
print(my_list6)

# dictionary comprehensions

simple_dict = {
    'a' : 1,
    'b' : 2,
    'c' : 3
}

my_dict = {k:v for k,v in simple_dict.items()}
print(my_dict)
my_dict2 = {k:v ** 2 for k,v in simple_dict.items()} # Here, values power is raised to 2.
print(my_dict2)
my_dict3 = {k:v ** 2 for k,v in simple_dict.items() if v % 2 == 0} # Print only even value pairs.
print(my_dict3)
my_dict4 = {num:num * 2 for num in [1,2,3]} # To make 1st value key and its multiplication of 2 is value.
print(my_dict4)

