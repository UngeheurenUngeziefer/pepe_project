from telegram.ext import Updater, CommandHandler

import requests
import re
import glob
import os

proxies = {'https': '169.51.80.228:3128',
           'http': '159.203.82.173:3128'}

TOKEN = '1279456273:AAECOMcJPNP7x5G5sD4zIzQukDcy34sG5KU'
MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'

chat_id = '-1001200942722'

# creating list of addresses to all imgs
def img_path():
    path = './downloads'
    img_list = []
    addresses_list = []

    os.chdir(path)
    for file in glob.glob("*.*"):
        img_list.append(file)
    for img in img_list:
        addresses_list.append(path + '/' + img)
    # print(addresses_list)
    for path in addresses_list:
        return path

def bop(bot, update):
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=img_path())

def main():
    updater = Updater('1279456273:AAECOMcJPNP7x5G5sD4zIzQukDcy34sG5KU')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop', bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()




