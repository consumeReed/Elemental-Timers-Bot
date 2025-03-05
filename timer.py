import os
from discord.ext import commands, tasks
from dotenv import load_dotenv
import discord
import pymongo
import time

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['timer']
col = db['boss']

#<t:1726156800>
#<t:1726105860:R>

def get_raids(boss_type):

    if boss_type == 'r':
        boss_type = 'raid'
    elif boss_type == 'e':
        boss_type = 'edl'
    elif boss_type == 'd':
        boss_type = 'dl'

    now = int(time.time())

    output = " ## Elemental Boss Times: \n*Times are in your local timezone*\n"

    res = col.find({'boss_type': boss_type})
    list_ = list(res)

    if len(list_) != 0: 
        for boss in list_:
            if boss['event'] and boss['window'] > 0:
                output+=boss['boss_name']+" (Event)\n"
            elif boss['event'] and boss['window'] == 0:
                output+=boss['boss_name']+" (Insta-spawn)\n"
            else:
                output+=boss['boss_name']+"\n"

            if boss['event'] and boss['window'] == 0:
                output+="spawns at <t:"+str(boss['open_time'])+">\n"
                output+="spawns <t:"+str(boss['open_time'])+":R>\n\n"
            else:
                output+="open at <t:"+str(boss['open_time'])+">\n"
                output+="open <t:"+str(boss['open_time'])+":R>\n\n"

            if boss['open_time'] < now:
                close_time = boss['open_time'] + boss['window']*60
                output+="\> closes at <t:"+str(close_time)+">\n"
                output+="\> closes <t:"+str(close_time)+":R>\n\n"
    else:
        return "Did not find any bosses matching '"+boss_type+"'\nValid searches are r, raid, e, edl, d, dl, ring."

    return output

#<@&ROLE_ID>

def check():
    ring_role = 1270835283147096164
    raid_role = 1270835238729154733
    dl_role = 1270834953596436652
    edl_role = 1270834559088332850
    event_role = 1346671613357326419

    now = int(time.time())

    output = ""

    res = col.find({'boss_name': {'$ne': 'Proteus'}, 'sent': False})

    for boss in res:
        if boss['open_time'] - 5*60 < now:
            col.update_one({'boss_name': boss['boss_name']}, {'$set': {'sent': True}})
            if boss['boss_name'] == '215':
                output+="<@&"+str(raid_role)+"> <@&"+str(edl_role)+"> "+boss['boss_name']+" window open <t:"+str(boss['open_time'])+":R>\n"
            elif boss['boss_type'] == 'edl':
                output+="<@&"+str(edl_role)+"> "+boss['boss_name']+" window open <t:"+str(boss['open_time'])+":R>\n"
            elif boss['boss_type'] == 'dl':
                output+="<@&"+str(dl_role)+"> "+boss['boss_name']+" window open <t:"+str(boss['open_time'])+":R>\n"
            elif boss['boss_type'] == 'ring':
                output+="<@&"+str(ring_role)+"> "+boss['boss_name']+" window open <t:"+str(boss['open_time'])+":R>\n"
            elif boss['boss_type'] == 'raid' and not boss['event']:
                output+="<@&"+str(raid_role)+"> "+boss['boss_name']+" window open <t:"+str(boss['open_time'])+":R>\n"
            elif boss['boss_type'] == 'raid' and boss['event']:
                output+="<@&"+str(raid_role)+"> <@&"+str(event_role)+"> "+boss['boss_name']+" spawns at <t:"+str(boss['open_time'])+":R>\n"

    res2 = col.find({'boss_name': 'Proteus', 'sent': False})
    for boss in res2:
        if boss['open_time'] - 15*60 < now:
            col.update_one({'boss_name': boss['boss_name']}, {'$set': {'sent': True}})
            if boss['boss_type'] == 'raid' and not boss['event']:
                output+="<@&"+str(raid_role)+"> "+boss['boss_name']+" window open <t:"+str(boss['open_time'])+":R>\n"
            elif boss['boss_type'] == 'raid' and boss['event']:
                output+="<@&"+str(raid_role)+"> <@&"+str(event_role)+"> "+boss['boss_name']+" spawns at <t:"+str(boss['open_time'])+":R>\n"

    return output

def set_times(boss_alias, respawn, window):
    boss = col.find_one({'alias': {"$in": [boss_alias.lower()]}})
    boss_name = boss['boss_name']
    col.update_one({'boss_name': boss_name}, {'$set': {'respawn': respawn, 'window': window, 'sent': True}})
    return boss_name

def minutes2Hours(minutes):
    hours = int(minutes/60)
    minutes = int(minutes%60)
    return str(hours)+":"+"{:02d}".format(minutes)

def set_down(boss_alias, offset):
    now = int(time.time())
    boss = col.find_one({'alias': {"$in": [boss_alias.lower()]}})
    boss_name = boss['boss_name']
    respawn = boss['respawn']
    open_time = now - offset*60 + respawn*60
    col.update_one({'boss_name': boss_name}, {'$set': {'open_time': open_time, 'sent': False}})
    return open_time

def get_aliases():
    output = ""
    bosses = col.find()
    for boss in bosses:
        output+=boss['boss_name']+" =="
        aliases = boss['alias']
        for i in range(len(aliases)):
            if i < len(aliases) - 1:
                output+=" "+aliases[i]+", "
            else:
                output+=" "+aliases[i]
        output+="\n"
    return output

def get_list():
    output = " # Current Boss Respawn Time Settings\n"
    bosses = col.find()
    for boss in bosses:
        output+="* "+boss['boss_name']+":  "+minutes2Hours(boss['respawn'])+" - "+minutes2Hours(boss['respawn']+boss['window'])+"\n"
    return output

def log(user, boss, respawn, window, event):
    now = int(time.time())
    col.insert_one({'user': user, 'time': now, 'boss': boss, 'window': window, 'respawn': respawn, 'event': event == 'event' or event == 'e'})

def get_log():
    col = db['change-log']
    res = col.find({'$query': {}, '$orderby': {'$natural': -1}}).limit(15)
    output = " ## Elemental Boss Times Change Log:\n"
    for entry in res:
        output += "<t:"+str(entry['time'])+"> " + entry['user'] + " updated\n"
        + "**" + str(entry['boss']) + "** to " + minutes2Hours(int(entry['respawn'])) + " respawn, "
        + minutes2Hours(int(entry['window'])) + " window "
        if entry['event'] and int(entry['window']) > 0:
            output+="event\n\n"
        elif entry['event'] and int(entry['window']) == 0:
            output+="instant event\n\n"
        else:
            output+="\n\n"
    col = db['boss']
    return output

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN_TIMER')
bot = commands.Bot(intents=discord.Intents.all(), command_prefix='!')

@bot.command(name='bosses', help='Get a list of boss times.')
async def aliases(ctx):
    try:
        elem = bot.get_guild(704350758417727662)
        if elem.get_member(ctx.author.id) is not None:
            message = get_list()
            await ctx.send(message)
        else:
            await ctx.send("You are not an Elementals member, you are ineligible to use this command!")
    except Exception as e:
        print("exception while getting aliases\n"+str(e))

@bot.command(name='aliases', help='Get a list of aliases.')
async def aliases(ctx):
    try:
        elem = bot.get_guild(704350758417727662)
        if elem.get_member(ctx.author.id) is not None:
            message = get_aliases()
            await ctx.send(message)
        else:
            await ctx.send("You are not an Elementals member, you are ineligible to use this command!")
    except Exception as e:
        print("exception while getting aliases\n"+str(e))

@bot.command(name='find', help='Get list of timers. Valid searches are r, raid, e, edl, d, dl, ring.')
async def find(ctx, search):
    try:
        elem = bot.get_guild(704350758417727662)
        if elem.get_member(ctx.author.id) is not None:
            message = get_raids(str(search))
            await ctx.send(message)
        else:
            await ctx.send("You are not an Elementals member, you are ineligible to use this command!")
    except Exception as e:
        print("error finding list of bosses\n"+str(e))

@bot.command(name='update', help='Update the respawn time and window of a boss.')
async def update(ctx, *, search):
    try:
        elem = bot.get_guild(704350758417727662)
        if elem.get_member(ctx.author.id) is not None:
            query = str(search).split(' ')
            if len(query) == 3:
                boss = set_times(str(query[0]), int(query[1]), int(query[2]), None)
                log(ctx.author.name, str(query[0]), int(query[1]), int(query[2]), None)
            else:
                boss = set_times(str(query[0]), int(query[1]), int(query[2]), str(query[3]))
                log(ctx.author.name, str(query[0]), int(query[1]), int(query[2]), str(query[3]))
            await ctx.send(boss+"\nNew respawn time is "+minutes2Hours(int(query[1]))+"\nNew window is "+minutes2Hours(int(query[2])))
        else:
            await ctx.send("You are not an Elementals member, you are ineligible to use this command!")
    except Exception as e:
        print("error updating boss respawn and window time\n"+str(e))

@bot.command(name='down')
async def down(ctx, *, search):
    try:
        elem = bot.get_guild(704350758417727662)
        if elem.get_member(ctx.author.id) is not None:
            query = str(search).split(' ')
            offset = 0
            if len(query) == 2:
                offset = query[1]
            open_time = set_down(str(query[0]), int(offset))
            await ctx.send(" ## Success!\nNew spawn time is <t:"+str(open_time)+":R>")
        else:
            await ctx.send("You are not an Elementals member, you are ineligible to use this command!")
    except Exception as e:
        print("Error while setting a boss to down\n"+str(e))

@bot.command(name='log', help='Most recent 15 updates to boss timers')
async def down(ctx):
    try:
        elem = bot.get_guild(704350758417727662)
        if elem.get_member(ctx.author.id) is not None:
           msg = get_log()
           await ctx.send(msg)
        else:
            await ctx.send("You are not an Elementals member, you are ineligible to use this command!")
    except Exception as e:
        print("Error while getting log\n"+str(e))

@bot.event
async def on_ready():
    check_open.start()

@tasks.loop(seconds=15)
async def check_open():
    try:
        channel = bot.get_channel(1224164705984057435)
        message = check()
        if message == "":
            return
        await channel.send(message)
    except Exception as e:
        print("Error checking open\n"+str(e))

bot.run(TOKEN)

