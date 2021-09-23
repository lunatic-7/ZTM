# Function (Exercise)

def highest_even(li):
    evens = []

    for item in li:
        if item % 2 == 0:
            evens.append(item)
    # Take care of the indentation here, it should be with for.
    return max(evens)


print(highest_even([2, 10, 3, 4, 8, 11]))
