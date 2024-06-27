# Recursion - A function that can call itself
#Key concepts
"""
1) Base Case 2) Recursive Case
"""
def factorial (num):
    #Base Case
    if num == 0 or num == 1:
        return 1

    #Recursive Case
    else:
        return num * factorial(num - 1)

print(factorial(0))