class DbInteractions:
    def __init__(self, client):
        self.client = client

    def create_db(self, name):
        return self.client[name]

    def insert_software(self, fields: dict):
        self.client['softwares'].insert_one(fields)
