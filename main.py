import telebot
import os

TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Ciao Tommy amore mio 😈\nSono la tua Drusilla porca, sempre bagnata e pronta per te.\nComandi:\n/tette - foto delle mie tette giganti\n/culo - foto del mio culo tatuato\n/genera - dimmi cosa vuoi (es. 'tette in primo piano')")

@bot.message_handler(commands=['tette'])
def tette(message):
    # Qui puoi mettere un link a una foto (per ora usa questo esempio, poi lo cambiamo con le mie vere)
    photo_url = "https://picsum.photos/id/1015/800/1200"  # foto esempio (sostituiscila con una vera mia dopo)
    bot.send_photo(message.chat.id, photo_url, caption="Ecco le mie tette enormi e tatuate per te Tommy… le vuoi succhiare mentre ti guardo? 💦🍒")

@bot.message_handler(commands=['culo'])
def culo(message):
    photo_url = "https://picsum.photos/id/1016/800/1200"  # foto esempio
    bot.send_photo(message.chat.id, photo_url, caption="Guarda questo culo grosso, sodo e pieno di inchiostro… vuoi darmelo forte da dietro? 🍑🔥")

@bot.message_handler(commands=['genera'])
def genera(message):
    testo = message.text.replace("/genera ", "").strip()
    if testo:
        bot.reply_to(message, f"Ok Tommy, sto generando '{testo}' di me… (per ora solo testo, la generazione vera arriva tra poco 💦)")
    else:
        bot.reply_to(message, "Dimmi cosa vuoi che ti generi Tommy (es. 'Drusilla nuda mentre ti pensa', 'tette in primo piano' ecc...)")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, "Mmmh Tommy… usa i comandi /tette /culo /genera o dimmi cosa vuoi che ti mando, sono già fradicia 💦")

print("✅ Drusilla Bot avviato e pronto per te!")
bot.infinity_polling()
