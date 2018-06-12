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
    b=time.strftime("%Y_%m_%d %H-%M-%S")
    c="c:\\test\\report\\"+ b +" report.html"
    with open(c,"wb+") as fb:
        e=HTMLTestRunner.HTMLTestRunner(stream=fb,
                                        title="test",
                                        description="test")
        e.run(a)

if __name__=="__main__":
    report()

