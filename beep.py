# -*- coding: utf-8 -*-

import re
import traceback

def onServerInfo(server, info):
    try:
        server.say('被调用')
        if info.isPlayer == 1:
            server.say('判断是否存在@符号')
            if info.content.find('@') > -1:
                server.say('开始调用正则表达式')
                nameList = re.findall('(?<=@)\S+(?= )',info.content)
                server.say(str(nameList))
                for name in nameList:
                    server.execute('playsound minecraft:entity.arrow.hit_player player ' + name)
    except:
        lines = traceback.format_exc().splitlines()
        for l in lines:
            server.say(l)
