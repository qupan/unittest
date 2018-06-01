#coding=utf-8
import xlrd

def read(x,y):
	a=xlrd.open_workbook('%s/%s.xlsx'%(x,y))
	b=a.sheets()[0]
	c=b.nrows
	d=[]
	for i in range(0,c):
		d.append(b.row_values(i))
	return d
if __name__ == '__main__':
	y=read('c:/robot/data','user')
	for i in y:
		for j in i:
			print (j)
		print ('\n')
