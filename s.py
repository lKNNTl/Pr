import telebot as tb
from telebot import types
import random as rd
import time
import datetime as dt
import logging
import sqlite3
import os

# Сценарии
priv = ['Добрый день, товарищ', 'Приветствую вас', 'Здравтсуйте, друг мой', 'День добрый', 'Хэллоу']
net = ['Извините, отказано', 'Ответ системы - "Нет"', 'Товарищ, отказано']
da = ['Статус - "ДА', 'Естествено', 'TRUE (Da)']
bot_pohval = ['Лучший помощник', 'JARVIS только лучше', 'Супер мега пупер помощник', 'Танос среди помщников в мире']
fakt = [['Интересный факт: Первый человек в космоесу был из СССР', 'Факт про космос'],
        ['В начале у тебя 20 отчимов', 'Факт про дотеров']]

# Токен бота
token = '6282629918:AAGxRTkieARpHeQyliDtn4y0k2UHr8Wh4wE'
bot = tb.TeleBot(token)

# Уведомление о запуске
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


# Факт
def fak(message):
    if 1 == rd.randint(0, 5):
        bot.send_message(message.chat.id, f'{fakt[rd.randint(0, 1)][1]}. Хотите узнать?')


# Подтверждение о готовности
@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = types.KeyboardButton('Да')
    b2 = types.KeyboardButton('Нет')
    b4 = types.KeyboardButton('Почему такое название бота?')
    b3 = types.KeyboardButton('Сайт - для регистрации.')
    keyboard.add(b1, b2, b3, b4)
    bot.send_message(message.chat.id, f'{priv[rd.randint(0, 4)]}. Вы готовы к общению?', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def keyboard_gotov(message):
    if message.text == 'Сайт - для регистрации.':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b2 = types.KeyboardButton('Назад в ад')
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Сайт Хабр", url='http://127.0.0.1:8080/')
        button2 = types.InlineKeyboardButton("Сайт Хабр правила", url='http://127.0.0.1:8080/rules')
        button3 = types.InlineKeyboardButton("Сайт Хабр регистрация", url='http://127.0.0.1:8080/Cams')
        markup.add(button1, button2, button3)
        keyboard.add(b2)

        a = bot.send_message(message.chat.id,
                             f"Сэр {message.from_user.username} - Лучше всего перейти на сайт по кнопке")
        a1 = bot.send_photo(message.chat.id,
                            'https://www.meme-arsenal.com/memes/8813fd8b7aa8f1efd97c435c679fa3e1.jpg'.format(
                                message.from_user),
                            reply_markup=markup)
        a2 = bot.send_audio(message.chat.id,
                            'https://cs1-65v4.vkuseraudio.net/p4/e3d1633c928938.mp3?extra=UwZawvd-y72N_CZYKP_lO04smUYKNGu3zxoXpl2drPQrkQ_PQpmg1ZsnEiMuElrCudU3abDH4V95MNh3aCNhU067lyStRejERVIJIJRQYUCRtA1KIL6q8hOK1Gtp1shMJhCNrCtovzc-IAENvvhsoNAp&long_chunk=1',
                            reply_markup=keyboard)

        # Готов
    if message.text == 'Почему такое название бота?':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        n1 = bot.send_message(message.chat.id, 'А тебе это важно?', reply_markup=keyboard)
        time.sleep(1)
        n2 = bot.send_photo(message.chat.id,
                            'https://risovach.ru/upload/2014/06/mem/tvoe-vyrazhenie-lica_53549909_orig_.jpeg')
        time.sleep(2)
        n3 = bot.send_message(message.chat.id, 'Всё поняли.....')
        n = [n1, n2, n3]
        for i in n:
            time.sleep(1.6)
            bot.delete_message(message.chat.id, i.id)
        start_message(message)
        # Помощник

    if message.text == 'Нет':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, 'Всмысле не можешь.', reply_markup=keyboard)
        time.sleep(2)
        bot.send_photo(message.chat.id,
                       'https://risovach.ru/upload/2014/01/mem/kakoy-pacan_41226535_orig_.jpeg')
        b1 = types.KeyboardButton('Назад в ад')
        b2 = types.KeyboardButton('Хотите факт')
        b3 = types.KeyboardButton('О боте')
        keyboard.add(b1, b3, b2)
        bot.send_message(message.chat.id, f'Куда дальше',
                         reply_markup=keyboard)

    if message.text == 'Хотите факт':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        c = types.KeyboardButton('Назад в ад')
        c1 = types.KeyboardButton('Точнее')
        keyboard.add(c, c1)
        r = rd.randint(0, 4)
        m = bot.send_message(message.chat.id, f'Хотите факт о {fakt[r][1]}',
                             reply_markup=keyboard)

    if message.text == 'Точнее':
        bot.delete_message(message.chat.id, m.id)
        bot.send_message(message.chat.id, f'Хотите факт о {fakt[r][2]}',
                         reply_markup=keyboard)

    if message.text.lower() == 'о боте':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bn1 = bot.send_message(message.chat.id,
                               f'{priv[rd.randint(0, 3)]} Если вы не поняли то я......{priv[rd.randint(0, 3)]}')
        bn2 = bot.send_photo(message.chat.id,
                             'https://timeweb.com/ru/community/article/f9/f9126325726f89cede1e0ec2c3f8e501.jpg',
                             message.id)
        b1 = types.KeyboardButton('Понял')
        keyboard.add(b1)
        bn3 = bot.send_message(message.chat.id, f'Я есть {bot_pohval[rd.randint(0, 3)]}', reply_markup=keyboard)

    if message.text == 'Назад в ад':
        start_message(message)

    if message.text == 'Понял':
        # for i in range(2):
        bot.delete_message(message.chat.id, bn1.id)
        time.sleep(3)
        bot.delete_message(message.chat.id, bn2.id)
        time.sleep(3)
        bot.delete_message(message.chat.id, bn3.id)
        time.sleep(3)
        start_message(message)

    if message.text == 'Да':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b1 = types.KeyboardButton('Добавить')
        b2 = types.KeyboardButton('Изменить')
        b3 = types.KeyboardButton('Узнать')
        b4 = types.KeyboardButton('Назад в ад')
        keyboard.add(b1, b2, b3, b4)
        bot.send_message(message.chat.id, 'Выберети что хотите сделать', reply_markup=keyboard)

    if message.text == 'Узнать':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, 'Введите логин и пароль')
        bot.register_next_step_handler(message, car_name)

    if message.text == 'Добавить':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, 'Введите новый - логин и пароль')
        bot.register_next_step_handler(message, new_name)

    if message.text == 'Изменить':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, 'Введите логи и пароль того пользватеоя которого хотите изменить')
        bot.register_next_step_handler(message, up_name)


def new_name(message):
    import os
    name, pasword = map(str, message.text.split())
    # name = input()
    # pasword = input()
    if f'{name}.txt' not in os.listdir():
        print(os.listdir())
        with open(f"{name}.txt", "a"):
            pass
        with open(f'{name}.txt', 'w') as fp:
            sps = fp.write(pasword)


def up_name(message):
    name, pasword = map(str, message.text.split())
    if f'{name}.txt' in os.listdir():
        print(os.listdir())
        with open(f'{name}.txt', 'w') as fp:
            sps = fp.write(new_pasword)


def car_name(message):
    name, pasword = map(str, message.text.split())
    # name = input()
    # pasword = input()
    with open(f'{name}.txt', 'r') as fp:
        NAST_PASSWORD = fp.readlines()
    if [pasword] == NAST_PASSWORD:
        print('Верено')
    else:
        print('Неверно')


bot.polling(non_stop=True)
