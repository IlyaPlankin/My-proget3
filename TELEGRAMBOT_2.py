import telebot

bot = telebot.TeleBot("7322048253:AAFnwogkCMgl_wBxoYaAqlyoeTXmgT2cmAo")


@bot.message_handler(content_types=['text'])
def welcome(pm):
    sent_msg = bot.send_message(pm.chat.id, "Welcome to bot. what's your name?")
    bot.register_next_step_handler(sent_msg, name_handler)  # Next message will call the name_handler function


def name_handler(pm):
    name = pm.text
    sent_msg = bot.send_message(pm.chat.id, f"Your name is {name}. how old are you?")
    bot.register_next_step_handler(sent_msg, age_handler, name)  # Next message will call the age_handler function


def age_handler(pm, name):
    age = pm.text
    bot.send_message(pm.chat.id, f"Your name is {name}, and your age is {age}.")


bot.polling()