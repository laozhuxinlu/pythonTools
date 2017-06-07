#!/usr/bin/python
# -*- coding:utf-8 -*-



import urllib
import urllib2
import cookielib

import re

import time

import sys
from multiprocessing  import Process
try:
  import gmail
except ImportError:
  sys.exit(("Install gmail from https://pypi.python.org/pypi/gmail"
            "\n or run pip install gmail"))

def send_email(msg_to_send, emailaddr):
  msg_subject = msg_to_send
  msg_body = 'link: http://www.wolai66.com/commodity?code=17206586167'
  gworker = gmail.GMailWorker("[gmail]", '[password]')
  msg = gmail.Message(subject=msg_subject, to=emailaddr, text=msg_body)
  gworker.send(msg)
  gworker.close()
  print "send email end"

def getHtml(html):
  posturl = html
  request = urllib2.Request(posturl)

  try:
    response = urllib2.urlopen(request)
    return response.read()
  except urllib2.URLError, e:
    return 0
    print e.reason

def main():
  data = getHtml('https://site.douban.com/263021')
  zhengze1 = re.compile('豆瓣售价.*元')
  ifHaveData = re.findall(zhengze1, data)
  for i in ifHaveData:
    # print i
    # zhengze2 = re.compile('\d*/.*\d')
    price = i.replace("豆瓣售价","")
    price = price.replace("元","")
    print price
    if(float(price) <= 20):
      print "Clay:: " + price
  else:
    print 'no'

if __name__=='__main__':
  while True:
    main()
    time.sleep(40)
