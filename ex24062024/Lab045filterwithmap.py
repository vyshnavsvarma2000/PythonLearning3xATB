#Map function

numbers = [1,2,3,4,5,6,7,8,9,10]

#map
def double_num(num):
    return num * 2
mapped_values = list(map(double_num, numbers))
print(mapped_values)

#filter

def even_giver(num):
    return num % 2 == 0

# even_filter = list(filter(even_giver, numbers))
# print(even_filter)

# even_filter = list(filter(lambda num : num%2 == 0, numbers))
# print(even_filter)
# or can give thw whole code in a single line

even_filter = list(filter(lambda num : num%2 == 0,[1,2,3,4,5,6,7,8,9,10]
))
print(even_filter)

