# -*- coding: utf-8 -*-
import copy
import json
import re
import time


def beep_small(server, info, name_list):
	for name in name_list:
		server.execute('execute at {0} run playsound minecraft:entity.arrow.hit_player player {0}'.format(name))


def beep_big(server, info, name_list):
	if not name_list:
		return
	source = info.player if info.isPlayer else '控制台'
	text = json.dumps([
		{
			'text': source,
			'color': 'aqua'
		},
		{
			'text': '在@你',
			'color': 'white'
		}
	])
	for name in name_list:
		server.execute('title {} times 2 15 5'.format(name))
		server.execute('title {} title {}'.format(name, text))
	for i in range(2):
		time.sleep(1.0 / 3)
		beep_small(server, info, name_list)


def find_name_list(text, pattern):
	name_list = None
	if text.find('{} '.format(pattern)) > -1:
		name_list = re.findall(r'(?<={} )\S+'.format(pattern), text)
	if not name_list:
		name_list = []
	for i, name in enumerate(name_list):
		if name == 'all':
			name_list[i] = '@a'
	return name_list


def onServerInfo(server, info):
	if info.isPlayer == 1 or (hasattr(server, 'MCDR') and info.is_user) and info.content.find('@ ') > -1:
		beep_small(server, info, find_name_list(info.content, '@'))
		beep_big(server, info, find_name_list(info.content, '@@'))


def on_info(server, info):
	info2 = copy.deepcopy(info)
	info2.isPlayer = info2.is_player
	onServerInfo(server, info2)


def on_load(server, old):
	server.add_help_message('@ xxx', '@某人，@ all可作用于所有玩家。使用两个@@效果更佳')
