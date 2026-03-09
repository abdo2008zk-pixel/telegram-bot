import telebot

TOKEN = "8572750379:AAFX2M1zMOPbwRukw09xMSNvem9gJk4W6cM"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "مرحبا بك في البوت 🤖")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
