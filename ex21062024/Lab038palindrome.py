string = input("Enter a string\n")
rev_string = string[::-1]
if string == rev_string:
    print("Palindrome ")
else:
    print("Not palindrome")