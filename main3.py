import config
import telebot
import requests
from bs4 import BeautifulSoup as BS
from colorama import Fore
from weathers import unreal1, unreal2, unreal3, unreal4, unreal5, unreal6
from weathers import t_minV, t_maxV, textV

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['help'])
def main2(message):
    bot.send_message(message.chat.id, 'Привет это бот погоды на  день, для того чтобы посмотреть погоду выбери город: ')


keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard2 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Погода Винница', 'Погода Киев')
keyboard1.row('Погода ЛЬвов', 'Погода Харьков')
keyboard1.row('Погода Одесса', 'Погода Ивано-Франковск')
keyboard1.row('Информация о COVID-19', 'COVID-19 в Мире')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start , я бот созданный для \n'
                                      'погоды в разных городах и информации об COVID-19', reply_markup=keyboard1)


# parsing covid achivements in ukraine
r = requests.get('https://covid19.gov.ua/')
html = BS(r.content, 'html.parser')

for el in html.select('.one-field light-box info-count'):
    aprove_ua = el.select('.field-value')[0].text
    print(aprove_ua)
    cov_ua = ('Подтверждённых случаев заболевания в Укриане : ', + ' ' + str(aprove_ua))
    print(cov_ua)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'погода винница':
        bot.send_message(message.chat.id, '\n'.join(unreal1))
    elif message.text.lower() == 'погода киев':
        bot.send_message(message.chat.id, '\n'.join(unreal2))
    elif message.text.lower() == 'погода львов':
        bot.send_message(message.chat.id, '\n'.join(unreal3))
    elif message.text.lower() == 'погода харьков':
        bot.send_message(message.chat.id, '\n'.join(unreal4))
    elif message.text.lower() == 'погода одесса':
        bot.send_message(message.chat.id, '\n'.join(unreal5))
    elif message.text.lower() == 'погода ивано-франковск':
        bot.send_message(message.chat.id, '\n'.join(unreal6))
    elif message.text.lower() == 'информация о covid-19':
        bot.send_message(message.chat.id,
                         'Для полного обзора ситуации в Украине,перейдите по ссылке https://covid19.gov.ua/ ')
    elif message.text.lower() == 'covid-19 в мире':
        bot.send_message(message.chat.id,
                         'Для полного обзора ситуации в мире перейдите по ссылке https://index.minfin.com.ua/reference/coronavirus/geography/')


if __name__ == '__main__':
    bot.polling(none_stop=True)
