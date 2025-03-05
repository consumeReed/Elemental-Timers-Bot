import pymongo
from datetime import datetime

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['timer']

col = db['boss']

col.update_many({}, {'$set': {"event": False}})

col = db['change-log']
col.insert_one({'user': 'name', 'time': 0, 'boss': 'boss_name', 'window': 0, 'respawn': 0, 'event': False})