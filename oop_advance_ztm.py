                                    #       PART (2) ADVANCE

# OOP (Object oriented programming) --> OOP is a paradigm, (a typical example or pattern of something; a model.)
# a way to think about our code and structure our code.
# It is like creating something (some class), that will be stored in python's memory that we can use any time,
# in our programm.

# Classes

# Making an object from a class is called instantiation, and you work with 
# instances of a class.


# classes are packages of functions that use and process built-in object types.

class BigObject: # Usually we write class in CamelCase
    # code
    pass

obj1 = BigObject() # Instanciate (To do an action)
obj2 = BigObject() # Instanciate (To do an action)
obj3 = BigObject() # Instanciate (To do an action)

print(obj1) # This will tell the memory where the object is stored.
print(type(obj1))

class PlayerCharactor:
    # Class object attribute --> This is static (fixed) this doesn't change.
    membership = True
    def __init__(self, name='anonymous', age=0):  # The self parameter is required in the method definition, self
                                                  # refers to the PlayerCharactor class and it must come first before
                                                  # the other parameters.This anonymous and 0 are default.
        if self.membership: # This will check if player has a membership. Instead self we can write
                            # PlayerCharactor as well here, as membership is static.
            
            self._name = name # Here, name and age are attributes
            self._age = age # this writing convention underscore before name and age, tells our python
                            # community that it is a private code.
    def shout(self):
        print(f"my name is {self._name}")

    def run(self):
        print("run")
        return 'done'

    @classmethod
    def adding_things(cls, num1, num2): # This cls is necessary here, otherwise it will give an error.
        return cls('Teddy', num1 + num2) # By cls we have access to our class PlayerCharactor.

    @staticmethod
    def adding_thingsss(num1, num2): # We don't need to write cls in staticmethod.
        return num1 + num2 # In Static method we don't have access to our parent class.

player_1 = PlayerCharactor('Cindy', 17)
player_2 = PlayerCharactor('Tim', 20)
player_2.attack = 50

print(player_1._name)
print(player_2._age)
print(player_2.attack)
print(player_1.run()) # Here, run is a method so, to call it we have to add parenthesis after that.
print(player_1.shout())

player_3 = PlayerCharactor.adding_things(2,3)

print(player_3._name)
print(player_3._age)

player_4 = PlayerCharactor.adding_thingsss(7,3)
print(player_4)

# 4 Pillars of OOP

# 1st pillar:
# Encapsulation --> It is just the storing of our data in a class so, we can use them anytime,
# in our programm. It is a good method bc it is more similar to our real life situations.

# 2nd pillar:
# Abstraction --> An abstraction means hiding your information or abstracting away information,
# and giving access to what's only necessary.

# 3rd pillar:
# Inheritance --> It allows new objects to take on the properties of existing objects.

# 4th pillar:
# Polymorphism --> Poly means many, and morphism means form. It is same function can give different output,
# bc of the different object we pass into it.

player_1.shout = "BOOO"
print(player_1.shout) # So, here we notice that we can overwrite our code, which is bad, it means our all 
# hardwork goes in vain, someone can easily overwrite our code. So, to prevent this we don't have actually any
# method to private our code in python. But we have a convention in our Python community, like _name, _age write 
# like this, it is just a way to tell other user that this is a private code plsss don't alter this. But they
# still can do this.

# Inheritance

# Here, User is parent class and rest are children(sub) classes.
class User():

    def __init__(self, email):
        self.email = email

    def sign_in(self): # We might be wondering why we haven't used __init__ here, it is bc we don't really,
        print('logged in!') # need to use init, when we aren't passing any parameters.

class Wizard(User): # Like this we inherited User class in wizard class.
    def __init__(self, name, power, email):
        # User.__init__(self, email)
        super().__init__(email) # We can write upper line like this, super refers to parent class.
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')

class Archer(User): # Like this we inherited User class in archer class.
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with arrows. Arrows-left: {self.num_arrows}')

# Introspection --> Ability to determine the type of object at its run-time.

wizard1 = Wizard('Merlin', 100, 'merlin@gmail.com')
archer1 = Archer('sika', 50)
wizard1.attack()
archer1.attack()
print(wizard1.sign_in())
print(wizard1.email)
print(dir(wizard1)) # This will introspect and tell what methods and objects this wizard1 has access to.
# So, Python gives us an isinstance function to check whether is something is an instance of some class. eg:
# isinstance(instance, class) # Writing convention.

print(isinstance(wizard1, Wizard)) # True, as wizard1 is an instance of Wizard.
print(isinstance(wizard1, User)) # True, as wizard1 is an instance of Wizard and Wizard is a sub class of User.
print(isinstance(wizard1, object)) # True, as object is a universal build-in class in Python, it stores all the 
# classes, Everything we write is a class which gets stored in object class of python.

def attacking(chr):
    chr.attack() # Here, we can see that the same function is giving diff. output and this is called Polymorphism.

attacking(wizard1)
attacking(archer1)

for char in [wizard1, archer1]: # Here, we can see that the same function is giving diff. output due to Polymorphism.
    char.attack()


# Dunder Method

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name' : 'yoyo',
            'have_pets' : False
        }

    def __str__(self): # We have modified __str__ working here.
        return f'{self.color}'

    def __len__(self):
        return 5

    def __call__(self):
        return 'yesss?'

    def __getitem__(self, i):
        return self.my_dict[i]

action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure)) # We can use dunder methods like this as well.
print(len(action_figure))
print(action_figure()) # We have modified call's value to yesss? So, it will give yesss?
print(action_figure['name'])


class User1():
    def sign_in(self): # We might be wondering why we haven't used __init__ here, it is bc we don't really,
        print('logged in!') # need to use init, when we aren't passing any parameters.

class Wiz(User1): # Like this we inherited User class in wizard class.
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')

class Arch(User1): # Like this we inherited User class in archer class.
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with arrows. Arrows-left: {self.num_arrows}')

    def check_arrows(self):
        print(f'{self.num_arrows} remaining')

    def run(self):
        print('runs really fast')

# Multiple inheritance

# As we can see Multiple inheritance can becoming really complicated here, so, we usually avoid it.
# Many programming languages don't even allow multiple inheritance.

class HybridBorg(Wiz, Arch): # To make it inherit the property of wizard and archer
    def __init__(self, name, power, num_arrows):
        Wiz.__init__(self, name, power)
        Arch.__init__(self, name, num_arrows)

hb1 = HybridBorg('borg', 100, 50)
print(hb1.sign_in())
print(hb1.attack())
print(hb1.run())
print(hb1.check_arrows())

# MRO ---> Method resolution order

class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B, C):
    pass

#       A
#      / \
#     /   \
#    /     \
#   B       C       # This will be the graph of upper class.
#    \     / 
#     \   /
#      \ /
#       D

print(D.mro())  # This mro methed will tell it's pattern of inheritance. D -> B -> C -> A
print(D.num)
print(B.num)
print(A.num)