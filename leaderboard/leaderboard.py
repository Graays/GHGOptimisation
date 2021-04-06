import json

with open('data/database.json', 'read') as data:

    json.dump(json.load(data), data)
    data.close()