# -*- coding: utf-8 -*-

import re
import traceback

def onServerInfo(server, info):
  if info.isPlayer == 1:
    if info.content.find('@') > -1:
      nameList = re.findall('(?<=@)\S+',info.content)
      server.say(str(nameList))
      for name in nameList:
        server.say('playsound minecraft:entity.arrow.hit_player player ' + name)
        server.execute('playsound minecraft:entity.arrow.hit_player player ' + name)
