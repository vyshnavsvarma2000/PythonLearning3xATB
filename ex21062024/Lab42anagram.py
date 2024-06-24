def is_anagram(s1,s2):
    if sorted(s1) == sorted(s2):
        print("Anagram")
        return True
    else:
        print("Not anagram")
        return False
print(is_anagram("namo", "onam"))