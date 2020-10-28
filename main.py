# -*- coding: utf-8 -*-
import random
import telebot
bot = telebot.TeleBot('1201165565:AAElTl8352APspMEaZcQhjTQXqDkPdoxq9A')
from telebot import types
import dictionaries


spb_way1_text = dictionaries.spb_way2_text
spb_way1_img = dictionaries.spb_way2_img
url = "https://raw.githubusercontent.com/ChKtn/BySteps/master/"
url_p = "img_way1_saint_peterburg/"
i = 0
len =  dictionaries.spb_way2_len
#dictionaries.spb_way1_len

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.from_user.id, "Привет")  # Готовим кнопки
    # По очереди готовим текст и обработчик для каждого знака зодиака
    keyboard = types.InlineKeyboardMarkup()
    key_spb = types.InlineKeyboardButton(text='Санкт-Петербург', callback_data='spb')
    # И добавляем кнопку на экран
    keyboard.add(key_spb)
    key_kazan = types.InlineKeyboardButton(text='Казань', callback_data='kazan')
    keyboard.add(key_kazan)
    # Показываем все кнопки сразу и пишем сообщение о выборе
    bot.send_message(message.from_user.id, text='Выбери город в котором хочешь погулять', reply_markup=keyboard)

    # Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: call.data == "spb")
def callback_worker(call):
    bot.send_message(call.message.chat.id, "Санкт-Петербург! Культурная столица России)")
    keyboard_spb = types.InlineKeyboardMarkup()
    key_spb_w1 = types.InlineKeyboardButton(text='Средний маршрут (~1ч)', callback_data='spb_w1')
    keyboard_spb.add(key_spb_w1)
    key_spb_w2 = types.InlineKeyboardButton(text='Длинный маршрут (~2ч)', callback_data='spb_w2')
    keyboard_spb.add(key_spb_w2)
    bot.send_message(call.from_user.id, text='Выбери маршрут', reply_markup=keyboard_spb)

@bot.callback_query_handler(func=lambda call: call.data == "spb_w1")
def callback_worker_spb_w1(call):
    bot.send_message(call.message.chat.id, "Средний маршрут")
    keyboard = types.InlineKeyboardMarkup()
    key_w1 = types.InlineKeyboardButton(text='Начинаем!', callback_data="next_place")
    keyboard.add(key_w1)
    bot.send_photo(call.from_user.id, url+url_p+spb_way1_img[0], spb_way1_text[0], reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data=="next_place")
def next_place(call):
    global i
    i += 1
    if i == len:
        bot.send_photo(call.from_user.id, url + spb_way1_img[i], spb_way1_text[i])
        bot.send_message(call.message.chat.id, "Надеемся, что прогулка вам понравилась!")
        start(call.message)
    keyboard_spb = types.InlineKeyboardMarkup()
    key_w1 = types.InlineKeyboardButton(text='Следующее место', callback_data="next_place")
    keyboard_spb.add(key_w1)
    bot.send_photo(call.from_user.id, url +url_p+ spb_way1_img[i], spb_way1_text[i], reply_markup=keyboard_spb)

@bot.callback_query_handler(func=lambda call: call.data == "spb_w2")
def callback_worker_spb_w2(call):
    bot.send_message(call.message.chat.id, "Второй маршрут")

@bot.callback_query_handler(func=lambda call: call.data == "kazan")
def callback_worker_kazan(call):
        bot.send_message(call.message.chat.id, "Этот город мы скоро загрузим, а пока выбери другой город командой /start")

# Запускаем постоянный опрос бота в Телеграме
if __name__ == '__main__':
    bot.polling(none_stop=True)