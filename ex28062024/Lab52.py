#Web Automation - Selenium
#Page - you're going to automate

class VWOLoginPage:
    def __init__(self, email, password):
        self.email = email
        self. password = password

    def login_confirm(self):
        if self.email == "amit@gmail.com"  and self.password == "Pass123":
            print("Allowed to enter")
        else:
            print("Not allowed to enter")

amit = VWOLoginPage("amit@gmail.com", "Pass123")
amit.login_confirm()