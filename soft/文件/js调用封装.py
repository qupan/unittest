#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


'''
正常定位：
x=driver.find_element(By.ID,'kw').click()
driver.execute_script(x)

定位方式如下：
By.ID='id'
By.NAME='name'
By.CLASSNAME='class name'   中间有空格
By.XPATH='xpath'
By.CSSSELECTOR='css selector'   中间有空格
By.LINKTEXT='link text'    中间有空格
By.TAGNAME='tag name'       中间有空格
使用定位，用等号后面的字符即可
'''
def find(x,y,z):
	a=x.find_element(y,z).click()
	x.execute_script(a)
#x是driver，y是定位方式，z是元素的属性
#执行调用函数,传入三个参数，x，y，z分别对应（浏览器；定位方式；元素属性）
find(driver,'id','kw')