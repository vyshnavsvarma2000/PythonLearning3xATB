#decorators

def my_decorator(func):
    def wrapper():
        print("****************************")
        print("Before")
        print("***************************")
        print("After")
        func()
    return wrapper()


@my_decorator
def say_hello():
    print("Say Hello ")
