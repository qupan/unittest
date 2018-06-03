#coding=utf-8
import re

fun_dict={"01":"a","02":"b","03":"b"}
data=['c:\\pan\\down','x1','01,02','x2','02']

#点击项目
for i in range(1,len(data),2):
	d.click(("link text",data[i]))
	#点击查询函数，保存csv格式文件
	if type(re.search(',',data[i+1])) == "<class 'NoneType'>":
		if data[i+1]=="02":
			d.click_list(('link text','b'),0)
		elif data[i+1]=="03":
			d.click_list(('link text','b'),1)
		else:
			d.click(('link text',fun_dict[data[i+1]]))
	else:
		x=data[i+1].split(',')
		for i in x:
			if i=="02":
				d.click_list(('link text','b'),0)
			elif i=="03":
				d.click_list(('link text','b'),1)
			else:
				d.click(("link text",fun_dict[i]))
	#点击所有项目，回到主页
	d.clic(("link text","jjj"))
