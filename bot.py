import telebot
import requests


TOKEN = "Paste Your Token Here"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'hi'])
def send_welcome(message):
	m = message.from_user.username
	bot.reply_to(message, f"Hey, how are you doing {m}?\n\n\nI'm a dictonary bot. if you want to know meaning of any word just type-\n\n\nmeaning word")
	

@bot.message_handler(func=lambda message: True)
def test(msg):
	r = msg.text.split()
	if r[0].lower() == 'meaning':
		word = r[1]
		url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
		req = requests.get(url).json()
		data = req[0]['meanings'][0]['definitions'][0]['definition']
		bot.reply_to(msg, f"it means\n{data}")
	else:
		bot.reply_to(msg, "i didn't get you")

	
	
bot.infinity_polling() 
