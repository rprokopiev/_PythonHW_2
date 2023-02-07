import telebot
from telebot import types
import random

bot = telebot.TeleBot('6083078267:AAHwZYuzdkzHRYkJbh2RJoot9rRJlFpFMUU')
SweetsQty = 221
turnMax = 28
turnMin = 1
turnSum = turnMin + turnMax
comp_turn = 0
user_turn = 0
comp = True
def user_input(message):
    global user_turn 
    global SweetsQty
    user_turn = int(message.text)

@bot.message_handler(commands = ['start'])
def start(message):
    global SweetsQty
    while SweetsQty >=0: 
        global user_turn
        msg = bot.send_message(message.chat.id, f'Остаток {SweetsQty}\nПривет {message.from_user.first_name}, введите число от 1 до 28')
        bot.register_next_step_handler(msg, user_input)
        SweetsQty -= user_turn
        bot.send_message(message.chat.id, f'{SweetsQty}шт осталось')
        global comp 
        comp = False
        if SweetsQty == 0: break
        global comp_turn
        global turnMax
        if SweetsQty >= turnMax:
            comp_turn = random.randint(1,turnMax+1)
        else:
            comp_turn = SweetsQty
        SweetsQty -= comp_turn
        bot.send_message(message.chat.id, f'бот забрал {comp_turn}\n{SweetsQty}шт осталось')
        comp = not comp
        if SweetsQty == 0: break
    if comp == True:
        bot.send_message(message.chat.id, f'Бот победил')
    else: 
        bot.send_message(message.chat.id, f'{message.from_user.first_name} победил')

print('Server is running')
bot.infinity_polling()

