import telebot

bot = telebot.TeleBot('7836824115:AAHI7Ap1ffqhIy2SlMNlEsBngRSYS63jpg0')

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.reply_to(message,'what a beautiful message')

bot.polling(none_stop=True)