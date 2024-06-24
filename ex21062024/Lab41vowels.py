string = input("Enter a string  ")
vowel_list =  ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
vowel_count = 0
consonant_count = 0
for char in string:
    if char in vowel_list:
        vowel_count+=1
    elif char not in vowel_list and char.isalpha():
        consonant_count+=1
print("count of vowels in the string is", vowel_count)
print("Consonant count of the string is", consonant_count)