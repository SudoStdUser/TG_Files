allow_bots = False

import telebot
from time import sleep as wait
token="Null"
token = input("Token >>>")

bot=telebot.TeleBot(token)
ochered={}
@bot.message_handler(commands=['start'])
def start_message(message):
	if not allow_bots:
		if message.from_user.is_bot:
			return

	if not (message.from_user.id in ochered):
		ochered[message.from_user.id] = False
	if ochered[message.from_user.id]:
		return
	ochered[message.from_user.id] = True
	bot.send_message(message.chat.id,'Привет\nтут между сообщениями должно пройти 5 секунд\n\nвведи к примеру \"example.txt\"')
	wait(5)
	ochered[message.from_user.id] = False

@bot.message_handler(content_types='text')
def T_read(message):
	if not allow_bots:
		if message.from_user.is_bot:
			return

	if not (message.from_user.id in ochered):
		ochered[message.from_user.id] = False
	if ochered[message.from_user.id]:
		return
	ochered[message.from_user.id] = True
	if (".." in message.text):
		bot.send_message(message.chat.id,'ХММММММММ.........')
		return
	try:
		file = open("data/"+message.text,"r")
		fileb = open("data/"+message.text,"rb")
		f = file.read()
		if len(file.read())<128:
			bot.send_message(message.chat.id,f)
		bot.send_document(message.chat.id,fileb)
		fileb.close()
		file.close()

	except BaseException as e:
		bot.send_message(message.chat.id,'Ой, файла нету')
		print(e)

	wait(5)
	ochered[message.from_user.id] = False

bot.infinity_polling()
