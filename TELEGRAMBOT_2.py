import telebot
import requests

from obmen_gui import result

bot = telebot.TeleBot("7322048253:AAFnwogkCMgl_wBxoYaAqlyoeTXmgT2cmAo")


@bot.message_handler(content_types=['text'])
def welcome(pm):
    sent_msg = bot.send_message(pm.chat.id, "Прошу Вас написать валюту, которую хотите обменять (пример: USD)")
    bot.register_next_step_handler(sent_msg, iv_handler)


def iv_handler(pm):
    iv = pm.text
    sent_msg = bot.send_message(pm.chat.id, f"Вами была выбрана валюта {iv}, на какую валюту вы бы хотели ее обменять (пример: RUB)?")
    bot.register_next_step_handler(sent_msg, ov_handler, iv)

def ov_handler(pm, iv):
    ov = pm.text
    bot.send_message(pm.chat.id, f"Ваша валюта {iv}, и вы ее хотите обменять на {ov}.")
    bot.register_next_step_handler(f"На сегодняшний день вы получите{result}?")

def get_ovcount_from_api(iv, ov, count):
    apiurl = f'http://192.168.159.232:8080/obmen?val1={iv}&val2={ov}&count={count}'
    result = requests.get(apiurl)


bot.polling()