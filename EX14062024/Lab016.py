browser = input("Enter the browser\n ")

match browser.lower():
    case "chrome":
        print("Execute the code for chrome browser")
    case "firefox":
        print("Execute the code for firefox browser ")
    case _:
        print("No browser found  ")