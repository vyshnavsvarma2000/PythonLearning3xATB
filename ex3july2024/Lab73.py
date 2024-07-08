#Custom Exception

class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

balance = 100
withdraw = int(input("Enter the amount to withdraw "))
if withdraw > balance:
    raise MyCustomException("My bal is low")
else:
    print('Remaining balance ', balance-withdraw)