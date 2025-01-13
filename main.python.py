import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

bot = telebot.TeleBot('7836824115:AAHI7Ap1ffqhIy2SlMNlEsBngRSYS63jpg0')  # Замените на ваш токен

@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    # Создание кнопки с использованием WebAppInfo
    button = KeyboardButton(text='Открыть веб приложение', web_app=WebAppInfo(url='https://pypi.org/project/CurrencyConverter/'))
    markup.add(button)
    bot.send_message(message.chat.id, 'Привет, мой друг', reply_markup=markup)

bot.polling()