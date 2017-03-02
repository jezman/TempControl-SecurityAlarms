#!/usr/bin/env python3

import os
import requests
import shutil
from datetime import datetime
from sys import argv
from time import strftime

date = strftime('%d-%m-%Y')
dir = '/video/'
hours = range(7, 19)
hour = int(strftime('%H'))
days = ('6', '7')
now = datetime.now()
weekday = str(now.isoweekday())


def sends(path):
    url = "https://api.telegram.org/botYour_bot_id/sendPhoto"
    files = {'photo': open(path, 'rb')}
    data = {'chat_id': "your_chat_id"}
    requests.post(url, files=files, data=data)


def sensor():
    fl = open('rid.txt')
    motion = fl.read()
    if '1' in motion:
        return True


def moveFiles(ext):
    fls = os.listdir(dir)
    to_move = filter(lambda x: x.endswith('.{ext}'.format(ext=ext)), fls)
    path = r'{dir}{date}'.format(dir=dir, date=date)

    if not os.path.exists(path):
        os.makedirs(path)

    for obj in to_move:
        shutil.move('{dir}{fls}'.format(fls=obj, dir=dir),
                    '{dir}{date}'.format(dir=dir, date=date))


if (hour not in hours or weekday in days) and sensor():
    sends(argv[1])


moveFiles('avi')
moveFiles('jpg')
