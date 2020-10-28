# -*- coding: utf-8 -*-
import random
import telebot
bot = telebot.TeleBot('1201165565:AAElTl8352APspMEaZcQhjTQXqDkPdoxq9A')
from telebot import types
import dictionaries

spb_way1_text = dictionaries.spb_way1_text
spb_way1_img = dictionaries.spb_way1_img

@bot.message_handler(commands=["start"])
def get_text_messages(message):
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
def callback_worker(call):
    bot.send_message(call.message.chat.id, "Средний маршрут")
    img = open (u'/ByStepsBot/img_way1_saint_peterburg/s_w1_1.jpg', 'rb')
    bot.send_photo(call.from_user.id, img)

@bot.callback_query_handler(func=lambda call: call.data == "spb_w2")
def callback_worker(call):
    bot.send_message(call.message.chat.id, "Второй маршрут")

@bot.callback_query_handler(func=lambda call: call.data == "kazan")
def callback_worker(call):
        bot.send_message(call.message.chat.id, "Этот город мы скоро загрузим, а пока выбери другой город командой /start")

# Запускаем постоянный опрос бота в Телеграме
if __name__ == '__main__':
    bot.polling(none_stop=True)