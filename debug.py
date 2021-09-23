# Debugging ---> Debugging is just a process of finding errors, bugs, exceptions etc,
# In our program. Remember no one is a perfect programmers, every programmers code
# have some bugs. So, to fix them we have some processes.

# Tips to reduce errors

# Use linter
# Use ide/ editors
# learn to read errors.

# Above all we also have a module which help us in debugging our code,
# It's called pdb ---> python debugger.

import pdb


def add(num1, num2):
    # print(num1, num2)  This is sometimes useful to check out errors.
    pdb.set_trace()  # This helps us to run code in our terminal, and with various commands of pdb
    return num1 + num2  # in it. We can check out the error.


print(add(2, "hhdhdhdd"))

# Now, the best method, pycharm has a pre-installed debugger in it, just click
# on debug on top and it will tell you the error.
