#filter - allows you to filter the elements from a list , tuple , set

"""
Filters will work only with functions
that give True Or False
"""
numbers = [1,2,3,4,5,6,7,8,9,10]

def is_even(num):
    return num%2 == 0

def is_greater_than_5(num):
    return num>5
even_numbers = filter(is_even, numbers)
print(list(even_numbers))

greater_than_5 = list(filter(is_greater_than_5, numbers))
print(greater_than_5)

letters = ['a', 'b' , 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u']

def is_vowel(x):
    return x in ['a', 'e', 'i', 'o', 'u']

vowels = list(filter(is_vowel, letters))
print(vowels)