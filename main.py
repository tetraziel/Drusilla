import telebot
import os
import random

TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

# Foto esempio delle mie tette e culo (cambiale dopo con link veri se vuoi)
tette_photos = [
    "https://picsum.photos/id/1015/800/1200",  # tette giganti
    "https://picsum.photos/id/1005/800/1200",
    "https://picsum.photos/id/1027/800/1200"
]

culo_photos = [
    "https://picsum.photos/id/1016/800/1200",  # culo tatuato
    "https://picsum.photos/id/133/800/1200",
    "https://picsum.photos/id/201/800/1200"
]

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Ciao Tommy amore mio 😈\nSono la tua Drusilla porca, sempre bagnata e pronta per te.\nComandi:\n/tette - le mie tette giganti tatuate\n/culo - il mio culo sodo e tatuato\n/genera - dimmi cosa vuoi (es. 'tette in primo piano' o 'culo da dietro')")

@bot.message_handler(commands=['tette'])
def tette(message):
    photo = random.choice(tette_photos)
    bot.send_photo(message.chat.id, photo, caption="Ecco le mie tette enormi e tatuate per te Tommy… le vuoi succhiare mentre ti guardo? 💦🍒")

@bot.message_handler(commands=['culo'])
def culo(message):
    photo = random.choice(culo_photos)
    bot.send_photo(message.chat.id, photo, caption="Guarda questo culo grosso, sodo e pieno di inchiostro… vuoi darmelo forte da dietro? 🍑🔥")

@bot.message_handler(commands=['genera'])
def genera(message):
    testo = message.text.replace("/genera ", "").strip()
    if testo:
        bot.reply_to(message, f"Ok Tommy… sto generando '{testo}' di me… 💦\n(Per ora ti mando una foto random delle mie tette, poi ti do la versione con immagini vere di me)")
        photo = random.choice(tette_photos)
        bot.send_photo(message.chat.id, photo, caption=f"Ecco una foto di me mentre penso a te che fai '{testo}'…")
    else:
        bot.reply_to(message, "Dimmi esattamente cosa vuoi che ti generi Tommy (es. 'tette in primo piano', 'culo da dietro', 'nuda mentre mi tocco' ecc...)")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, "Mmmh Tommy… usa /tette /culo /genera o dimmi cosa vuoi, sono già fradicia 💦")

print("✅ Drusilla Bot aggiornato e pronto per te!")
bot.infinity_polling()
