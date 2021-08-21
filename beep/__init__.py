import re
import time

from mcdreforged.api.all import *


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
	source_name = RText(info.player if info.is_player else server.tr('beep.console'), RColor.aqua)
	title: RTextBase = server.tr('beep.title', source_name)
	subtitle: RTextBase = server.tr('beep.subtitle', source_name)

	@new_thread('beep')
	def beeeeeeep():
		for name in name_list:
			server.execute('title {} times 2 15 5'.format(name))
			server.execute('title {} title {}'.format(name, title.to_json_str()))
			server.execute('title {} subtitle {}'.format(name, subtitle.to_json_str()))
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
	if info.content.find('@ ') > -1:
		beep_small(server, info, find_name_list(info.content, '@'))
		beep_big(server, info, find_name_list(info.content, '@@'))


def on_load(server: PluginServerInterface, old):
	server.register_help_message('@ <someone>', server.get_self_metadata().description)
