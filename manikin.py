import json
import pymongo
from datetime import datetime

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['timer']

col = db['boss']

col.insert_one({'boss_name': 'Manikin', 'boss_type': 'raid', 'open_time': 0, 'respawn': 1200, 'window': 960, 'alias': ['manakin', 'mani', 'manikin', 'hellborne'], 'sent': True})