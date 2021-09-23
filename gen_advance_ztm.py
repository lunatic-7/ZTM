# Generator --> Everything that is a generator is an iterable. Iterable underneath the hood uses __iter__
# method. But not everything that is iterable is a generator. A generator is a subset of iterable. eg:
# a range is a generator so iterable as well. But a list is an iterable only.

def make_list(num):
    item = []
    for i in range(num): # range is also a gennerator but it generates the no. 1 by 1 which we later append in a list.
        item.append(i * 2) # therefore it takes up a lot of memory. What if we don't want to generate such a long 
    return item # list and want some num. witout taking up so much space. We can do that with generators.

print(make_list(100))

# Yield --> yield pauses the function and comes back to it when next is called eg:

def generator_function(num):
    for i in range(num):
        yield i * 2

g = generator_function(100)
print(g) # This will simply give the location of function.
print(next(g)) # This will give the first value i = 0 which will yield 0 * 2 = 0
next(g)
next(g)
print(next(g)) # This will give 6 bc it has 4 next before it, means it will give 0,1,2,3  (3 Finally.)

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
    print(1)
    for i in range(100000000): # So, we can see here, generator range takes almost half time from list.
        i * 5
long_time()

@performance
def long_time2():
    print(2)
    for i in list(range(100000000)): # list almost takes double time of range.
        i * 5
long_time2()

# Underneath the hood of Generators

# For loop (Underneath the hood)

def special_for(iterable):
    iterator = iter(iterable)  # This iter function is used for iteration, and this can accept next function later on.
    while True:
        try:
            print(iterator)  # This will tell the path of memory of these iterable, and we can see that they are stored,
            print(next(iterator)) # In same memory.
        except StopIteration:
            break

special_for([1,2,3])

# Range function (Underneath the hood)

class MyGen():
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration

gen = MyGen(1,100)
for i in gen:
    print(i)

# Fibonacci Numbers

# F0	F1	 F2	 F3	 F4	 F5	 F6	 F7	 F8	 F9	 F10  F11	 F12   F13	 F14   F15	 F16	 F17	F18	    F19	    F20
#  0	1	 1	 2	 3	 5	 8	 13	 21	 34	 55	   89	 144   233   377   610	 987	 1597	2584	4181	6765
#                                           CALCULATION PROCESS
      #    (0+1)(1+2).................................................................(610+987).............(2584+4181)    

def fib(numbers):
    a = 0
    b = 1
    for i in range(numbers):
        yield a
        temp = a
        a = b
        b = temp + a

for x in fib(21):
    print(x)

# To store fibonacci numbers in a list.

def fib2(numbers):
    a = 0
    b = 1
    result = []
    for i in range(numbers):
        result.append(a)
        temp = a
        a = b
        b = temp + a
    return result

print(fib2(21))