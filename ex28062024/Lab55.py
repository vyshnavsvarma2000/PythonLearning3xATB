class VwoLogin:

    def __init__(self, email, password, name):
        self.__email = email
        self.__password = password
        self.name = name

    def login_confirm(self):
        if self.__email == "abc@gmail.com" and self.__password == 123:
            print("Allowed", self.name)
        else:
            print("Not allowed")

p1 = VwoLogin("abc@gmail.com", 123, "Amit")
p1.login_confirm()

