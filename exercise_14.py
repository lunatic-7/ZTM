# Find Duplicates (Exercise) Using Comprehension.

# Check for duplicates in list and print them in a list.

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates: # This is imp. to not print b and n twice in output.
            duplicates.append(value)
print(duplicates)

# Now we have to do this using list comprehension.

duplicates1 = list(set([x for x in some_list if some_list.count(x) > 1 ])) # So, I can understand the inside code,
# but it will give the repeteted value so to prevent it we use function set then it removes duplicate value, and 
# after that we again change it into a list, bc we want a list in final output.
print(duplicates1)