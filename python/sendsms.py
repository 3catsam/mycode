#!/usr/bin/env python
# coding=utf8

import httplib
import urllib
import os

httpClient = None
# BASE_DIR = os.path.dirname(os.path.dirname(__file__)) #获取当前文件夹的父目录绝对路径
BASE_DIR = os.path.dirname(__file__)  # 获取当前文件夹的绝对路径
print BASE_DIR
# os.environ["MessagePath"]
file_path = os.path.join(BASE_DIR, 'text', 'readme.txt')
data = open(file_path, 'r')  # r:readonly
sendMessage = ''
for line in data:
    sendMessage += line.replace('\n', '') + ';'
data.close()

if sendMessage == '':
    print 'empty'
    exit(0)

try:
    httpClient = httplib.HTTPConnection(
        'sms.shanghai-electric.com', 9080, timeout=30)
    url = '/ema/http/SendSms?Account=9990009&Password=66af1f48aab165e83f658a61260a908f\
&SubCode=123&Phone=18101852518&Content=' + urllib.quote(sendMessage) + '&SendTime='
    httpClient.request('GET', url)

    # Response is HTTPResponse object
    response = httpClient.getresponse()
    print response.status
    print response.reason
    print response.read()
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()
file = open(file_path, 'w+')  # open file with rw,recover original file
file.truncate()  # truncate file
print sendMessage
