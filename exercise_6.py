# Find Duplicates (Exercise)

# Check for duplicates in list and print them in a list.

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates: # This is imp. to not print b and n twice in output.
            duplicates.append(value)
print(duplicates)