import re

def onServerInfo(server, info):
    if info.isPlayer == 1:
        server.say('start finding name')
        nameList = re.findall('(?<=@)\S+(?= )',info.content)
        for name in nameList:
            server.say(name)
            server.execute('playsound minecraft:entity.arrow.hit_player player ' + name)
