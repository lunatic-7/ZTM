import utility
# import shopping_cart  # We can't directly call this module like this, bc it is inside a package 
# (folder). To call it we need to write package's name first. like this:

import shopping.shopping_cart

# import bucket_list.wishlist.my_wishes  # We can import like this but this isn't a good practise.

from bucket_list.wishlist import my_wishes # This is a better way.

# from bucket_list.wishlist.my_wishes import *  # A short way to import all the functions +nt inside it.

# from bucket_list.wishlist.my_wishes import instrument # We can call a particular function like this as well.

# When we import any module, it simply creates a __pycache__ file, So, that whenever we call the
# function +nt inside utility. It doesn't have to go to compilation step again, bc pycache, stored
# a compiled file for us. It makes our code faster whenever we call the utility again.

if __name__ == '__main__': # Sometimes we do this, to verify whether this main file has imports 
    # from __name__

    print(utility) # This will simply give the location of utility.py
    print(utility.multiply(2,3))
    print(utility.divide(2,3))

print(shopping.shopping_cart.buy('grapes'))
# print(bucket_list.wishlist.my_wishes.tour('wasif', 'aryan', 'sahil', 'aadil', 'kartikey')) # We can
# call like this but this isn't a good practise.
print(my_wishes.tour('wasif', 'sahil', 'aryan', 'aadil', 'kartikey')) # This is a better way
print(my_wishes.instrument('guitar'))

print(__name__) # This will simply print __main__ bc, this in the main file, in which all the 
# __name__ imports have been called.

# Python Built-in modules --> Python has a lot of build in modules, which has been made for us,
# to simplify our work, and that why python is so famous as well.

# Eg, let we call a famous one random

import random

# from random import shuffle  # This is a good practise tho, to mention which method you are
# particularly calling from random, this will help any developer to see and understand our pragramm easily. 

print(random) # This will simply give the location of random in our computer, where it is installed.
print(dir(random)) # This will tell the methods, available in the random module which we can use.
# Some of them are:

print(random.random()) # This will simply give a random no, b/w 0 and 1
print(random.randint(1,10)) # This will give a random integer b/w 1,10 here.
print(random.choice([1,2,3,4,5,6,7])) # This will simply choose a random no. from the list we have given.
print(random.shuffle([1,2,3,4,5])) # This will give None, bc it doesn't changes a list permanently.
# It changes the list in place. So, The way to use it, is like this:
my_list = [1,2,3,4,5,6,7]
random.shuffle(my_list) # This will simply changes the positions of items in list, randomly.
print(my_list)

# Alias 
# import random as oulala  # We can give any name to alias eg, here, oulala, so, to call random
# anywhere, instead of random we have to type oulala there.

# Open 1.py to learn abt. one more imp. python module.

# So, Why is python so popular!
# Bc it has a large community of python developers, it is easier to understand, it is more like
# english. And above all, not only it has Python library from where we can import modules,
# We have 3rd party libraries as well, written by python developers all over the world.
# Which we can use in our programm freely. We can get them on pypi.org

# To install a 3rd party module, we can write pip install (package name) on command prompt,
# And after that we can import it and use it our programm.

# We have installed pyjokes, now we can use it.

import pyjokes

print(pyjokes.get_joke()) # We can see these calling information from pypi from where, we have
# installed this module.

# So, I have installed version 0.5.0 of pyjokes. What does these no's means???
# 1st no. which is 0 represents 'major changes'
# 2nd no. which is 5 represents 'updates'
# 3rd no. which is 0 represents 'bug fixes'
# So, we can conclude that this module, pyjokes has 0 major changes, 5 updates and 0 bug fixes.

# What is virtual environment?

# So, as we make programm, versions of modules are constantly upgrading, but sometimes some of our
# programms requires older versions to work. And it is impossible to install same module of
# different versions at a time. So, we use Virtual environments for our projects, by this,
# we can have different modules of different versions, for some specific programm.
# Pycharm already uses venv (virtual environment) but if ever we needed to install it, we can
# do it by pipenv command.

