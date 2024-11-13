import json
import pymongo
from datetime import datetime

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['timer']

col = db['boss']
col.drop()
col = db['boss']

col.insert_one({'boss_name': 'Mordris', 'boss_type': 'raid', 'open_time': 0, 'respawn': 1200, 'window': 960, 'alias': ['mord', 'mordy', 'mordi', 'mordris'], 'sent': True})
col.insert_one({'boss_name': 'Bloodthorn', 'boss_type': 'raid', 'open_time': 0, 'respawn': 2040, 'window': 1680, 'alias': ['bt', 'bloodthorn'], 'sent': True})
col.insert_one({'boss_name': 'Hrungnir', 'boss_type': 'raid', 'open_time': 0, 'respawn': 1320, 'window': 960, 'alias': ['hrungnir', 'hrung', 'hippo', 'hrunrir'], 'sent': True})
col.insert_one({'boss_name': 'Proteus', 'boss_type': 'raid', 'open_time': 0, 'respawn': 1080, 'window': 30, 'alias': ['proteus', 'prot', 'base', 'prime'], 'sent': True})
col.insert_one({'boss_name': 'Necromancer', 'boss_type': 'raid', 'open_time': 0, 'respawn': 1320, 'window': 960, 'alias': ['nec', 'necro', 'necromancer', 'efnisien'], 'sent': True})
col.insert_one({'boss_name': 'Gelebron', 'boss_type': 'raid', 'open_time': 0, 'respawn': 1560, 'window': 1320, 'alias': ['gele', 'gelebron'], 'sent': True})
col.insert_one({'boss_name': 'Dhiothu', 'boss_type': 'raid', 'open_time': 0, 'respawn': 2040, 'window': 1680, 'alias': ['dhio', 'dino', 'dhino', 'dhiothu'], 'sent': True})
col.insert_one({'boss_name': 'Aggragoth', 'boss_type': 'raid', 'open_time': 0, 'respawn': 1200, 'window': 960, 'alias': ['aggy', 'agg', 'agragoth', 'aggragoth'], 'sent': True})

col.insert_one({'boss_name': 'Ring', 'boss_type': 'ring', 'open_time': 0, 'respawn': 216, 'window': 48, 'alias': ['ring', 'rb'], 'sent': True})

col.insert_one({'boss_name': 'Snorri', 'boss_type': 'dl', 'open_time': 0, 'respawn': 90, 'window': 5, 'alias': ['snorri', '180'], 'sent': True})
col.insert_one({'boss_name': 'Sreng', 'boss_type': 'dl', 'open_time': 0, 'respawn': 0, 'window': 5, 'alias': ['sreng', '170'], 'sent': True})
col.insert_one({'boss_name': 'King', 'boss_type': 'dl', 'open_time': 0, 'respawn': 0, 'window': 5, 'alias': ['king', '165'], 'sent': True})
col.insert_one({'boss_name': 'Priest', 'boss_type': 'dl', 'open_time': 0, 'respawn': 0, 'window': 5, 'alias': ['priest', '160'], 'sent': True})

col.insert_one({'boss_name': '215', 'boss_type': 'edl', 'open_time': 0, 'respawn': 133, 'window': 10, 'alias': ['215', 'unox'], 'sent': True})
col.insert_one({'boss_name': '210', 'boss_type': 'edl', 'open_time': 0, 'respawn': 125, 'window': 10, 'alias': ['210', 'phantom'], 'sent': True})
col.insert_one({'boss_name': '200', 'boss_type': 'edl', 'open_time': 0, 'respawn': 120, 'window': 10, 'alias': ['200'], 'sent': True})
col.insert_one({'boss_name': '195', 'boss_type': 'edl', 'open_time': 0, 'respawn': 100, 'window': 10, 'alias': ['195'], 'sent': True})
col.insert_one({'boss_name': '190', 'boss_type': 'edl', 'open_time': 0, 'respawn': 91, 'window': 10, 'alias': ['190'], 'sent': True})
col.insert_one({'boss_name': '185', 'boss_type': 'edl', 'open_time': 0, 'respawn': 80, 'window': 10, 'alias': ['185'], 'sent': True})


