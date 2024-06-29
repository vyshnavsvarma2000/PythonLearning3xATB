#OOPS

class Dog:
    name = None
    id = None

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def sleep(self, name):
        print("I can sleep", name)

dg = Dog("shaw", 1)
print(dg.name, dg.id)