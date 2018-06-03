#coding=utf-8
from login import Login
import unittest

class LianXi(unittest.TestCase):
	def setUp(self):
		self.base=Login("gc","http://www.baidu.com")
	@unittest.skip("kiii")
	def test01(self):
		d=self.base
		input(self)
		sleep(3)

	def test02(self):
		d=self.base
		d.input()
		d.click_element()

	def tearDown(self):
		self.base.quit()
		self.base.kill_driver()
		
if __name__=="__main__":
	unittest.main()
