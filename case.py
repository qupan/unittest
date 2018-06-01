#coding=utf-8
from basePage import *

d=Page("gc","http://www.baidu.com")
try:
        d.send_keys(("css","kw"),"heolo")
except Exception as e:
        d.send_keys(("css","#kw"),"heolo")
        print(e)
sleep(3)
d.quit()
