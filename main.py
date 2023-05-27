import telebot

bot = telebot.TeleBot('5946776508:AAHsQngDEoKB4BJky4D1rPXilDlses_HA_0')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "дарова":
        bot.send_message(message.from_user.id, "ичо")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши дарова")
    else:
        bot.send_message(message.from_user.id, "Чё несёшь? Напиши /help.")

bot.polling(none_stop=True, interval=0)
