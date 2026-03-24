class User:
    def login(self):
        pass   # abstraction


class Admin(User):
    def login(self):
        return "Admin Login Successful"

    def role(self):
        return "Admin"


class Faculty(User):
    def login(self):
        return "Faculty Login Successful"

    def role(self):
        return "Faculty"