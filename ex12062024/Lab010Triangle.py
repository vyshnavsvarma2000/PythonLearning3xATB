"""
Write a program that classifies a triangle based on its side lengths.
Given three input values representing the lengths of the sides,
determine if the triangle is equilateral (all sides are equal),
isosceles (exactly two sides are equal), or scalene (no sides are equal).
"""

side1=int(input("Enter the measurement of side 1 :-"))
side2=int(input("Enter the measurement of side 2 :-"))
side3=int(input("Enter the measurement of side 3 :-"))
if side1 == side2 == side3 :
    print("It is an Equilateral triangle")
elif side1 == side2 != side3 or side1!= side2 == side3 or side1 == side3 !=side2:
    print("It is an isoceles triangle")
elif side1 != side2 != side3:
    print("It is a scalene triangle")
