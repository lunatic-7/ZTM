# This is a Password checker:

# It means it checks that if your password has ever been hacked.

# How are password get hacked?
# There are security breeches in accounts like facebook, linkedin, yahoo etc, where,
# Hackers steal a large amt. of data of emails and password, which to put into
# a dictionary. are loop then over on site like facebook to log it in.

# What is a Hash function?
# A Hash function is something that generates a 'value of fixed length' for each input that it gets.

# 1. Hash function is one way it means, eg:

# hello
# 5d41402abc4b2a76b9719d911017c592   (this is MD5 hashed version of hello)

# So, one way means if someone gets this hashed version he would never be able to find,
# what its actual value was which is hello tho.

# 2. Hash value is always same for a particular input.

# There are a lot of hash generators like MD5, SHA-1, SHA-256 etc.
import hashlib  # To convert to hash values.
import sys
import requests

# url = 'https://api.pwnedpasswords.com/range/' + 'hello'  # This is gonna give a Response [400]
# res = requests.get(url)  # Which is not good, and it is because, we simply wrote our password, instead
# print(res)  # It prefers a hashed version of password for security reasons, and even we don't give full,
# hashed password, instead we give first 5 letters of it

# url = 'https://api.pwnedpasswords.com/range/' + '5d414'  # Now this will give Response [200] which is good.
# res = requests.get(url)
# print(res)


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching {res.status_code} check the api and try again!')
    return res


def get_password_leak_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    # Check password if it exists in API response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # If we miss encode part, it will give this error.
    # TypeError: Unicode-objects must be encoded before hashing
    first5char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5char)
    return get_password_leak_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times... You should probably change it.')
        else:
            print(f'{password} was found {count} times. Carry on!')
    return 'Done Boss!'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
