# Functions in python acts as first class citizens. eg:

def helo():
    print('heelllooo')

greet = helo()
del helo
# print(helo())  # This will give an error bc we have deleted this helo
print(greet) # As this greet is gonna work bc our function isn't deleted.


# Higher Order Function (HOC) ---> Functions inside function is a higher order function.

def hello(func):
    func()

def greet():
    print('still here!')

print(hello(greet)) # We don't need to use brackets here to call, bc func() already call it for us.

# Decorator --> A decorator is a function that wraps another function and enhances it. By just adding @func_name to
# another function, we can add extra functionality to other function.

def my_decorator(func):
    def wrap_func():
        print('*' * 7)
        func()
        print('*' * 7)
    return wrap_func

@my_decorator
def say_helo():
    print('Hellllooo!')

@my_decorator
def by():
    print('Byeeeeee')

print(say_helo())
print(by())

# So, what is actually happening above!!!

my_decorator(say_helo()) # This is actually happening above.

# So, let's say now we have to pass parameters to our decorators.

def your_decorator(func):
    def wrap_func(*args, **kwargs):
        print('*' * 7)
        func(*args, **kwargs)
        print('*' * 7)
    return wrap_func

@your_decorator
def say_helo(greeting, emoji=':('):
    print(greeting, emoji)


say_helo('Hiiiiiii')
say_helo('Hellooo', ':)')

# Let's create a function running time calculator from decorator.

from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2 - t1} sec.')
        return result
    return wrapper

@performance
def long_time():
    for i in range(10000000):
        i * 5
long_time()