import telebot
import requests
import os

TOKEN = "8572750379:AAFpzAgYabB6mE4q7L_QGmrQobjPyImY4Zs"
API = os.getenv("SHRINKME_API")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "ارسل أي رابط وسأقوم بتقصيره لك 💰")

@bot.message_handler(func=lambda message: True)
def shorten(message):
    url = message.text
    
    r = requests.get(f"https://shrinkme.io/api?api={API}&url={url}")
    data = r.json()

    if data["status"] == "success":
        bot.reply_to(message, data["shortenedUrl"])
    else:
        bot.reply_to(message, "حدث خطأ في تقصير الرابط")

bot.infinity_polling()
