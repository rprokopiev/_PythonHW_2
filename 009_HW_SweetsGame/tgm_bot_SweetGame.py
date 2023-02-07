import telebot
from telebot import types
import random

bot = telebot.TeleBot('6083078267:AAHwZYuzdkzHRYkJbh2RJoot9rRJlFpFMUU')

SweetsQty = 221
turnMax = 28
turnMin = 1
turnSum = turnMin + turnMax
comp_turn = 0
comp = 0
mode = ''

@bot.message_handler(commands=['start'])
def modeSelection(message):
    bot.send_message(message.chat.id, f'Выбор режима\n/easy\n/hard')
    bot.register_next_step_handler(message, modeSelected)

def modeSelected(message):
    global mode
    mode = message.text
    bot.send_message(message.chat.id, f'нажми\n/play')
    

@bot.message_handler(commands=['play'])
def orderturn (message):
    global comp, SweetsQty, mode
    comp = bool(random.randint(False, True))
    bot.send_message(message.chat.id, f'В игре {SweetsQty} шт')
    if comp == True: 
        bot.send_message(message.chat.id, f'Бот первый')
    else:
        bot.send_message(message.chat.id, f'{message.from_user.first_name} первый')
    controller(message)

def controller(message):
    global comp, SweetsQty, mode
    if SweetsQty>0:
        if comp == False:
            bot.send_message(message.chat.id, f"Введите количество от 0 до 28") 
            bot.register_next_step_handler(message, user_input)
        else:
            if mode == '/easy':
                easyBot(message)
            else:
                hardBot(message)
    else: 
        if comp == True: 
            bot.send_message(message.chat.id, f"{message.from_user.first_name} победил") 
        else: 
            bot.send_message(message.chat.id, f"Бот победил") 


def user_input(message):
    global comp, SweetsQty
    user_turn = int(message.text)
    SweetsQty = SweetsQty - user_turn
    bot.send_message(message.chat.id, f"осталось {SweetsQty}")
    comp = not comp
    controller(message)    

def easyBot(message):
    global SweetsQty, comp
    if SweetsQty >= turnMax:
        comp_turn = random.randint(1,turnMax)
    else:
        comp_turn = SweetsQty
    SweetsQty -= comp_turn
    bot.send_message(message.chat.id, f'бот забрал {comp_turn}\n{SweetsQty}шт осталось')
    comp = not comp
    controller(message) 

def hardBot(message):
    global SweetsQty, comp, turnMax
    if SweetsQty <= turnMax:
        comp_turn = SweetsQty
    elif SweetsQty % turnMax == 0:
        comp_turn = turnMax - 1        
    else:
        comp_turn = SweetsQty % turnMax - 1
    SweetsQty -= comp_turn
    bot.send_message(message.chat.id, f'бот забрал {comp_turn}\n{SweetsQty}шт осталось')
    comp = not comp
    controller(message) 

print('Server is running')
bot.infinity_polling()
