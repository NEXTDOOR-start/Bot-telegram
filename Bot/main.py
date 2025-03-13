import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def send_message(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Привет! Я бот. Зайдите на моего создателя: [ссылка]")

bot.polling(none_stop=True)
