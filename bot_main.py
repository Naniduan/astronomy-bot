import telebot
from telebot import types
from user import *
from bodies import *
from moment import *
from get_moons_position import *
from datetime import *
from math import floor

bot = telebot.TeleBot('')

users = dict()

@bot.message_handler(commands=['start'])
def start_message(message):
    global users
    
    bot.send_message(message.chat.id,"Здравствуйте!")

    user = User(message.chat.id)
    users[message.chat.id] = user

    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("телескоп-рефрактор")
    item2 = types.KeyboardButton("бинокль")
    markup.add(item1)
    markup.add(item2)

    bot.send_message(message.chat.id, "выберете ваш тип оборудования", reply_markup=markup)

@bot.message_handler(commands=['jovian_moons'])
def jovian_moons(message):
    dt = datetime.utcnow()
    pos = get_moons_position(dt)
    
    ans = ['-']*70
    ans[floor(pos.io_x)+30] = 'i'
    ans[floor(pos.europa_x)+30] = 'e'
    ans[floor(pos.ganymede_x)+30] = 'g'
    ans[floor(pos.callisto_x)+30] = 'c'
    ans[30] = 'O'

    ansstr = ''
    for i in ans: ansstr+=i
    ansstr += "\nO - Юпитер\ni - Ио\ne - Европа\ng - Ганимед\nc - Каллисто"

    bot.send_message(message.chat.id, ansstr)

    

@bot.message_handler(content_types='text')
def text_handler(message):
    global users
    
    if message.text in ("телескоп-рефрактор", "бинокль"):
        users[message.chat.id].set_gadget_type(message.text)
        bot.send_message(message.chat.id, "напишите фокусное расстояние натуральным числом")
    else:
        users[message.chat.id].set_gadget_focus(int(message.text))
        bot.send_message(message.chat.id, "у вас " + users[message.chat.id].gadget_type + " с фокусным расстоянием " + str(users[message.chat.id].gadget_focus))

    
bot.infinity_polling()
