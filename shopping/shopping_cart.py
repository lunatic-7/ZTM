# The shopping folder in which this module is stored is called package. A package is where
# we can store a large amount of modules.

print(__name__) # This wil tell the location or name of this modules, in the file in which it is 
# being imported.

def buy(item):
    cart = []
    cart.append(item)
    return cart