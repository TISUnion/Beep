# -*- coding: utf-8 -*-

import re
import traceback

def onServerInfo(server, info):
  if info.isPlayer == 1:
    if info.content.find('@ ') > -1:
      nameList = re.findall('(?<=@ )\S+(?= ?)',info.content)
      if nameList:
        for name in nameList:
          server.execute('execute at ' + name + ' run playsound minecraft:entity.arrow.hit_player player ' + name)
  server.tell('Lucun_Ji', info.content)
