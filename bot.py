import telebot

TOKEN = "PUT_YOUR_NEW_TOKEN_HERE"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "اهلا بك في البوت 🤖")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
