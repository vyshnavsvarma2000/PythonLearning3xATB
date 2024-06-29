#OOPs
#Class Variables / instance variable
class Person:
    name = 'amit'
    age = None

    def walk(self):
        a = 10
        print("I am a method")
        print("Hi", self.age)

per = Person()
per.walk()