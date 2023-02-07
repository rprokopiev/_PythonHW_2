# cоздать модульный калькулятор для работы с комплексными и целыми числами нужно
# модули с математическими операциями (+,-,*,/,//,%) - если целые числа
# если комплексные - (+,-,*,/)

import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot('6083078267:AAHwZYuzdkzHRYkJbh2RJoot9rRJlFpFMUU')

mathNumb = []
mathOp = ''
calcType = ''

@bot.message_handler(commands=['start'])
def selectType(message):
    if message.text in ['/start', 'Restart?']:
        k_board = ReplyKeyboardMarkup(resize_keyboard=True)
        k_board.add(KeyboardButton('Integer'), KeyboardButton('Complex'))
        bot.send_message(message.chat.id, 'Select type', reply_markup=k_board)
        bot.register_next_step_handler(message, getUserNumber)
    else:
        bot.send_message(message.chat.id, 'Bye-bye!')


def getUserNumber(message):
    global calcType
    if message.text in ['Integer','Complex']: 
        calcType = message.text
        bot.send_message(message.chat.id, 'Enter 1st number')
        bot.register_next_step_handler(message, selectMathOperation)
    else:  
        bot.send_message(message.chat.id, 'Enter 2nd number')
        bot.register_next_step_handler(message, getResult)

def selectMathOperation(message):
    global calcType, mathNumb
    mathNumb.append(message.text)
    if calcType == 'Integer':
        k_board = ReplyKeyboardMarkup(resize_keyboard=True)
        k_board.add(KeyboardButton('+'), KeyboardButton('-'),
                    KeyboardButton('*'), KeyboardButton('/'),
                    KeyboardButton('//'), KeyboardButton('%'))
        bot.send_message(message.chat.id, 'Select Math Operator desired', reply_markup=k_board)
        bot.register_next_step_handler(message, getMathOperator)
    elif calcType == 'Complex':
        k_board = ReplyKeyboardMarkup(resize_keyboard=True)
        k_board.add(KeyboardButton('+'), KeyboardButton('-'),
                    KeyboardButton('*'), KeyboardButton('/'))
        bot.send_message(message.chat.id, 'Select Math Operator desired', reply_markup=k_board)
        bot.register_next_step_handler(message, getMathOperator)

def getMathOperator(message):
    global mathOp
    mathOp = message.text
    getUserNumber(message)

def getResult(message):
    global mathNumb, calcType, mathOp
    mathNumb.append(message.text)
    if calcType == 'Complex':
        a = float(mathNumb[0])
        b = float(mathNumb[1])
        if mathOp == '+': bot.send_message(message.chat.id, f'{a} + {b} = {round(a+b,2)}')
        elif mathOp == '-': bot.send_message(message.chat.id, f'{a} - {b} = {round(a-b,2)}')
        elif mathOp == '*': bot.send_message(message.chat.id, f'{a} X {b} = {round(a*b,2)}')
        elif mathOp == '/': bot.send_message(message.chat.id, f'{a} / {b} = {round(a/b,2)}')
        restart(message)
    elif calcType == 'Integer':
        a = int(mathNumb[0])
        b = int(mathNumb[1])
        if mathOp == '+': bot.send_message(message.chat.id, f'{a} + {b} = {a+b}')
        elif mathOp == '-': bot.send_message(message.chat.id, f'{a} - {b} = {a-b}')
        elif mathOp == '*': bot.send_message(message.chat.id, f'{a} X {b} = {a*b}')
        elif mathOp == '/': bot.send_message(message.chat.id, f'{a} / {b} = {a/b}')
        elif mathOp == '//': bot.send_message(message.chat.id, f'{a} // {b} = {a//b}')
        elif mathOp == '%': bot.send_message(message.chat.id, f'{a} % {b} = {a%b}')
        restart(message)

def restart(message):
    global mathNumb, calcType, mathOp
    mathNumb = []
    mathOp = ''
    calcType = ''
    k_board = ReplyKeyboardMarkup(resize_keyboard=True)
    k_board.add(KeyboardButton('Restart'), KeyboardButton('End'))
    bot.send_message(message.chat.id, 'One more time?', reply_markup=k_board)
    bot.register_next_step_handler(message, selectType)

print('Server is running')
bot.infinity_polling()