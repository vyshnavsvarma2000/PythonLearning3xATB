#   Sum of Digits
def sum_of_digits(num):
    # Base case
    if num < 10:
        return num
    #Recursive Case
    else:
       return num % 10 + sum_of_digits(num // 10)

print(sum_of_digits(12345))
#Without Recursion
def sum_of_digits(num):
    sum = 0
    while  num > 0:
        digit = num % 10
        sum  += digit
        num = num // 10
    return sum
print(sum_of_digits(125))
