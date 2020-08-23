import config
import telebot
import requests
from bs4 import BeautifulSoup as BS
from colorama import Fore

bot = telebot.TeleBot(config.token)

r = requests.get('https://sinoptik.ua/погода-винница')
html = BS(r.content, 'html.parser')


for el in html.select('#content'):
    t_minV = el.select('.temperature .min')[0].text
    t_maxV = el.select('.temperature .max')[0].text
    textV = el.select('.wDescription .description')[0].text
for el in html.select('#bd1'):
    date = el.select('.date')[0].text
    print(t_minV + ', ' + t_maxV + '\n' + textV + '\n', date )
    unreal1 = ('Погода в Виннице на :' + ' ' + str(date) + ' ' + 'число' + '\n', t_minV, t_maxV, textV)
    print(unreal1)



#parsing Kiev Weather

r = requests.get('https://sinoptik.ua/погода-киев')
html = BS(r.content, 'html.parser')


for el in html.select('#content'):
    t_min = el.select('.temperature .min')[0].text
    t_max = el.select('.temperature .max')[0].text
    text = el.select('.wDescription .description')[0].text
for el in html.select('#bd1'):
    date = el.select('.date')[0].text
    print(t_min + ', ' + t_max + '\n' + text + '\n', date )
    unreal2 = ('Погода в Киеве на :' + ' ' + str(date) + ' ' + 'число' + '\n', t_min, t_max, text)
    print(unreal2)


#parsing Lviv weather from sinoptic.com

r = requests.get('https://sinoptik.ua/погода-львов')
html = BS(r.content, 'html.parser')


for el in html.select('#content'):
    t_min = el.select('.temperature .min')[0].text
    t_max = el.select('.temperature .max')[0].text
    text = el.select('.wDescription .description')[0].text
for el in html.select('#bd1'):
    date = el.select('.date')[0].text
    print(t_min + ', ' + t_max + '\n' + text + '\n', date )
    unreal3 = ('Погода во Львове на :' + ' ' + str(date) + ' ' + 'число' + '\n', t_min, t_max, text)
    print(unreal3)





# parsing kharkov weather fom sinoptik.c0m


r = requests.get('https://sinoptik.ua/погода-харьков')
html = BS(r.content, 'html.parser')


for el in html.select('#content'):
    t_min = el.select('.temperature .min')[0].text
    t_max = el.select('.temperature .max')[0].text
    text = el.select('.wDescription .description')[0].text
for el in html.select('#bd1'):
    date = el.select('.date')[0].text
    print(t_min + ', ' + t_max + '\n' + text + '\n', date )
    unreal4 = ('Погода в Харькове на :' + ' ' + str(date) + ' ' + 'число' + '\n', t_min, t_max, text)
    print(unreal4)



#parsing Odessa weather from sinoptik.com

r = requests.get('https://sinoptik.ua/погода-одесса')
html = BS(r.content, 'html.parser')


for el in html.select('#content'):
    t_min = el.select('.temperature .min')[0].text
    t_max = el.select('.temperature .max')[0].text
    text = el.select('.wDescription .description')[0].text
for el in html.select('#bd1'):
    date = el.select('.date')[0].text
    print(t_min + ', ' + t_max + '\n' + text + '\n', date )
    unreal5 = ('Погода в Одессе на :' + ' ' + str(date) + ' ' + 'число' + '\n', t_min, t_max, text)
    print(unreal5)

#parsing IF weather from sinoptik.com


r = requests.get('https://sinoptik.ua/погода-ивано-франковск')
html = BS(r.content, 'html.parser')


for el in html.select('#content'):
    t_min = el.select('.temperature .min')[0].text
    t_max = el.select('.temperature .max')[0].text
    text = el.select('.wDescription .description')[0].text
for el in html.select('#bd1'):
    date = el.select('.date')[0].text
    print(t_min + ', ' + t_max + '\n' + text + '\n', date )
    unreal6 = ('Погода в Ивано-Франковске на :' + ' ' + str(date) + ' ' + 'число' + '\n', t_min, t_max, text)
    print(unreal6)

########################################################################################################################aaa
