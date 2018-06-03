from basePage import Page

class Login(Page):
	def __init__(self,driver,url):
                Page.kill_browser(self)
		Page.__init__(self,driver,url)
	def input(self):
		self.send_keys(("css","#kw"),"hello")

	def click_element(self):
		self.click(("css","#su"))
