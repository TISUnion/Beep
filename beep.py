import re

def onServerInfo(server, info):
    if info.isPlayer == 1:
        nameList = re.findall('(?<=@)\S+(?= )',info.content)
        for name in nameList:
            server.execute('playsound random.orb player ' + name)
