import telebot
from telebot import types
import conf
import requests

bot = telebot.TeleBot(conf.TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):    
    bot.reply_to(message, "Привет, " + message.from_user.first_name + "!")
    bot.send_message(message.chat.id, 'Этот бот умеет присылать треды с ресурса Двач.')
    menu(message)
    
@bot.message_handler(commands=['help'])
def repeat_all_messages(message):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Привет! 👋", callback_data="button1")
    button2 = types.InlineKeyboardButton(text="Кнопка 2", callback_data="button2")
    keyboard.add(button1)
    keyboard.add(button2)

    bot.send_message(message.chat.id, "Нажмите кнопку!", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "button1":
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text="Случайный тред", callback_data="button3")
        button2 = types.InlineKeyboardButton(text="Случайный тред по ключевому слову", callback_data="button4")
        button3 = types.InlineKeyboardButton(text="Вернуться", callback_data="button5")
        
        keyboard.add(button1)
        keyboard.add(button2)
        
        bot.send_message(call.message.chat.id, "Чего ты хочешь?", reply_markup=keyboard)
        
    elif call.data == "button2":
        bot.send_message(call.message.chat.id, "Информация")
        
        menu(call.message)
        
    elif call.data == "button3":
        bot.send_message(call.message.chat.id, "Тред")
        
        menu(call.message)
        
    elif call.data == "button4":
        bot.send_message(call.message.chat.id, "Тред")
        
        menu(call.message)
        
    elif call.data == "button5":
        menu(call.message)
    
def menu(message):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Пришли мне тред", callback_data="button1")
    button2 = types.InlineKeyboardButton(text="О боте", callback_data="button2")
    
    keyboard.add(button1)
    keyboard.add(button2)
    
    bot.send_message(message.chat.id, "Начнём?", reply_markup=keyboard)
        
if __name__ == '__main__':
    bot.polling(none_stop=True)