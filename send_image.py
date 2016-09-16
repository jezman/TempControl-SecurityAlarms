#!/usr/bin/env python

import requests
import sys
import os
import datetime
import shutil

hours = ('09', '10', '11', '12', '13', '14', '15', '16', '17', '18')
days = ('6', '7')
now = datetime.datetime.now()
hour = now.strftime('%H')
weekday = str(now.isoweekday())
date = now.strftime('%d-%m-%Y')
dir = '/home/user/dir'


def sensor():
    fl = open('sensor_status')
    motion = fl.read()
    if '1' in motion:
        return True


def moveFiles(extention):
    files = os.listdir(dir)
    to_move = filter(lambda x: x.endswith('.{ext}'.format(ext = ext)), files)
    path = r'{dir}{date}'.format(dir = dir, date = date)

    if not os.path.exists(path):
        os.makedirs(path)

    for obj in to_move:
        shutil.move('{dir}{files}'.format(files = obj, dir = dir),
                    '{dir}{date}'.format(dir = dir, date = date))


def sendImage(path):
    url = "https://api.telegram.org/bot_token/sendPhoto";
    files = {'photo': open(path, 'rb')}
    data = {'chat_id' : 'your_telegram_id'}
    r = requests.post(url, files=files, data=data)


if (hour not in hours or weekday in days) and sensor():
    sendImage(sys.argv[1])


moveFiles('avi')
moveFiles('jpg')
