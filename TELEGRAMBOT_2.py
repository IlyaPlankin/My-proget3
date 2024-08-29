import telebot
import requests

from Give_text_web import result

bot = telebot.TeleBot("7322048253:AAFnwogkCMgl_wBxoYaAqlyoeTXmgT2cmAo")


@bot.message_handler(content_types=['text'])
def welcome(pm):
    sent_msg = bot.send_message(pm.chat.id, "Прошу Вас написать валюту, которую хотите обменять (пример: USD)")
    bot.register_next_step_handler(sent_msg, iv_handler)

def iv_handler(pm):
    iv = pm.text
    sent_msg = bot.send_message(pm.chat.id, f"Вами была выбрана валюта {iv}, на какую валюту вы бы хотели ее обменять (пример: RUB)?")
    bot.register_next_step_handler(sent_msg, ov_handler, iv)

def ov_handler(pm,iv):
    ov = pm.text
    sent_msg = bot.send_message(pm.chat.id, f"Вами была выбрана валюта {ov}, сколько вы хотите обменять (только цифры)?")
    bot.register_next_step_handler(sent_msg, count_handler,iv, ov)

def count_handler(pm, iv,ov):
    count = pm.text
    print(iv,ov)
    result = get_ovcount_from_api(iv, ov, count)
    sent_msg = bot.send_message(pm.chat.id,f"На сегодняшний день вы получите{result}?")


def get_ovcount_from_api(iv, ov, count):
    iv = iv.upper()
    ov = ov.upper()
    apiurl = f'http://192.168.207.232:8080/obmen/?val1={iv}&val2={ov}&count={count}'
    print(apiurl)
    #result = requests.get(apiurl)
    return "125 EUR"

bot.polling()