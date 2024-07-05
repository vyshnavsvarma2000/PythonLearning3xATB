class Parent:
    gold = "2kg"
    def two_bhk(self):
        print("Two bhk")


class Child(Parent):
    def three_bhk(self):
        print("Three bhk")

child = Child()
print(child.gold)