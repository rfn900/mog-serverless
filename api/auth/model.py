class User:
    def __init__(self, fullName, username, email, password):
        self.fullName = fullName
        self.username = username
        self.email = email
        self.password = password

    def prepare_payload(self):
        return {
            "fullName": self.fullName,
            "username": self.username,
            "email": self.email,
            "password": self.password,
        }
