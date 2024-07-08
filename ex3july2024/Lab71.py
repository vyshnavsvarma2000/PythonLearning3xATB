#try except else finally
try:
    num1 = int(input("Enter a number\n"))
    num2 = int(input("Enter another number\n"))
    result = num1/ num2

except ZeroDivisionError as e:
    print(e)
except ValueError as v:
    print(v)
else:
    print("Result is ",result)
finally:
    print("I will be executed anyway")
