#!/usr/bin/env python3

import os
import requests
import shutil
from datetime import datetime
from sys import argv
from time import strftime

date = strftime('%d-%m-%Y')
path = '/home/pi/video/'
hours = range(7, 19)
hour = int(strftime('%H'))
days = ('6', '7')
now = datetime.now()
weekday = str(now.isoweekday())
bot_key = os.getenv['MOTION_KEY']


def sends(pict):
    url = f'https://api.telegram.org/{bot_key}/sendPhoto'
    files = {'photo': open(pict, 'rb')}
    data = {'chat_id': "your_chat_id"}
    requests.post(url, files=files, data=data)


def sensor():
    with open('rid.txt') as f:
        motion = f.read()
        if '1' in motion:
            return True


    fls = os.listdir(path)
    to_move = filter(lambda x: x.endswith('.{ext}'.format(ext=ext)), fls)
    path = r'{dir}{date}'.format(dirs=dirs, date=date)

    if not os.path.exists(path):
        os.makedirs(path)

    for obj in to_move:
        shutil.move('{dir}{fls}'.format(fls=obj, dirs=dirs),
                    '{dir}{date}'.format(dir=dir, date=date))


if (hour not in hours or weekday in days) and sensor():
    sends(argv[1])


moveFiles('avi')
moveFiles('jpg')
