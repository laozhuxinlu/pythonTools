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
  gworker = gmail.GMailWorker("[Gmail]", '[password]')
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
  data = getHtml('http://www.wolai66.com/commodity?code=17206586167')
  zhengze = re.compile('class="tb_amount_input".*?id="pro_number_input.*?value="1".*?/>')
  ifHaveData = re.findall(zhengze, data)
  # print ifHaveData
  if(ifHaveData == ['class="tb_amount_input" id="pro_number_input" onblur="cart_number_input(&quot;#pro_number_input&quot;)" value="1" />']):
    print 'yes'
    send_email('We have Jingdong card now, buy it now!!!', '15656008623@163.com')
    time.sleep(5)
    send_email('We have Jingdong card now, buy it now!!!', 'clay.zhu0102@gmail.com')
    time.sleep(5)
    send_email('We have Jingdong card now, buy it now!!!', 'becky1992.li@gmail.com')
    time.sleep(20)
    send_email('We have Jingdong card now, buy it now!!!', '15656008623@163.com')
    time.sleep(5)
    send_email('We have Jingdong card now, buy it now!!!', 'clay.zhu0102@gmail.com')
    time.sleep(5)
    send_email('We have Jingdong card now, buy it now!!!', 'becky1992.li@gmail.com')
    while True:
      pass
  else:
    print 'no'

if __name__=='__main__':
  while True:
    main()
    time.sleep(20)
