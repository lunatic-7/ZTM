# Some Useful Modules

from collections import Counter, defaultdict, OrderedDict

li = [1, 2, 3, 4, 5]
print(Counter(li))  # This counter simply creates a dictionary counting how many times a character
name = 'blah blah blah thinking for python'  # comes in li
print(Counter(name))  # Same counts no. of words

dictionary = defaultdict(lambda: 'not exist', {'a': 1, 'b': 2})
print(dictionary['a'])  # This will simply give value.
# print(dictionary['c'])  # This will give an error bc this key doesn't exist. So, to prevent it
# We use defaultdict function imported from collections in our dictionary and give it a default value.
print(dictionary['v'])  # Now this won't give an error.

dic = {
    'a': 1,
    'b': 2,
    'c': 3
}

dic1 = {
    'c': 3,
    'b': 2,
    'a': 1
}

print(dic == dic1)  # This will give True, as python doesn't care abt. the order of dictionary.

di = OrderedDict({
    'x': 3,
    'y': 2,
    'z': 1
})

di1 = OrderedDict({
    'x': 3,
    'z': 1,
    'y': 2
})

print(di == di1)  # This will give False, as we have used OrderedDict method for collections,
# This will only give True when the dictionary is in order.

# Some more useful modules

import datetime

print(datetime.time())  # It will simply give 00:00:00, as we haven't given any time to it.
print(datetime.time(7, 57, 2))
print(datetime.date.today())  # It will tell what today is:
