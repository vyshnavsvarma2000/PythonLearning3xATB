# Encapsulation with Access Modifiers
class Myclass:

    def public_func(self):
        print("Public Function")

    def __private_func(self):
        print("I am a private variable , can only be accessed by a method within the class")

    def public_fn_private(self):
        self.__private_func()

a = Myclass()
a.public_func()
a.public_fn_private()

