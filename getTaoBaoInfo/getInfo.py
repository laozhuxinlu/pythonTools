#!/usr/bin/python
# -*- coding:utf-8 -*-
import urllib
import urllib2
import cookielib
import datetime
import os
import re
import time

import sys
from multiprocessing  import Process

def getHtml(html):
  posturl = html
  request = urllib2.Request(posturl)

  try:
    response = urllib2.urlopen(request)
    return response.read()
  except urllib2.URLError, e:
    return 0
    print e.reason

def saveData(fileName, data):
  with open(fileName,'a') as f:
    f.write(data)
    f.close()

def main(key):
  saveData = ""
  # baseNum = 26500
  baseNum = 28500
  # baseNum = 26895
  theNum = baseNum + key
  base_url = "https://open.taobao.com/docs/api.htm?spm=a219a.7386797.0.0.eBRvlx&source=search&apiId="
  url = base_url + str(theNum)
  data = getHtml(url)
  # print data
  zhengze1 = re.compile('apiName=.*&scopeId')
  zhengze2 = re.compile('class="mtl-desc">[\S\s]*</p>\r\n\r\n</div>')
  zhengze3 = re.compile('class="mtl-main"[\S\s]*</span></h2>')
  if data:
    ifHaveData1 = re.findall(zhengze1, data)
    ifHaveData2 = re.findall(zhengze2, data)
    ifHaveData3 = re.findall(zhengze3, data)
  else:
    return saveData
  # print ifHaveData1
  # print "%s"%ifHaveData2
  # print "%s" % ifHaveData3
  if ifHaveData1:
    aa = ifHaveData1[0].replace("apiName=","")
    bb = aa.replace("&scopeId","")
    saveData = str(theNum) + "                                                                                                                                                                                                                                                                                                              ," + bb
    if ifHaveData3:
      zhengzeQ = re.compile('\(.*\)')
      ifHaveDataQ = re.findall(zhengzeQ, ifHaveData3[0])
      mm = ifHaveDataQ[0].replace("(","")
      nn = mm.replace(")","")
      saveData = saveData + "," + nn
      # saveData = saveData + "," + ifHaveDataQ[0]
    if ifHaveData2:
      cc = ifHaveData2[0].replace("class=\"mtl-desc\">","")
      dd = cc.replace("</p>\r\n\r\n</div>","")
      saveData = saveData + "," + dd
  return saveData

if __name__=='__main__':
  # main(0)
  print "Clay: Please Waitting..."
  theTime = datetime.datetime.now().strftime("%Y%m%d%H%M")
  fileName = "result_26000+500_" + str(theTime) + ".csv"
  theData = ""
  key = 0
  while True:
    if key < 1500:
      print "Clay::Key--> " + str(key)
      abc = main(key)
      if abc == "":
        pass
      else:
        print "Save"
        data = str(abc) + "\n"
        saveData(fileName, data)
      key += 1
      time.sleep(0.5)
    else:
      print "Clay: Finished..."
      break

