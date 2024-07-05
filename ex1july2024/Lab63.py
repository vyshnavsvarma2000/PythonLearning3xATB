#Hybrid Inheritance
#Combination of single , hierarchial, multiple inheritances
#Last child can access every methods
class A:
    def method_a(self):
        print("Method A")

class B(A):
    def method_b(self):
        print("Method B")

class C(A):
    def method_c(self):
        print("Method C")

class D(B,C):
    def method_d(self):
        print("Method D")

d = D()
d.method_a()
d.method_b()
d.method_c()
d.method_d()
