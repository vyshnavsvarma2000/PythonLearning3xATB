#Method Overloading - Pythod doesn't supports it

# Method overloading is When 2 or more functions have same name but different parameters
#Takes the latest functions when having same functions
class Maths:
    def add(self, a, b=0, c=0):
        return a + b + c

obj = Maths()
print(obj.add(1,2))
print(obj.add(1,2,3))
