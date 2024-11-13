import json
import pymongo
from datetime import datetime

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['timer']

col = db['boss']
col.insert_one({'boss_name': 'North', 'boss_type': 'ring', 'open_time': 0, 'respawn': 216, 'window': 48, 'alias': ['north', 'n'], 'sent': True})
col.insert_one({'boss_name': 'Middle', 'boss_type': 'ring', 'open_time': 0, 'respawn': 216, 'window': 48, 'alias': ['middle', 'm'], 'sent': True})
col.insert_one({'boss_name': 'South', 'boss_type': 'ring', 'open_time': 0, 'respawn': 216, 'window': 48, 'alias': ['south', 's'], 'sent': True})
col.insert_one({'boss_name': 'East', 'boss_type': 'ring', 'open_time': 0, 'respawn': 216, 'window': 48, 'alias': ['east', 'e'], 'sent': True})