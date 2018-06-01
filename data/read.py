#coding=utf-8
import xlrd

def read(x):
	a=xlrd.open_workbook('c:\\test\\data\\%s.xlsx'%x)
	b=a.sheets()[0]
	c=b.nrows
	d=[]
	for i in range(1,c):
		d.append(b.row_values(i))
	return d
if __name__ == '__main__':
	y=read('login')
	for i in y:
		for j in i:
			print (j)
		print ('\n')