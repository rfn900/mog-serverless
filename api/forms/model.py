class Forms:
    def register_payload(self, data):
        self.payload = data

    def save(self):
        from run import db

        db.mog_prod.contacts.insert_one(self.payload)
