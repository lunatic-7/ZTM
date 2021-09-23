print(__name__) # This wil tell the location or name of this modules, in the file in which it is 
# being imported.

def tour(*names):
    friends = []
    friends.append(names)
    return friends

def instrument(name):
    print(f"Need to collect $20 for that! {name}")