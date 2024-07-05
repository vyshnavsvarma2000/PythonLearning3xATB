#Multiple Inheritance - 2 parents 1 child

class Father:
    father_cash = 100
    def father_money(self):
        print("Father money")

class Mother:
    mother_cash = 200
    def mother_money(self):
        print("Mother's money ")

class Child(Father, Mother):
    child_cash = 10
    def child_money(self):
        print("Child's money ")

child = Child()
child.father_money()
print(child.father_cash)
child.mother_money()
print(child.mother_cash)
child.child_money()
print(child.child_cash)

#Method Resolution Order
"""
Since the Father and Mother have same function and 
the Son doesn't have a function , if Son calls the
common function which is in both parent's ,
It will only call the method of it's First parent

If the Son has the same method, it is called since local functions have
more priority
"""

class Father:
    def home(self):
        print("Father's home")


class Mother:
    def home(self):
        print("Mother's home")

class Son(Mother, Father):
    pass

son = Son()
son.home()