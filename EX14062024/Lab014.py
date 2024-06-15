numbers = int(input('Enter a number \n'))
match numbers:
    case 1:
        print("Hello 1")
    case 2:
        print("Hello 2")
    case 3:
        print("Hello 3")
if not numbers in [1,2,3]:
    print("Invalid case")