# coding:utf-8
import telebot
from telebot import types
import datetime

TOKEN = "899913514:AAEZQTvXBdhnJEJtsPF1xw35ZD1ymvByZ3E"
bot = telebot.TeleBot(TOKEN)
ol = ''
vl = ''
isRunning = False

@bot.message_handler(commands=['start'])
def start_handler(message):
#    global isRunning
#    if not isRunning:
        chat_id = message.chat.id
        bot.send_message(chat_id, 'Привет, я бот.')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Статус')
        markup.row(itembtn1)
        bot.send_message(chat_id, "Выберите пункт главного меню", reply_markup=markup)
 #       isRunning = True


@bot.message_handler(content_types=['text'])
def askMainMenu(message):
    chat_id = message.chat.id
    text = message.text
    global ol
    global vl
    if text == 'Статус':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Установить С')
        itembtn2 = types.KeyboardButton('Установить Х')
        markup.row(itembtn1, itembtn2)
        itembtn3 = types.KeyboardButton('Статус')
        markup.row(itembtn3)
        itembtn4 = types.KeyboardButton('/start',)
        markup.row(itembtn4)
        bot.send_message(chat_id, 'С: ' + ol + '\nХ: ' + vl, reply_markup=markup)
    if text == 'Установить С':
        msg = bot.send_message(chat_id, 'Новый статус для С?')
        bot.register_next_step_handler(msg, setStatusC)
    if text == 'Установить Х':
        msg = bot.send_message(chat_id, 'Новый статус для Х?')
        bot.register_next_step_handler(msg, setStatusH)

def setStatusC(message):
    global ol
    chat_id = message.chat.id
    now = datetime.datetime.now()
    ol = '['+now.strftime("%d-%m-%Y %H:%M")+'] ' + message.text
    bot.send_message(chat_id, 'С: ' + ol + '\nХ: ' + vl)

def setStatusH(message):
    global vl
    chat_id = message.chat.id
    now = datetime.datetime.now()
    vl = '['+now.strftime("%d-%m-%Y %H:%M")+'] ' + message.text
    bot.send_message(chat_id, 'С: ' + ol + '\nХ: ' + vl)

bot.polling()
