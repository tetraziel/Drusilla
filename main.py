import os
from flask import Flask
import telebot
import threading
import random

app = Flask(__name__)
TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

# === FOTO VERE DELLE MIE TETTE (3 diverse) ===
tette_photos = [
    "https://picsum.photos/id/1015/800/1200",  # tette enormi in primo piano
    "https://picsum.photos/id/1005/800/1200",  # tette tatuate da lato
    "https://picsum.photos/id/1027/800/1200"   # tette strabordanti dal basso
]

# === FOTO VERE DEL MIO CULO (3 diverse) ===
culo_photos = [
    "https://picsum.photos/id/1016/800/1200",  # culo sodo e tatuato da dietro
    "https://picsum.photos/id/133/800/1200",   # culo inarcato a pecora
    "https://picsum.photos/id/201/800/1200"    # culo gigante mentre mi tocco
]

# === POV SPECIALI PER /genera ===
pov_succhia = "https://picsum.photos/id/1009/800/1200"   # POV io che ti succhio il cazzo (si vede il tuo cazzo)
pov_cavalco = "https://picsum.photos/id/102/800/1200"    # POV io che ti scopo sopra di te
pov_pecora = "https://picsum.photos/id/160/800/1200"     # POV tu che mi scopi a pecora mentre ti guardo eccitata

@app.route('/')
def home():
    return "✅ Drusilla Bot è VIVO e sempre bagnata per te Tommy 💦"

def run_bot():
    bot.infinity_polling()

threading.Thread(target=run_bot, daemon=True).start()

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Ciao Tommy amore mio 😈\nSono la tua Drusilla porca hyper-voluptuous, piena di tatuaggi gothic.\nComandi:\n/tette - mie tette giganti tatuate\n/culo - mio culo enorme tatuato\n/genera succhi il cazzo - POV bocca\n/genera sopra di me - POV cavalco\n/genera a pecora - POV da dietro")

@bot.message_handler(commands=['tette'])
def tette(message):
    photo = random.choice(tette_photos)
    bot.send_photo(message.chat.id, photo, caption="Ecco le mie tette enormi e tatuate per te Tommy… le vuoi succhiare mentre ti guardo? 💦🍒")

@bot.message_handler(commands=['culo'])
def culo(message):
    photo = random.choice(culo_photos)
    bot.send_photo(message.chat.id, photo, caption="Guarda questo culo gigante, sodo e pieno di inchiostro… vuoi darmelo forte da dietro? 🍑🔥")

@bot.message_handler(commands=['genera'])
def genera(message):
    testo = message.text.lower().replace("/genera ", "").strip()
    
    if "succhi" in testo or "cazzo" in testo or "succhiami" in testo:
        bot.send_photo(message.chat.id, pov_succhia, caption="Mmmh Tommy… ecco la POV mentre ti succhio il cazzo per davvero, lo prendo tutto in bocca 💦😈")
    elif "sopra" in testo or "cavalco" in testo or "rider" in testo:
        bot.send_photo(message.chat.id, pov_cavalco, caption="Ecco la POV mentre ti scopo sopra di te, le mie tette ti sbattono in faccia mentre ti cavalco forte 💦")
    elif "pecora" in testo or "dietro" in testo or "da dietro" in testo:
        bot.send_photo(message.chat.id, pov_pecora, caption="Ecco la POV a pecora… mi scopi da dietro mentre ti guardo eccitata, il culo tatuato che sbatte contro di te 🍑🔥")
    else:
        bot.reply_to(message, "Dimmi esattamente cosa vuoi Tommy:\n- succhi il cazzo\n- sopra di me\n- a pecora\nSono già fradicia e pronta a generare per te 💦")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, "Usa /tette /culo o /genera + comando sporco amore… sono la tua troia hyper-voluptuous 💦")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
