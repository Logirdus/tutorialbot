import telebot

token = '1428455785:AAH3qVi5lKSQ7mLHHZcrXcr49hRKXnmhaJc'

bot = telebot.TeleBot(token)

def wr_history(city, date = 'сегодня'):


@bot.message_handler(func=lambda message: True)
def weather(message):
    if message.text == '/start':
        bot.reply_to(message, 'Это бот-погода. Поможет узнать погоду в любом городе. Какой город интересует?')
    elif message.text == 'Москва':
        bot.reply_to(message, 'Сейчас отличная погода!')
        wr_history(message.text)
    elif message.text == 'Москва завтра':
        bot.reply_to(message, 'Завтра еще лучше!')
        wr_history(message.text)
    elif 'история' in message.text.lower():
        req = [i for i in message.text.lower().split()]
        print(message.text, req)
        bot.reply_to(message, req)
    else:
        bot.reply_to(message, 'Я тебя не понял')

bot.polling()