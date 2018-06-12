#coding=utf-8
from basePage import *

d=Page('gc','http://www.baidu.com')
try:
	d.send_keys(('css','#3kw'),'hello')
except Exception as e:
	print('001')
	d.send_keys(('css','#kw'),'hello')
	d.click(('css','#su'))
	x=d.get_window_size()
	y=x['height']/3
	d.js_scroll_top(y)
	try:
		d.send_keys(('css','#isdd'),'hello')
	except Exception as e:
		print('002')
Kill().kill_driver()
Kill().kill_browser()