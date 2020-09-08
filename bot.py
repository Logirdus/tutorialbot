import telebot, logging
from variables import *
from telebot import types

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.from_user.id, start_mess)


@bot.message_handler(commands=['help'])
def help_handles(message):
    bot.send_message(message.from_user.id, help_mess)
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text="Number one", callback_data="NumberOne")
    but_2 = types.InlineKeyboardButton(text="Number Two", callback_data="NumberTwo")
    but_3 = types.InlineKeyboardButton(text="Number Tree", callback_data="NumberTree")
    key.add(but_1, but_2, but_3)
    bot.send_message(message.chat.id, "Выберите кнопку", reply_markup=key)


@bot.callback_query_handler(func=lambda c:True)
def inline(c):
  if c.data == 'NumberOne':
    bot.send_message(c.message.chat.id, 'Это кнопка 1')
  if c.data == 'NumberTwo':
    bot.send_message(c.message.chat.id, 'Это кнопка 2')
  if c.data == 'NumberTree':
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text="NumberOne", callback_data="NumberOne")
    but_2 = types.InlineKeyboardButton(text="NumberTwo", callback_data="NumberTwo")
    but_3 = types.InlineKeyboardButton(text="NumberTree", callback_data="NumberTree")
    key.add(but_1, but_2, but_3)
    bot.send_message(c.message.chat.id, 'Это кнопка 3', reply_markup=key)


@bot.message_handler(func=lambda message:True)
def forward_handles(message):
    try:
        if message.chat.id == int(CHAT):
            bot.send_message(message.reply_to_message.forward_from.id, message.text)
        else:
            bot.forward_message(CHAT, message.chat.id, message.message_id)
            bot.send_message(message.from_user.id, success_mess)
    except Exception as error:
        print('Exception in forward handler. Info: {}'.format(error))


def main(use_logging, level_name):
    if use_logging:
        telebot.logger.setLevel((logging.getLevelName(level_name)))
    bot.polling(none_stop=True, interval=.5)


if __name__ == '__main__':
    main(True, 'DEBUG')