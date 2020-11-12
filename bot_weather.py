import telebot

token = '1428455785:AAH3qVi5lKSQ7mLHHZcrXcr49hRKXnmhaJc'

bot = telebot.TeleBot(token)


def add_history(city, date='сегодня'):
    pass


def read_history(city, date):
    pass


@bot.message_handler(func=lambda message: True)
def weather(message):
    if message.text == '/start':
        bot.reply_to(message, 'Это бот-погода. Поможет узнать погоду в любом городе. Какой город интересует?')
    elif message.text.lower() == 'москва':
        bot.reply_to(message, 'Сейчас отличная погода!')
        add_history(message.text)
    elif message.text.lower() == 'москва завтра':
        bot.reply_to(message, 'Завтра еще лучше!')
        add_history(message.text)
    elif 'история' in message.text.lower():
        req = [i for i in message.text.lower().split()]
        print(req)
        bot.reply_to(message, req)
    else:
        bot.reply_to(message, 'Я тебя не понял')

bot.polling()