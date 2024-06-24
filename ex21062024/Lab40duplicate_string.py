string = input("Enter a string\n")
duplicate_string = ""
for i in string:
    if i not in duplicate_string:
        duplicate_string+=i
print(duplicate_string)