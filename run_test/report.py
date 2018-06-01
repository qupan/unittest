import unittest,HTMLTestRunner
import time

def suite():
    x="c:\\test\\case"
    y=unittest.defaultTestLoader.discover(x,
                                          pattern="test_*.py",
                                          top_level_dir=None)
    return y
def report():
    a=suite()
    b=time.strftime("%Y_%m_%d %H-%M-%S",time.localtime(time.time()))
    c="c:\\test\\report\\"+ b +" report.html"
    d=open(c,"wb+")
    e=HTMLTestRunner.HTMLTestRunner(stream=d,
                                    title="test",
                                    description="test")
    #x=unittest.TextTestRunner()
    #y=x.run(a)
    #print (y)
    e.run(a)
    d.close()


if __name__=="__main__":
    report()

