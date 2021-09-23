# map, filter, zip, reduce (Exercise)

from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def cap(item):
    return item.upper()

print(list(map(cap, my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, my_numbers[::-1])))
# print(list(zip(my_strings, sorted(my_numbers)))) # Can also do like this.

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def score(item):
    return item > 50

print(list(filter(score, scores)))


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def combine(comb, item):
    # print(comb, item)
    return comb + item
    

print(reduce(combine, (my_numbers + scores)))