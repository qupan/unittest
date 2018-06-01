import yagmail,os
from bs4 import BeautifulSoup

def read():
    a="c:\\test\\report"
    x=os.listdir(a)
    x.sort(key=lambda fn:os.path.getmtime(a+"\\"+fn))
    y=os.path.join(a,x[-1])
    
    with open(y,"rb") as b:
        c=b.read()
    d=BeautifulSoup(c,"html.parser")
    e=d.find_all(class_="attribute")
    f=e[2].contents[-2]
    if ("Error" in f)or("Failure" in f):
        return y
    else:
        return "Pass"

def mail():
    a=read()
    if a!="Pass":
        m=yagmail.SMTP(user="15202493273@163.com",
                        password="qp1993",
                        host="smtp.163.com")
        m.send("1007172144@qq.com","屈潘","测试失败-附件打开两次看",a)
        print ("测试失败")
    else:
        print ("测试成功")


"""
if __name__=="__main__":
    mail()

"""
