import os
import telebot
from telebot import *
from random import randint
import subprocess
# from dotenv import load_dotenv
# load_dotenv()

# API_KEY = os.getenv('API_KEY')
API_KEY = "1754733850:AAFCv3LzdXpWSOQfocfkRsiYEmLG8eNxKHc"

bot = telebot.TeleBot(API_KEY, parse_mode=None)

@bot.message_handler(commands=['start'])
def start(message):
	bot.reply_to(message, 'Hey there, I am AppGenie!')

@bot.message_handler(commands=['greet', 'hi', 'hey', 'hello'])
def greet(message):
	responses = ['Howdy', 'Hey there', 'Hello', 'Hi back!', 'Hi hi', 'Hello there']
	bot.send_message(message.chat.id, responses[randint(0, len(responses) - 1)])

def die():
	exit()
@bot.message_handler(commands=['killme'])
def killme(message):
	bot.reply_to(message, 'Good Bye.' )
	die()

@bot.message_handler(commands=['open'])
def open_app(message):
	markup = types.ReplyKeyboardMarkup()
	markup.one_time_keyboard=True
	firefox = types.KeyboardButton('FireFox 🌐')
	vscode = types.KeyboardButton('VS Code 💻')
	terminal = types.KeyboardButton('Terminal 📟')
	spotify = types.KeyboardButton('Spotify 🎵')
	whatsapp = types.KeyboardButton('WhatsApp 🟢')
	discord = types.KeyboardButton('Discord 🎮')
	telegram = types.KeyboardButton('FDM ⬇️')
	netflix = types.KeyboardButton('Netflix 📺')
	vlc = types.KeyboardButton('VLC 💿')
	# fdm = types.KeyboardButton('FDM 📲')
	
	markup.row(firefox, vscode, terminal)
	markup.row(spotify, whatsapp, discord)
	markup.row(telegram, netflix, vlc)

	app_to_open = bot.send_message(message.chat.id, 'Which app would like to open?', reply_markup=markup)
	
	bot.register_next_step_handler(app_to_open, start_app)

def start_app(message):
	print(message.text)

	if message.text == 'FireFox 🌐':
		subprocess.call(r'C:\Program Files\Mozilla Firefox\firefox.exe')
	elif message.text == 'VS Code 💻':
		subprocess.call(r'C:\Program Files\Microsoft VS Code\Code.exe')
	elif message.text == 'Terminal 📟':
		subprocess.call(r'C:\Users\JasonPC\AppData\Local\Microsoft\WindowsApps\wt.exe')
	elif message.text == 'Spotify 🎵':
		subprocess.call(r'C:\Users\JasonPC\AppData\Local\Microsoft\WindowsApps\Spotify.exe')
	elif message.text == 'WhatsApp 🟢':
		subprocess.call(r'C:\Users\JasonPC\AppData\Local\WhatsApp\WhatsApp.exe')
	elif message.text == 'Discord 🎮':
		subprocess.call(r'C:\Users\JasonPC\AppData\Local\Discord\app-1.0.9001\Discord.exe')
	elif message.text == 'FDM ⬇️':
		subprocess.call(r'C:\Program Files\FreeDownloadManager.ORG\Free Download Manager\fdm.exe')
	elif message.text == 'Netflix 📺':
		os.system('Start netflix:')
	elif message.text == 'VLC 💿':
		subprocess.call(r'C:\Program Files\VideoLAN\VLC\vlc.exe')

bot.polling()
