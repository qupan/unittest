#coding=utf-8
from selenium.webdriver.common.by import By
from basePage import Page

class LoginPage(Page):
    """搜索页面元素类"""
    #x=[用户名，密码，登陆按钮]
    x=[(By.NAME,"username"),(By.NAME,"password"),(By.CSS_SELECTOR,"button[type=submit")]
    #y=[用户名，点击家园,得到所有为a的标签数]
    y=[(By.LINK_TEXT,"qupan"),("link text","家园"),("tag name","a")]
    base_url="http://localhost/upload/forum.php"

    def __init__(self,driver,):
        Page.__init__(self,driver)

    def log_home(self):
        self.home(self.base_url)

    def log_user(self,text):
        self.send_keys(self.x[0],text)

    def log_pass(self,text):
        self.send_keys(self.x[1],text)

    def log_click(self):
        self.click(self.x[2])

    def jy(self):
        self.click(self.y[1])




