# -*- coding: utf-8 -*-

import re
import traceback
import copy

def onServerInfo(server, info):
  if info.isPlayer == 1:
    if info.content.find('@ ') > -1:
      nameList = re.findall('(?<=@ )\S+',info.content)
      if nameList:
        for name in nameList:
          if name == 'all':
            server.execute('execute at @a run playsound minecraft:entity.arrow.hit_player player @a')
          else:
            server.execute('execute at ' + name + ' run playsound minecraft:entity.arrow.hit_player player ' + name)

def on_info(server, info):
  info2 = copy.deepcopy(info)
  info2.isPlayer = info2.is_player
  onServerInfo(server, info2)
