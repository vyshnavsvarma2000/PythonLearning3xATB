#Hierarchial Inheritance

#1 Parent - Multiple childrens

class Father:
    gold = "4kg"
    def one_bhk(self):
        print("One bhk")

class Child1(Father):
    def two_bhk(self):
         print("2 bhk house")

class Child2(Father):
    def three_bhk(self):
        print("3 bhk house")

child1 = Child1()
child2 = Child2()
child1.one_bhk()
print(child1.gold)
child2.three_bhk()
child2.one_bhk()