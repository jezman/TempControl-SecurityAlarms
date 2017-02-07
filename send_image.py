#!/usr/bin/env python3

import os
import requests
import shutil
from sys import argv
from time import strftime

date = strftime('%d-%m-%Y')
dir = 'path'
works_hours = range(7, 17)
currently_hour = int(strftime('%H'))


def sends(path):
    url = "https://api.telegram.org/bot"BOT_ID"/sendPhoto"
    files = {'photo': open(path, 'rb')}
    data = {'chat_id': "CHAT_ID"}
    r = requests.post(url, files=files, data=data)
    # print(r.status_code, r.reason, r.content)


def sensor():
    fl = open('path_to_rid')
    motion = fl.read()
    if '1' in motion:
        return True


def moveFiles(extention):
    files = os.listdir(dir)
    to_move = filter(lambda x: x.endswith('.{ext}'.format(ext=ext)), files)
    path = r'{dir}{date}'.format(dir=dir, date=date)

    if not os.path.exists(path):
        os.makedirs(path)

    for obj in to_move:
        shutil.move('{dir}{files}'.format(files=obj, dir=dir),
                    '{dir}{date}'.format(dir=dir, date=date))


if (hour not in hours or weekday in days) and sensor():
    sendImage(sys.argv[1])


moveFiles('avi')
moveFiles('jpg')
