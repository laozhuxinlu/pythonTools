#!/usr/bin/python
# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re

global ifHaveCard
ifHaveCard = True

def checkAgain(html):
  zhengze = re.compile('class="tb_attribute_stock f_14.*id="fesco_pro_inventory_quantity">0</div>')
  ifHaveData = re.findall(zhengze, html)
  if(ifHaveData == [u'class="tb_attribute_stock f_14" id="fesco_pro_inventory_quantity">0</div>']):
    global ifHaveCard
    ifHaveCard = True
  else:
    global ifHaveCard
    ifHaveCard = False

def main():
  driver = webdriver.Firefox()
  driver.get("http://wolai66.com/sign_in")

  username = driver.find_element_by_name("user_name")
  username.send_keys("[username]")
  password = driver.find_element_by_name("user_password")
  password.send_keys("[password]")

  password.send_keys(Keys.RETURN)

  time.sleep(20)

  content = driver.find_elements_by_class_name('each_img')

  theCard = content[1]

  theCard.click()

  time.sleep(20)

  html = driver.page_source

  global ifHaveCard
  while ifHaveCard:
    driver.refresh()
    time.sleep(5)
    html = driver.page_source
    checkAgain(html)
    time.sleep(1)

  print driver.page_source
  time.sleep(5)
  print "Clay:: OK..."

  add  = driver.find_element_by_id("tb_btn_pro_buy")
  add.click()
  time.sleep(10)
  jiesuan = driver.find_element_by_class_name('check_btn')
  jiesuan.click()
  print driver.page_source
  time.sleep(5)
  money = driver.find_element_by_id("point_1_0")
  money.send_keys("100")
  confirmBuy = driver.find_element_by_class_name('check_btn')
  confirmBuy.click()
  time.sleep(5)
  print "Clay:: finaly html..."
  print driver.page_source

if __name__=='__main__':
    main()



