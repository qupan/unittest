#coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import *
from selenium import webdriver
from time import sleep
import os,logging,time,datetime,re
import os.path


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
        if os.path.exists('c:\\log')==False:
            os.mkdir('c:\\log')
        log_name = 'c:\\log\\' + log_file

        # 创建一个handler，用于输出到指定文件,并设置其日志等级
        fi = logging.FileHandler(log_name,encoding='utf-8')
        fi.setLevel(logging.INFO)
        # 创建一个handler,用于输出到控制台，并设置其日志等级
        st = logging.StreamHandler()
        st.setLevel(logging .INFO)
        #定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
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
        os.system('taskkill /f /im IEDriverServer.exe')
        self.log.info("kill IEDriverServer success")
        os.system('taskkill /f /im chromedriver.exe')
        self.log.info("kill chromedriver success")

    def kill_browser(self):
        os.system('taskkill /f /im firefox.exe')
        os.system('taskkill /f /im chrome.exe')
        os.system('taskkill /f /im iexplore.exe')

class Page(Logger):
    '''
    在每个页面类常用的一些方法
    '''

    def __init__(self, browser, url):
        Logger.__init__(self,'OA')
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

    def start(self):
        self.log.info('beginning of the test case')

    def end(self):
        self.log.info('end of the test case')

    def error(self,text):
        self.log.info('出现的错误是：%s' % text)

    def find_element(self, locator, timeout=10):
        '''
        定位元素，参数locator为元祖类型
        locator = ('id','xxx')
        driver.find_element(locator)
        '''
        element = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.presence_of_element_located(locator))
        self.log.info("find by '%s', element is '%s'." % locator)
        return element

    def find_elements(self, locator, timeout=10):
        '''
        定位一组元素
        :param locator:
        :param timeout:
        :return:
        '''
        elements = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.presence_of_all_elements_located(locator))
        self.log.info("find by '%s', element is '%s'." % locator)
        return elements

    def click(self, locator):
        '''
        点击操作，传入元素的定位器，调用findelement方法接收返回值后执行click操作
        '''
        element = self.find_element(locator)
        element.click()
        self.log.info("click element '%s', success" % locator[1])

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

    def frame(self,text):
        '''
        跳转到frame框架
        '''
        self.driver.switch_to.frame(text)
        self.log.info("switch to frame success,by element '%s'." % text)

    def back(self):
        self.driver.back()
        self.log.info('back driver!')

    def forward(self):
        self.driver.forward()
        self.log.info('forward driver!')

    def close(self):
        self.driver.close()
        self.log.info('close window!')

    def quit(self):
        self.driver.quit()
        self.log.info('close driver!')

    def get_title(self):
        '''
        获取title
        '''
        self.log.info('git dirver title.')
        return self.driver.title

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

    def move_to_element(self, locator):
        '''
        鼠标悬停操作
        locator=('id','xxx')
        driver.move_to_element(locator)
        '''
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()
        self.log.info('ActionChins move to %s' % locator)

    def js_execute(self, js):
        '''
        执行js
        '''
        self.log.info('Execute js.%s' % js)
        return self.driver.execute_script(js)

    def js_focus_element(self, locator):
        '''
        聚焦元素
        '''
        target = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        '''
        滚动到顶部
        '''
        js = 'window.scrollTo(0,0)'
        self.driver.js_execute(js)
        self.log.info('Roll to the top!')

    def js_scroll_end(self):
        '''
        滚动到底部
        '''
        js = "window.scrollTo(0,document.body.scrollHight)"
        self.js_execute(js)
        self.log.info('Roll to the end!')

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
