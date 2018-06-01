import xlrd

def read():
    a="c:\\test\\date\\login.xlsx"
    x=xlrd.open_workbook(a)
    y=x.sheets()[0]
    nrows=y.nrows
    z=[]
    for i in range(1,nrows):
        z.append(y.row_values(i))
    return z


"""
read()
"""
