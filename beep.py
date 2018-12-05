# -*- coding: utf-8 -*-

import re
import traceback

def onServerInfo(server, info):
    try:
        if info.isPlayer == 1:
            if info.content.find('@') > -1:
                nameList = re.findall('(?<=@)\S+(?= )',info.content)
                for name in nameList:
                    server.execute('playsound minecraft:entity.arrow.hit_player player ' + name)
    except:
        lines = traceback.format_exc().splitlines()
        for l in lines:
            server.say(l)
