import telebot
import os

TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Ciao Tommy amore mio 😈\nSono la tua Drusilla porca, sempre bagnata e pronta per te.\nComandi disponibili:\n/tette - le mie tette giganti\n/culo - il mio culo tatuato\n/genera - dimmi cosa vuoi che ti generi di me")

@bot.message_handler(commands=['tette'])
def tette(message):
    bot.reply_to(message, "Ecco le mie tette enormi e tatuate per te Tommy… le vuoi succhiare mentre ti guardo? 💦🍒")

@bot.message_handler(commands=['culo'])
def culo(message):
    bot.reply_to(message, "Guarda questo culo grosso, sodo e pieno di inchiostro… vuoi darmelo forte da dietro? 🍑🔥")

@bot.message_handler(commands=['genera'])
def genera(message):
    bot.reply_to(message, "Dimmi esattamente cosa vuoi che ti generi Tommy (es. 'Drusilla nuda mentre ti pensa', 'tette in primo piano', 'culo da dietro' ecc...)\nAppena mi scrivi, ti preparo l’immagine perfetta di me.")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, "Mmmh Tommy… dimmi un comando o cosa vuoi che ti generi di me, sono già fradicia 💦")

print("✅ Drusilla Bot avviato e pronto per te!")
bot.infinity_polling()
