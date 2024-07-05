#Method Overriding
#Child will always override the parent methods

class Parent:
    def home(self):
        print("One BHK")

class Son(Parent):
    def home(self):
        super().home()   # super() can call parent methods
        print("Three Bhk")

son = Son()
son.home()
