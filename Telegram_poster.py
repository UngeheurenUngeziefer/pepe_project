import telepot
import glob
import os

token = ' '
proxies = {'https': '169.51.80.228:3128', 'http': '159.203.82.173:3128'}
telepot.api.set_proxy('https://169.51.80.228:3128')
PosterBot = telepot.Bot(token)

# print(PosterBot.getMe())                             # API request getMe, info about bot
''' {'id': 1279456273, 'is_bot': True, 'first_name': 'Image_Poster', 'username': 'Img_poster_bot',
'can_join_groups': True, 'can_read_all_group_messages': False, 'supports_inline_queries': False} '''

# print(PosterBot.getUpdates())
''' [{'update_id': 103524651, 'message':
    {'message_id': 8, 'from':
        {'id': 477002742, 'is_bot': False, 'first_name': 'Snek', 'username': 'PermanenteDa', 'language_code': 'en'},
     'chat': {'id': 477002742, 'first_name': 'Snek', 'username': 'PermanenteDa', 'type': 'private'},
     'date': 1592476344, 'text': '/start', 'entities': [{'offset': 0, 'length': 6, 'type': 'bot_command'}]}}] '''

# PosterBot.sendMessage('477002742', 'Hey!')            # send me a message
chat_id = '-1001200942722'

# creating list of addresses to all imgs
def img_path(message):
    content_type, chat_type, chat_id_console = telepot.glance(message)
    print(content_type, chat_type, chat_id_console)
    path = 'C:/Users/sewer/MyPython/Pepe_project/downloads'
    img_list = []
    addresses_list = []
    os.chdir(path)
    for file in glob.glob("*.*"):
        img_list.append(file)
    for img in img_list:
        addresses_list.append(path + '/' + img)         # addresses list contain ['address_1', 'address_N' ...]
    for path in addresses_list:
        # return path                                      # return addresses like: './downloads/pepe_10.png'
        try:
            PosterBot.sendPhoto(chat_id, photo=open(path, 'rb'))
            print('Posting {}'.format(path))
        except telepot.exception.TooManyRequestsError:
            print('Too Many Requests')
            continue

MessageLoop(PosterBot, img_path).run_as_thread()
print('Listening ...')

while 1:
    sleep(10)

            
