# cоздать модульный калькулятор для работы с комплексными и целыми числами нужно
# модули с математическими операциями (+,-,*,/,//,%) - если целые числа
# если комплексные - (+,-,*,/)

import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = telebot.TeleBot('6083078267:AAHwZYuzdkzHRYkJbh2RJoot9rRJlFpFMUU')

def initSelection():
    inline_kb = InlineKeyboardMarkup(row_width=2)
    inline_kb.add(InlineKeyboardButton('Complex #', callback_data='comp'),
                  InlineKeyboardButton('Integer #', callback_data='nat'))
    return inline_kb


@bot.callback_query_handler(func=lambda call: call in ['comp','nat'])
def compMathOper(call):
    global message
    if call.data == 'comp':
        bot.answer_callback_query(call.id, text='Complex #\n')
    elif call.data == 'nat':
        message = 'Integer #'
        bot.answer_callback_query(call.id, text='Integer #')

def complexSelection():
    inline_kb = InlineKeyboardMarkup()
    inline_kb.add(InlineKeyboardButton('+', callback_data='SUM'),
                  InlineKeyboardButton('-', callback_data='SUBTRACTION'),
                  InlineKeyboardButton('*', callback_data='MULTIPLICATION'),
                  InlineKeyboardButton('/', callback_data='DIVISION'))
    return inline_kb

def complexSelection():
    inline_kb = InlineKeyboardMarkup()
    inline_kb.add(InlineKeyboardButton('+', callback_data='SUM'),
                  InlineKeyboardButton('-', callback_data='SUBTRACTION'),
                  InlineKeyboardButton('*', callback_data='MULTIPLICATION'),
                  InlineKeyboardButton('/', callback_data='DIVISION'),
                  InlineKeyboardButton('*', callback_data='INTEGER DIVISION'),
                  InlineKeyboardButton('*', callback_data='REMINDER OF DIVISION'),)
    return inline_kb 
    

@bot.message_handler(commands=['start'])
def selection(message):
    # inline_kb = InlineKeyboardMarkup(row_width=2)
    # inline_kb.add(InlineKeyboardButton(text='Complex #', callback_data='comp'),
    #               InlineKeyboardButton(text='Integer #', callback_data='integ'))
    bot.send_message(message.chat.id, f"Всего в игре bla bla конфет")
    mrk = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    key1 = telebot.types.KeyboardButton("sdf")
    key2= telebot.types.KeyboardButton("sdfsdf")
    mrk.add(key1)
    mrk.add(key2)
    bot.send_message(message.chat.id,"выбери ниже", reply_markup=mrk)
    bot.register_next_step_handler(message,controller)
    # bot.send_message(message.chat.id,'Select type of number', reply_markup=inline_kb)
    # bot.register_next_step_handler(message.chat.id, controller)
    
def controller(message):
    # if message.text == 'Complex #': 
    bot.send_message(message.chat.id,'Complex #')
    # elif message.text == 'Natural #':
    #     bot.send_message(message.chat.id,'Integer #')
    mrk = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    key1 = telebot.types.KeyboardButton("bla1")
    key2= telebot.types.KeyboardButton("bla2")
    mrk.add(key1)
    mrk.add(key2)
    bot.send_message(message.chat.id,"выбери ниже", reply_markup=mrk)
    bot.register_next_step_handler(message,bla)
   
def bla(message):
    # if message.text == 'Complex #': 
    bot.send_message(message.chat.id,'BLA #')


print('Server is running')
bot.infinity_polling()