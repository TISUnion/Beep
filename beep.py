import json
import re
import time

from mcdreforged.api.decorator import new_thread
from mcdreforged.api.types import *

PLUGIN_METADATA = {
	'id': 'beep',
	'version': '1.0.0'
}


def beep_small(server, info, name_list):
	if not name_list:
		return
	info.cancel_send_to_server()
	for name in name_list:
		server.execute('execute at {0} run playsound minecraft:entity.arrow.hit_player player {0}'.format(name))


def beep_big(server: ServerInterface, info: Info, name_list):
	if not name_list:
		return
	info.cancel_send_to_server()
	source = info.player if info.is_player else '控制台'
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

	@new_thread('beep')
	def beeeeeeep():
		for name in name_list:
			server.execute('title {} times 2 15 5'.format(name))
			server.execute('title {} title {}'.format(name, text))
		for i in range(2):
			time.sleep(1.0 / 3)
			beep_small(server, info, name_list)

	beeeeeeep()


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


def on_user_info(server: ServerInterface, info: Info):
	if info.is_user and info.content.find('@ ') > -1:
		beep_small(server, info, find_name_list(info.content, '@'))
		beep_big(server, info, find_name_list(info.content, '@@'))


def on_load(server: ServerInterface, old):
	server.register_help_message('@ xxx', '@某人，@ all可作用于所有玩家。使用两个@@小心被打')
