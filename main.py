import os

import pymongo
import db_interactions
import software


def create_database_if_needed(name: str):
    if name in client.list_database_names():
        print(f'DB {name} exists')
        return db_interactions.create_db(name)
    else:
        create_db_input = input('DB {name} does not exist. Should it be created? (y/n): ')
        if create_db_input == 'y':
            print(f'Creating DB {name}')
            return db_interactions.create_db(name)
        else:
            return None


connection_string = os.environ.get('CS_MONGODB')
client = pymongo.MongoClient(connection_string)
db_interactions = db_interactions.DbInteractions(client)

softwares_db = create_database_if_needed('softwares')
keys_db = create_database_if_needed('keys')

if softwares_db is None or keys_db is None:
    print('Required DB is not available')
else:
    action = input('Select action (i, k, ik, q): ')
    if action == 'q':
        print('Goodbye!')
    elif action == 'i':
        software_input = input('Enter software name and manufacturer')
        name = software_input.split(' ')[0]
        manufacturer = software_input.split(' ')[1]
        software = software.Software(name, manufacturer)
        db_interactions.insert_software(software.__dict__)
