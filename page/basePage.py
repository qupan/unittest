#coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
from selenium import webdriver
from time import sleep
import os,logging,time,datetime,re
import os.path
import pytest


class Logger(object):
    '''
    日志信息类创建后class logger（object），在初始化方法中完成保存日志的路径，日志的级别，调用的文件
    将日志储存到指定文件中等工作内容
    :param obj:
    :return:
    '''

    def __init__(self, obj):
        self.logger = logging.getLogger(obj)  # 使用logging.getLogger传入其他类名称来创建一个logger
        self.logger.setLevel(logging.DEBUG)  # 通过setLeverl方法来设置日志的等级

        '''
        创建好logger后编辑log的储存路径，文件名以时间的形式避免重复
        '''
        log_file = time.strftime('%Y%m%d.%H.%M.%S') + '.log'
        #log_name = os.path.abspath('..') + '\logs\\' + log_file
        x=os.getcwd()
        if 'case' in x:
            x1=os.path.join(x.split('case')[0],'log')
            if os.path.exists(x1)==False:
                os.mkdir(x1)
        else:
            x1=os.path.join(x,'log')
            if os.path.exists(x1)==False:
                os.mkdir(x1)
        log_name=os.path.join(x1,log_file)

        # 创建一个handler，用于输出到指定文件,并设置其日志等级
        fi = logging.FileHandler(log_name,encoding='utf-8')
        fi.setLevel(logging.INFO)
        # 创建一个handler,用于输出到控制台，并设置其日志等级
        st = logging.StreamHandler()
        st.setLevel(logging .INFO)
        #定义handler的输出格式
        formatter = logging.Formatter(u'%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fi.setFormatter(formatter)
        st.setFormatter(formatter)
        #给日志添加handler
        self.logger.addHandler(fi)
        self.logger.addHandler(st)

    def getlog(self):
        '''
        :return: logger
        '''
        return self.logger

class Kill(Logger):

    def __init__(self):
        Logger.__init__(self,'OA')
        self.log = self.getlog()

    def kill_driver(self):
        '''
        关闭IE和谷歌浏览器的驱动
        '''
        os.system('taskkill /f /im IEDriverServer.exe')
        self.log.info("kill IEDriverServer success")
        os.system('taskkill /f /im chromedriver.exe')
        self.log.info("kill chromedriver success")

    def kill_browser(self):
        '''
        关闭、IE、谷歌、火狐浏览器
        '''
        os.system('taskkill /f /im firefox.exe')
        os.system('taskkill /f /im chrome.exe')
        os.system('taskkill /f /im iexplore.exe')

class Page(Kill):
    '''
    在每个页面类常用的一些方法
    '''

    def __init__(self, browser, url):
        Logger.__init__(self,'Project')
        self.log = self.getlog()
        if browser=="ie":
            driver=webdriver.Ie()
        elif browser=="gc":
            driver=webdriver.Chrome()
        elif browser=="ff":
            driver=webdriver.Firefox()
        self.driver = driver
        self.driver.get(url)
        self.log.info("Open url:'%s' success" % url)
        self.driver.maximize_window()
        self.log.info('maximize_window')

    def start(self):
        self.log.info('beginning of the test case')

    def end(self):
        self.log.info('end of the test case')

    def error(self,text):
        self.log.info(u'出现的错误是：%s' % text)

    def get(self,url):
        '''
        打开网址
        driver.get(url)
        '''
        self.driver.get(url)
        self.log.info("Open url:'%s' success" % url)

    def max(self):
        '''
        最大化浏览器
        driver.maximize_window()
        '''
        self.driver.maximize_window()
        self.log.info('maximize_window')

    def size(self,x,y):
        '''
        设置浏览器的宽和高
        driver.set_window_size(480,900)
        '''
        self.driver.set_window_size(x,y)
        self.log.info('set window size')

    def refresh(self):
        '''
        刷新页面
        driver.refresh()
        '''
        self.driver.refresh()
        self.log.info('refresh url')

    def back(self):
        '''
        浏览器的后退
        driver.back()
        '''
        self.driver.back()
        self.log.info('back driver!')

    def forward(self):
        '''
        浏览器的前进
        driver.forward()
        '''
        self.driver.forward()
        self.log.info('forward driver!')

    def close(self):
        '''
        关闭当前页面
        driver.close()
        '''
        self.driver.close()
        self.log.info('close window!')

    def quit(self):
        '''
        关闭浏览器
        driver.quit()
        '''
        self.driver.quit()
        self.log.info('close driver!')
        self.kill_driver()

    def find_element(self, locator, timeout=10):
        '''
        定位元素，参数locator为元祖类型
        locator = ('id','xxx')
        driver.find_element(locator)
        '''
        try:
            element = WebDriverWait(
                self.driver, timeout, 1
            ).until(EC.presence_of_element_located(locator),message='element not find')
            element = WebDriverWait(
                self.driver, timeout, 1
            ).until(EC.visibility_of_element_located(locator),message='element not visible')
        except Exception as e:
            element = WebDriverWait(
                self.driver, timeout, 1
            ).until(EC.presence_of_element_located(locator),message='element not find')
            element = WebDriverWait(
                self.driver, timeout, 1
            ).until(EC.visibility_of_element_located(locator),message='element not visible')
            
        self.log.info("find by '%s', element is '%s'." % locator)
        return element

    def find_elements(self, locator, timeout=10):
        '''
        定位一组元素,参数locator为元祖类型
        locator = ('id','xxx')
        driver.find_elements(locator)
        '''
        try:
            elements = WebDriverWait(
                self.driver, timeout, 1
            ).until(EC.presence_of_all_elements_located(locator))
            elements = WebDriverWait(
                self.driver, timeout, 1
            ).until(EC.visibility_of_all_elements_located(locator))
        except Exception as e:
            elements = WebDriverWait(
                self.driver, timeout, 1
            ).until(EC.presence_of_all_elements_located(locator))
            elements = WebDriverWait(
                self.driver, timeout, 1
            ).until(EC.visibility_of_all_elements_located(locator))
        self.log.info("find by '%s', element is '%s'." % locator)
        return elements


    def second_find(self, locator, x, y, timeout=10):
        '''
        二次定位元素，参数locator为元祖类型,
        第一个参数为locator = ('id','xxx')，
        第二个参数x为定位方式，css
        第三个参数y：为定位方式的写法“#id"，不用带括号
        x=driver.find_element(locator)
        x.find_element(locator).click()
        '''
        element = self.find_element(locator)
        element.find_element(x,y).click()
        self.log.info("second find click element '%s', success" % locator[1])

    def seconds_find(self, locator, x, y, number, timeout=10):
        '''
        二次定位元素，参数locator为元祖类型,
        第一个参数为locator = ('id','xxx')，
        第二个参数x为定位方式，css
        第三个参数y：为定位方式的写法“#id"，不用带括号
        number为第一个定位的索引
        x=driver.find_element(locator)
        x.find_element(locator).click()
        '''
        element = self.find_elements(locator)
        element[number].find_element(x,y).click()
        self.log.info("seconds find click element '%s', success" % locator[1])

    def click(self, locator):
        '''
        点击操作，传入元素的定位器，调用findelement方法接收返回值后执行click操作
        driver.find_element(locator).click()
        '''
        element = self.find_element(locator)
        element.click()
        self.log.info("click element '%s', success" % locator[1])

    def click_list(self, locator,number):
        '''
        点击操作，传入元素的定位器，调用findelements方法接收返回值后得到一个列表
        输入number索引值，执行click操作
        driver.find_element(locator).click()
        '''
        element = self.find_elements(locator)
        element[number].click()
        self.log.info("click element '%s', success" % locator[1])

    def select_by_index(self, locator, index=0):
        '''
        下拉框，通过索引index是索引的第几个，默认从0开始
        '''
        element = self.find_element(locator)
        Select(element).select_by_index(index)
        self.log.info("select element '%s', success" % locator[1])

    def select_by_value(self, locator, value):
        '''
        下拉框，通过value属性查找元素
        '''
        element = self.find_element(locator)
        Select(element).select_by_value(value)
        self.log.info("select element '%s', success" % locator[1])

    def select_by_text(self, locator, text):
        '''
        下拉框，通过text属性查找元素
        '''
        element = self.find_element(locator)
        Select(element).select_by_visible_text(text)
        self.log.info("select element '%s', success" % locator[1])

    def choose_file(self, locator, file_path):
        """
        上传文件，输入定位和文件地址
        """
        if not os.path.isfile(file_path):
            raise ValueError("File '%s' does not exist on the local file "
                             "system." % file_path)
        element = self.find_element(locator)
        self.log.info("find element '%s', success" % locator[1])
        element.send_keys(file_path)
        self.log.info("upload file '%s', success" % file_path)

    def double_click(self, locator):
        '''
        鼠标双击操作
        '''
        element = self.find_element(locator)
        ActionChains(self.driver).double_click(element).perform()
        self.log.info('ActionChins double click %s success' % locator[1])

    def move_to_element(self, locator):
        '''
        鼠标悬停操作
        '''
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()
        self.log.info('ActionChins move to element %s success' % locator[1])

    def move_to_elements(self, locator, number):
        '''
        鼠标悬停操作
        '''
        element = self.find_elements(locator)
        ActionChains(self.driver).move_to_element(element[number]).perform()
        self.log.info('ActionChins move to element %s success' % locator[1])


    def context_click(self, locator):
        '''
        鼠标右击操作
        '''
        element = self.find_element(locator)
        ActionChains(self.driver).context_click(element).perform()
        self.log.info('ActionChins context_click %s success' % locator[1])

    def drag_and_drop(self, locator, x,y):
        '''
        鼠标拖动,locator为源文件位置
        第一个参数为locator = ('id','xxx')，
        x,y我要移动的位置，不用带括号
        第二个参数x为定位方式，css
        第三个参数y：为定位方式的写法“#id"
        '''
        element = self.find_element(locator)
        target = self.find_element(x,y)
        ActionChains(self.driver).drag_and_drop(element,target).perform()
        self.log.info('ActionChins drag_and_drop %s success' % locator[1])

    def send_keys(self, locator, text):
        '''
        发送文本，清空后输入
        locator = ('id','xxx')
        element.send_keys(locator,text)
        '''
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        self.log.info("Send '%s' to input box success." % text)

    def back_space(self, locator):
        '''
        键盘后退键
        '''
        element = self.find_element(locator)
        element.send_keys(Keys.BACK_SPACE)
        self.log.info("Send BACK_SPACE success.")

    def space(self, locator):
        '''
        输入空格
        '''
        element = self.find_element(locator)
        element.send_keys(Keys.SPACE)
        self.log.info("Send SPACE to input box success.")

    def ctrl_a(self, locator):
        '''
        执行组合键：ctrl+a 全选输入框内容
        '''
        element = self.find_element(locator)
        element.send_keys(Keys.CONTROL,'a')
        self.log.info("Send ctrl+a success。")

    def ctrl_c(self, locator):
        '''
        执行组合键：复制（Ctrl+C）
        '''
        element = self.find_element(locator)
        element.send_keys(Keys.CONTROL,'c')
        self.log.info("Send ctrl+x success.")

    def ctrl_x(self, locator):
        '''
        执行组合键：ctrl+x 剪切输入框内容
        '''
        element = self.find_element(locator)
        element.send_keys(Keys.CONTROL,'x')
        self.log.info("Send ctrl+x success.")

    def ctrl_v(self, locator):
        '''
        执行组合键：ctrl+v 粘贴内容到输入框
        '''
        element = self.find_element(locator)
        element.send_keys(Keys.CONTROL,'x')
        self.log.info("Send ctrl+v success.")

    def enter(self, locator):
        '''
        执行键：通过回车键盘来代替点击操作
        '''
        element = self.find_element(locator)
        element.send_keys(Keys.ENTER)
        self.log.info("Send ENTER success.")

    def tab(self, locator):
        '''
        执行键：制表键(Tab)
        '''
        element = self.find_element(locator)
        element.send_keys(Keys.TAB)
        self.log.info("Send TAB success.")

    def esc(self, locator):
        '''
        执行键：回退键（Esc）
        '''
        element = self.find_element(locator)
        element.send_keys(Keys.ESCAPE)
        self.log.info("Send Keys.ESCAPE success.")

    def switch_frame(self,locator):
        '''
        切到frame中(switch_to.frame())
        '''
        element = self.find_element(locator)
        self.driver.switch_to.frame(element)
        self.log.info("switch to frame success,by element ")

    def default_content(self):
        '''
        从frame中切回主文档(switch_to.default_content())
        '''
        self.driver.switch_to.default_content()
        self.log.info("switch to default_content success,by element .")

    def parent_frame(self):
        '''
        嵌套frame的操作(switch_to.parent_frame()),返回上一层frame
        '''
        self.driver.switch_to.parent_frame()
        self.log.info("switch to parent_frame success,by element ")

    def current_window(self):
        '''
        获得当前所有打开的窗口的句柄：
        driver.window_handles
        '''
        element = self.driver.current_window_handle
        self.log.info("get current_window success")
        return element

    def window_handles(self):
        '''
        获得当前所有打开的窗口的句柄：
        driver.window_handles
        '''
        element = self.driver.window_handles
        self.log.info("get window_handles success")
        return element

    def switch_window(self,x,y):
        '''
        切到frame中(switch_to.frame())
        传入两个句柄的列表，切换到第一个窗口时，
        传入第一个窗口句柄的列表和一个空列表[]
        '''
        z=[list(set(x)-set(y))[0] if len(x) > len(y) else list(set(y)-set(x))[0]]
        self.switch_to_window(z[0])
        self.log.info("switch window success")

    def alert_text(self):
        '''
        返回 alert/confirm/prompt 中的文字信息
        driver.switch_to_alert().text()
        '''
        text=self.driver.switch_to_alert().text()
        self.log.info("get alert text success")
        return text

    def alert_accept(self):
        '''
        点击确认按钮
        driver.switch_to_alert().text()
        '''
        self.driver.switch_to_alert().accept()
        self.log.info("click alert accept success")

    def alert_dismiss(self):
        '''
        点击取消按钮
        driver.switch_to_alert().text()
        '''
        self.driver.switch_to_alert().dismiss()
        self.log.info("click alert dismiss success")

    def alert_send_keys(self,text):
        '''
        输入值，这个 alert\confirm 没有对话框就不能用了
        driver.switch_to_alert().send_keys()
        '''
        self.driver.switch_to_alert().send_keys(text)
        self.log.info("send text to alert success")

    def get_size(self, locator):
        '''
        获取当元素大小
        '''
        element = self.find_element(locator)
        self.log.info("get size success,by element '%s'." % locator[1])
        return element.size

    def get_window_size(self):
        '''
        获取当前页面大小
        '''
        element = self.driver.get_window_size()
        self.log.info("get size success")
        return element

    def get_title(self):
        '''
        获取title
        '''
        self.log.info('get dirver title.')
        return self.driver.title

    def get_url(self):
        '''
        获取当前页面URL
        '''
        self.log.info('get dirver current_url.')
        return self.driver.current_url

    def get_text(self, locator):
        '''
        获取文本
        '''
        element = self.find_element(locator)
        self.log.info("get text success,by element '%s'." % locator[1])
        return element.text

    def get_attribute(self, locator, name):
        '''
        获取属性
        '''
        element = self.find_element(locator)
        self.log.info("get attribute success,by element '%s'." % locator[1])
        return element.get_attribute(name)

    def get_cookies(self):
        '''
        获得所有 cookie 信息
        driver.get_cookies()
        '''
        self.log.info('get all cookies success')
        return self.driver.get_cookies()

    def get_cookie(self,name):
        '''
        返回有特定 name 值有 cookie 信息
        driver.get_cookie(name)
        '''
        self.log.info('get all cookies success')
        return self.driver.get_cookie(name)

    def add_cookie(self,text):
        '''
        添加 cookie，必须有 name 和 value 值
        driver.add_cookie({'name':'key-aaaaaaa', 'value':'value-bbbbbb'})
        '''
        self.driver.add_cookie(text)
        self.log.info('add cookies success')
        

    def delete_cookie(self,name):
        '''
        删除特定(部分)的 cookie 信息
        driver.delete_cookie(name)
        '''
        self.driver.add_cookie(text)
        self.log.info('add cookies success')
        

    def delete_all_cookies(self):
        '''
        删除所有 cookie 信息
        driver.delete_cookie(name)
        '''
        self.driver.add_cookie(text)
        self.log.info('add cookies success')
        
    def js_execute(self, js):
        '''
        执行js
        '''
        self.log.info('Execute js by %s' % js)
        self.driver.execute_script(js)

    def js_focus_element(self, locator):
        '''
        聚焦元素
        '''
        target = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_click(self,css):
        '''
        使用js执行点击
        js = 'document.querySelector('#id').click()'
        driver.execute_script(js)
        '''
        element = self.find_element(('css','%s'%css))
        js = ("document.querySelector(\'%s\').click()"%css)
        #self.driver.execute_script(js)
        self.js_execute(js)
        self.log.info('js_click success , by %s'%css)

    def jq_click(self,css):
        '''
        使用jquery执行点击
        js = '$('#id').click()'
        driver.execute_script(js)
        '''
        element = self.find_element(('css','%s'%css))
        js = ("$(\'%s\').click()"%css)
        self.js_execute(js)
        self.log.info('jq_click success,by %s'%css)

    def jq_dblclick(self,css):
        '''
        使用jquery执行双击
        js = '$('#id').dblclick()'
        driver.execute_script(js)
        '''
        element = self.find_element(('css','%s'%css))
        js = ("$(\'%s\').dblclick()"%css)
        self.js_execute(js)
        self.log.info('jq_double_click success,by %s'%css)

    def js_input(self,css,text):
        '''
        使用js输入文本
        js = 'document.querySelector('#id').click()'
        driver.execute_script(js)
        '''
        element = self.find_element(('css','%s'%css))
        js = ("document.querySelector(\'%s\').value=\'%s\'"%(css,text))
        self.js_execute(js)
        self.log.info('js_input text: %s success , by %s'%(text,css))

    def jq_input(self,css,text):
        '''
        使用jQuery输入文本
        js = 'document.querySelector('#id').click()'
        driver.execute_script(js)
        '''
        element = self.find_element(('css','%s'%css))
        js = ("$(\'%s\').val(\'%s\')"%(css,text))
        self.js_execute(js)
        self.log.info('jquery_input text: %s success , by %s'%(text,css))

    def js_scroll_Top(self,number):
        '''
        滚动到顶部
        '''
        js = "window.scrollTo(0,%s)"%number
        self.js_execute(js)
        self.log.info('Roll to the top!')

    def js_scroll_End(self):
        '''
        滚动到底部
        '''
        js = "window.scrollTo(0,document.body.scrollHight)"
        self.js_execute(js)
        self.log.info('Roll to the end!')

    def js_div_scrollTop(self,css,number):
        '''
        执行js操作内嵌式div滚动条，上下移动
        number为上下的位置输入数字
        '''
        element = self.find_element(('css','%s'%css))
        js = ("document.querySelector(\'%s\').scrollTop=\'%s\'"%(css,str(number)))
        self.js_execute(js)
        self.log.info('Roll div top to the %d!'%number)

    def jq_div_scrollTop(self,css,number):
        '''
        执行js操作内嵌式div滚动条，上下移动
        number为上下的位置输入数字
        '''
        element = self.find_element(('css','%s'%css))
        js = ("$(\'%s\').scrollTop=\'%s\'"%(css,str(number)))
        self.js_execute(js)
        self.log.info('Roll div top to the %d!'%number)

    def js_div_scrollLeft(self,css,number):
        '''
        执行js操作内嵌式div滚动条，左右移动
        number为左右的位置输入数字
        '''
        element = self.find_element(('css','%s'%css))
        js = ("document.querySelector(\'%s\').scrollLeft=\'%s\'"%(css,str(number)))
        self.js_execute(js)
        self.log.info('Roll div left to the %d!'%number)

    def get_windows_img(self):
        '''
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹里，.\Screenshots下
        '''
        file_name = time.strftime('%Y%m%d.%H.%M.%S')
        file_path = os.path.abspath('..') + '\Screenshots\\' + file_name + '.png'
        try:
            self.driver.get_screenshot_as_file(file_path)
            self.log.info('Had take screenshot and save to folder:/screenshots')
        except NameError as e:
            self.log.info('Failed to take the screenshot!%s' % e)
            self.get_windows_img()

    def is_text_in_element(self, locator, text, timeout=10):
        '''
        判断文本在元素里，没有元素返回false打印日志，定位到返回判断结果的布尔值
        result = driver.text_in_element(locator,text)
        '''
        try:
            result = WebDriverWait(
                self.driver, timeout, 1
            ).until(EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            logger.info('No location to the element.')
            return False
        else:
            return result

    def is_text_in_value(self, locator, value, timeout=10):
        '''
        判断元素的value值，没定位到元素返回false，定位到返回判断结果布尔值
        result = dirver.text_to_be_present_in_element_value(locator,text)
        '''
        try:
            result = WebDriverWait(
                self.driver, timeout, 1
            ).until(EC.text_to_be_present_in_element_value(locator, value))
        except TimeoutException:
            logger.info('No location to the element.')
            return False
        else:
            return result

    def is_title(self, title, timeout=10):
        '''
        判断元素的title是否完全等于
        '''
        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.title_is(title))
        return result

    def is_title_contains(self, title, timeout=10):
        '''
        判断元素的title是否包含
        '''
        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.title_contains(title))
        return result

    def is_selected(self, locator, timeout=10):
        '''
        判断元素是否被选中
        '''
        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.element_located_to_be_selected(locator))
        return result

    def is_selected_be(self, locator, selected=True, timeout=10):
        '''
        判断元素的状态是不是符合期望的状态，selected是期望的状态
        '''
        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.element_located_selection_state_to_be(locator, selected))
        return result

    def is_alert_present(self, timeout=10):
        '''
        判断页面是否有alert,有的话返回alert，没有返回False
        '''
        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.alert_is_present())
        return result

    def is_visibility(self, locator, timeout=10):
        '''
        元素可见，返回本身，不可见返回False
        '''
        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.visibility_of_element_located(locator))
        return result

    def is_invisibility(self, locator, timeout=10):
        '''
        元素可见返回本身，不可见返回Ture,没有找到元素也返回Ture
        '''
        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.invisibility_of_element_located(locator))
        return result

    def is_clickable(self, locator, timeout=10):
        '''
        元素可以点击is_enabled返回本身，不可点击返回False
        '''
        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.element_to_be_clickable(locator))
        return result

    def is_located(self, locator, timeout=10):
        '''
        判断元素有没有被定位到(并不意味着可见),定位到返回element，没有定位到返回False
        '''
        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.presence_of_all_elements_located(locator))
        return result
