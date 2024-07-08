#Exception Handling
"""
Exception is an event occurs during the execution of a program
that disrupts normal flow of instructions
"""
"""
try -> Run this code
except -> Execute this code when their is an exception
else -> No exceptions? Run this code
finally -> Always run this code

"""
try:

    a = int(input("Enter the num 1 "))
    b = int(input("Enter the num2 "))
    c = a/b
    print("Result is ", c)

except ZeroDivisionError:
    print("Division by zero is not allowed")
except Exception as e:
    print("Wrong value\n",e)
