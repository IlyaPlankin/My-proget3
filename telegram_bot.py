import telebot
import requests
api_token = '7322048253:AAFnwogkCMgl_wBxoYaAqlyoeTXmgT2cmAo'


bot = telebot.TeleBot(api_token)

@bot.message_handler(commands=['start'])
def get_weather(message):
    bot.send_message(message.chat.id, text=f'Hello')

def get_ovcount_from_api(iv, ov, count):
    apiurl = f'http://192.168.159.232:8080/obmen?val1={iv}&val2={ov}&count={count}'
    result = requests.get(apiurl)
    result_sring = result.text
    result_elem = window['result']
    result_elem.update(result_sring)


@bot.message_handler(commands=['get_weather', 'weather', 'pogoda'])
def get_weather(message):
    bot.send_message(message.chat.id, text=f'.....')
bot.polling(none_stop=True)