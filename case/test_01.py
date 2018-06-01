#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by   import By
from selenium.webdriver.common.action_chains    import ActionChains
import time

b=webdriver.Chrome()
b.implicitly_wait(10)
b.get('https://pan.baidu.com/')
time.sleep(3)
b.find_element('class name','tang-pass-footerBarULogin').click()
x=b.find_element_by_name('userName')
x.clear()
x.send_keys("15202493273")
y=b.find_element_by_name('password')
y.clear()
y.send_keys('qp66666')
b.find_element_by_class_name('pass-button').click()
time.sleep(3)
b.quit()

