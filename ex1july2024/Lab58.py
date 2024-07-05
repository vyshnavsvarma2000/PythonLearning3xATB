#Inheritance

#Single Inheritance

class GrandParent:
    key = 123
    def grand_parent_method(self):
        return "Grand parent"

class Father(GrandParent):
    def father_method(self):
        return "Father "

parent = Father()
print(parent.key)
print(parent.grand_parent_method())