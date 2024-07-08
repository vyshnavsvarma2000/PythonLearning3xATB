try:
    file= open('vyshnav', 'r')
    content = file.read()
    print(content)
except FileNotFoundError as e:
    print(e)

finally:
    try:
        print("Close the file")
        file.close()
    except NameError as w:
        print(w)


