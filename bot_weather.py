import telebot

token = '1428455785:AAH3qVi5lKSQ7mLHHZcrXcr49hRKXnmhaJc'

bot = telebot.TeleBot(token)

'''
словарь истории запросов history вида:
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
    # функция добавляет запись в историю запросов погоды
    # параметры город, прогноз, дата(по умолчанию = сегодня)
    if city in history:
        if date in history[city]:
            history[city][date].append(forecast)
        else:
            history[city].update({date: [forecast]})
    else:
        history.update({city: {date: [forecast]}})


def read_history(city, date):
    # функция возвращает до 3х последних запросов из истории
    # параметры город, дата
    # если запросов для города/даты не было возвращает соответствующее сообщение
    if city not in history:
        callback = f'История запросов для города "{city}" пуста'
    elif date not in history[city]:
        callback = f'История запросов для города "{city}" за дату "{date}" пуста'
    else:
        callback = f'История погоды для города {city}:\n{date}\n\n'
        history_size = len(history[city][date])
        if history_size < 3:
            for i in range(history_size):
                callback += history[city][date][-i] + '\n'
        else:
            for i in range(1, 4):
                callback += history[city][date][-i] + '\n'
        callback += f'\nВсего запросов {history_size}'

    return callback


@bot.message_handler(func=lambda message: True)
def weather(message):
    if message.text == '/start':
        bot.reply_to(message, 'Это бот-погода. Поможет узнать погоду в любом городе. Какой город интересует?')
    elif message.text == 'Москва':
        bot.reply_to(message, 'Сейчас отличная погода!')
        add_history(message.text, 'Сейчас отличная погода!')
    elif message.text == 'Москва завтра':
        bot.reply_to(message, 'Завтра еще лучше!')
        city = message.text.split()[0]
        date = message.text.split()[1]
        add_history(city, 'Завтра еще лучше!', date)
    # запрос истории 'история %Город% %день%'
    elif 'история' in message.text.lower():
        city = message.text.split()[1]
        date = message.text.split()[2]
        bot.reply_to(message, read_history(city, date))
    else:
        bot.reply_to(message, 'Я тебя не понял')


bot.polling()
