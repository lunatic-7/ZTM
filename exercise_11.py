# Extending list (Exercise)

class SuperList(list): # So, here list is the parent class of SuperList
    def __len__(self):
        return 1000

super_list1 = SuperList()

print(len(super_list1))
super_list1.append(5) # We have appended 5 in our list
super_list1.append(100) # We have appended 100 here.
print(super_list1)
print(super_list1[0])
print(issubclass(SuperList, list)) # Is superlist subclass of list. This is True.