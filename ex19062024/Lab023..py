# Function Scope

def outer_function():
    a = 10
    print(a)
    def inner_function():
        print("hi ")
    inner_function()
outer_function()

