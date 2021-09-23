import re

string = 'search this, inside of this text please! Wasif'

print("search" in string)  # This will simply give True as search exists in string.
# But with re (regular expressions) we can do a lot more.

pattern = re.compile('this')

a = pattern.search(string)  # This will give a lot info, like from which index this starts and end.
print(a)
b = pattern.findall(string)  # This will print all the occurrence of this
print(b)
c = pattern.fullmatch(string)  # This will check what we are checking fully matches with the string or not
print(c)  # which is not here.
d = pattern.match(string)  # This also doesn't, if we searched for search then it would have matched.
print(d)  # bc both line starts with search

# Visit regex101.com to know more about regular expressions.

# Regular expressions, they can be used to validate email, as well. It means to check whether someone,
# has entered a correct email or not.
# We are not gonna literally write regular expressions on our own, we usually google them.

# Email Checker

email = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

checker = input("Email: ")

e = email.search(checker)
print(e)

# Password checker

# At least 8 characters long
# contains any sort letters, numbers, &%$#
# must end with a number.

password = re.compile(r"[A-Za-z0-9&%$#]{8,}\d")  # I created this re myself from regex101.com

p_check = "Wasif&%$#7"

p = password.fullmatch(p_check)
print(p)
