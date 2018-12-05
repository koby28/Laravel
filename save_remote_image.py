#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import requests
import os

def saveRemoteImage():
    imgurl = 'http://www.tantengvip.com/wp-content/uploads/2015/01/cropped-13887362_13887362_1347773771848.jpg'
    filename = imgurl.split('/')[-1]
    path = './static/'+filename
    if not os.path.exists(path):
        r = requests.get(imgurl)
        with open(path, 'wb') as f:
            f.write(r.content)
            print('OK')
    else:
        print('Already exists.')

    """
    下载大文件这样写：
    for chunk in r.iter_content():
        f.write(chunk)
    """

saveRemoteImage()
