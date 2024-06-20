numbers = [1, 2, 3]

def function(numbers):
    numbers.append(4)
    numbers[0] = 123
    return numbers

a = function(numbers)
print(a)