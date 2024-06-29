#Encapsulation with Access Modifiers
#Hide the data members(class variables, instance variables) by using only methods

class Car:
    name = None
    def __init__(self):
        self.public_var = "public"
        self._protected_variable = "protected"
        self.__private_variable = "private"

    def __private_method(self):
        print("Private ")

    def print_name(self):
        self.__private_variable()
        print("Hi public var")

alto = Car()
alto.print_name()