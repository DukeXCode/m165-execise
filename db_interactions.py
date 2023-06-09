class DbInteractions:
    def __init__(self, client):
        self.client = client

    def create_db(self, name):
        return self.client[name]

    def insert_software(self, fields: dict):
        self.client['softwares'].insert_one(fields)

    def insert_key(self, software_id, key):
        return self.client['keys'].insert_one({'software_id': software_id, 'key': key})

    def get_key(self, software_id):
        return self.client['keys'].find({'software_id': software_id})['key']
