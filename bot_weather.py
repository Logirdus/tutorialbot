import telebot
from pprint import pprint

token = '1428455785:AAH3qVi5lKSQ7mLHHZcrXcr49hRKXnmhaJc'

bot = telebot.TeleBot(token)
'''
При каждом запуске создается пустой словарь истории запросов вида
{
  "%Город%": {
    "%день%": [
      "Сейчас отличная погода!",
      "..."
    ]
  }
}
'''
history = {}


def add_history(city, forecast, date='сегодня'):
    if city in history:
        if date in history[city]:
            history[city][date].append(forecast)
        else:
            history[city].update({date: [forecast]})
    else:
        history.update({city: {date: [forecast]}})


def read_history(city, date):
    pass


@bot.message_handler(func=lambda message: True)
def weather(message):
    if message.text == '/start':
        bot.reply_to(message, 'Это бот-погода. Поможет узнать погоду в любом городе. Какой город интересует?')
    elif message.text == 'Москва':
        bot.reply_to(message, 'Сейчас отличная погода!')
        add_history(message.text, 'Сейчас отличная погода!')
        pprint(history)
    elif message.text == 'Москва завтра':
        bot.reply_to(message, 'Завтра еще лучше!')
        city = message.text.split()[0]
        date = message.text.split()[1]
        add_history(city, 'Завтра еще лучше!', date)
        pprint(history)
    elif 'история' in message.text.lower():
        req = [i for i in message.text.lower().split()]
        print(req)
        bot.reply_to(message, req)
    else:
        bot.reply_to(message, 'Я тебя не понял')


bot.polling()
