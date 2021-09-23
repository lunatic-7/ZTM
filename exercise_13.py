# lambda function (Exercise)

# 1) Square the numbers
my_list = [5,4,3]

print(list(map(lambda item: item ** 2, my_list)))

# 2) List sorting (sort acc. to second no. of the tuples, lowest to highest.)
a = [(0,2), (4,3), (10,-1), (9,9)]

# a.sort() # This will sort acc. to 1st term of each tuple.

a.sort(key=lambda x: x[1]) # This means in a tuple which is x here, we have to consider [1] means 2nd term of each.
print(a)

