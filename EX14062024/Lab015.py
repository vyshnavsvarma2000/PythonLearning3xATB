string = input("Enter a string ")

match string:
    case "vyshnav":
        print("You are vyshnav")
    case "vishal":
        print("You are vishal")
    case _:
        print("no idea")