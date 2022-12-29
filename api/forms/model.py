class Forms:
    def __init__(self, data) -> None:
        self.payload = data

    def save(self):
        from run import db

        db.mog_prod.contacts.insert_one(self.payload)
