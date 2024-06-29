class BankAccount:

    def __init__(self):
        self.balance = 0
        self.__private_var = 100

    def public_fn(self):
        print(self.__private_var)

    def deposit(self, amount):
        self.balance += amount

    def __withdraw(self, amount):
        self.balance -= amount

    def __display_balance(self):
        print("Balance is ", self.balance)

    def if_you_are_authenticated(self, flag):
        if flag:
            self.__display_balance()
        else:
            print("Not allowed ")

    def if_you_are_auth_user(self, auth,amount):
        if auth:
            self.__withdraw(amount=amount)
        else:
            print("Not allowed ")


hdfc = BankAccount()
hdfc.deposit(1000)
secret_password = int(input("Enter your pin\n"))
if secret_password == 1234:
    hdfc.if_you_are_authenticated(True)
else:
    print("Not allowed")

secret_password = int(input("Enter your pin to withdraw amount \n"))
if secret_password == 1234:
    amount = int(input("Enter an amount "))
    hdfc.if_you_are_auth_user(True, amount)
    hdfc.if_you_are_authenticated(True)
else:
    print("Not allowed")
