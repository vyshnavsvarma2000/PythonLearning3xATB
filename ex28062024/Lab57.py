class Password:

    def __init__(self, password):
        self.__password = password
        a = 10

    def get_password(self, is_auth):
        if is_auth:
            print(self.__password)
        else:
            print("Invalid password")

    def set_password(self, password):
        if len(password)>10:
            self.__password = password
            print("Set to correct", self.__password)
        else:
            print("Weak password")

pwd = Password(1234567890)
pwd.get_password(True)
pwd.set_password("jwhdefbEJDFBJJ")
pwd.get_password(True)
