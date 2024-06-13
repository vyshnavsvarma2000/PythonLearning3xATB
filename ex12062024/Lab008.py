"""
Write a program that calculates and displays grades based on numberical scores
A:90-100
B:80-89
C:70-79
D:60:69
E:50-59
F:0-49
"""
try:
    score = int(input("Enter your score : "))
    if score >=90:
        print("Grade A")
    elif score>=80 and score<90:
        print("Grade B")
    elif score>=70 and score<80:
        print("Grade C")
    elif score>=60 and score<70:
        print("Grade D")
    elif score>=50 and score<60:
        print("Grade E")
    elif score>0 and score<=49:
        print("Grade F")
    else:
        print("Invalid choice")
except:
    print("Wrong input")
