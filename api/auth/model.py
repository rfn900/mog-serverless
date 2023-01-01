class User:
    def set_new_user(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = password

    def retrieve_user_by_email(self, email):
        from run import db

        user = db.mog_prod.users.find_one({"email": email})
        if user:
            return user
        return False

    def save_user(self):
        from run import db

        db.mog_prod.users.insert_one(
            {
                "name": self.name,
                "username": self.username,
                "email": self.email,
                "password": self.password,
            }
        )
