try:
    with open('yshnav', 'r') as file:
        print(file.read())
except FileNotFoundError as e:
    print("Unable to find the file",e)

finally:
    try:
        print("CLOSING FILE -----")
        file.close()
    except NameError as ne:
        print(ne)
