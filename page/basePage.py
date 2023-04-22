#coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
from selenium import webdriver
# 从seleniumwire中引入webdriver，使用driver.requests获取页面的请求头数据
# from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pathlib2 import Path
import os,logging,time,datetime,re,unittest,time
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
        # x=os.getcwd()
        # if 'case' in x:
        #     x1=os.path.join(x.split('case')[0],'log')
        #     if os.path.exists(x1)==False:
        #         os.mkdir(x1)
        # else:
        #     x1=os.path.join(x,'log')
        #     if os.path.exists(x1)==False:
        #         os.mkdir(x1)
        # log_name=os.path.join(x1,log_file)

        # 创建一个handler，用于输出到指定文件,并设置其日志等级
        # fi = logging.FileHandler(log_name,encoding='utf-8')
        # fi.setLevel(logging.INFO)
        # 创建一个handler,用于输出到控制台，并设置其日志等级
        st = logging.StreamHandler()
        st.setLevel(logging .INFO)
        
        #定义handler的输出格式
        formatter = logging.Formatter(u'%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # fi.setFormatter(formatter)
        st.setFormatter(formatter)


        #给日志添加handler
        # self.logger.addHandler(fi)
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
        # os.system('taskkill /f /im IEDriverServer.exe')
        # os.system('taskkill /f /im chromedriver.exe')
        # os.system('taskkill /f /im geckodriver.exe')
        # self.log.info('close driver success!')

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

    def __init__(self, browser="gc"):
        Logger.__init__(self,'Project')
        self.log = self.getlog()
        if browser=="ie":
            driver=webdriver.Ie()
        elif browser=="gc":
            driver=webdriver.Chrome()
        elif browser=="gc_headless":
            options=self.gc_headless()
            driver=webdriver.Chrome(options=options)
        elif browser=="ff":
            driver=webdriver.Firefox()
        elif browser=="ff_headless":
            options=self.ff_headless()
            driver=webdriver.Firefox(options=options)
        self.driver = driver
        self.refresh()

    def gc_headless(self):
        # 谷歌浏览器使用无头模式，linux、window、Mac均可使用
        chrome_options=webdriver.ChromeOptions()
        #解决DevToolsActivePort文件不存在的报错
        chrome_options.add_argument('--no-sandbox')
        #浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
        chrome_options.add_argument('--headless')
        #谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('--disable-gpu')
        #指定浏览器分辨率
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument("--start-maximized")
        #不加载图片, 提升速度
        #chrome_options.add_argument('blink-settings=imagesEnabled=false')
        #隐藏滚动条, 应对一些特殊页面
        chrome_options.add_argument('--hide-scrollbars')
        #手动指定使用的浏览器位置
        #chrome_options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" 
        #防止有的元素在无头模式下无法操作，加入谷歌浏览器的user-agent信息,版本信息不能超过驱动的版本，否则无头模式会报错
        chrome_options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36")
        chrome_options.add_argument('--disable-dev-shm-usage')

        return  chrome_options

    def ff_headless(self):
        # 火狐浏览器使用无头模式，linux、window、Mac均可使用
        firefox_options=webdriver.FirefoxOptions()
        #解决DevToolsActivePort文件不存在的报错
        firefox_options.add_argument('--no-sandbox')
        #浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
        firefox_options.add_argument('--headless')
        #谷歌文档提到需要加上这个属性来规避bug
        firefox_options.add_argument('--disable-gpu')
        #指定浏览器分辨率
        firefox_options.add_argument('--window-size=1920,1080')
        #不加载图片, 提升速度
        #firefox_options.add_argument('blink-settings=imagesEnabled=false')
        #隐藏滚动条, 应对一些特殊页面
        firefox_options.add_argument('--hide-scrollbars')
        #手动指定使用的浏览器位置
        #firefox_options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" 
        #防止有的元素在无头模式下无法操作，加入火狐浏览器的user-agent信息
        firefox_options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0")
        
        return  firefox_options

    def get_element(self, by, value, timeout=30):

        '''
        等待元素显示，显示等待元素，消耗时间最短
        by为定位方法:id,name,class,link_text,xpath,css
        value为定位的值: #id
        '''

        if by == "id":
            locator = (By.ID, value)
        elif by == "name":
            locator = (By.NAME, value)
        elif by == "class":
            by = (By.CLASS_NAME, value)
        elif by == "link_text":
            locator = (By.LINK_TEXT, value)
        elif by == "xpath":
            locator = (By.XPATH, value)
        elif by == "css":
            locator = (By.CSS_SELECTOR, value)
        
        try:
            #等待页面包含元素
            element = WebDriverWait(
                self.driver, timeout, 1
                ).until(EC.presence_of_element_located(locator),'Page not contains element.')
            #等待页面显示元素
            element = WebDriverWait(
                self.driver, timeout, 1
                ).until(EC.visibility_of_element_located(locator),'element not visible .')
            
            self.log.info("find by '%s', element  '%s' find success" % locator)
        except TimeoutException:
            print("查找元素超时请检查元素")
        
        return element


    def get_elements(self,  by, value, index, timeout=30):
        '''
        定位一组元素
        等待元素显示，显示等待元素，消耗时间最短
        by为定位方法:id,name,class,link_text,xpath,css
        value为定位的值: #id
        '''

        if by == "id":
            locator = (By.ID, value)
        elif by == "name":
            locator = (By.NAME, value)
        elif by == "class":
            by = (By.CLASS_NAME, value)
        elif by == "link_text":
            locator = (By.LINK_TEXT, value)
        elif by == "xpath":
            locator = (By.XPATH, value)
        elif by == "css":
            locator = (By.CSS_SELECTOR, value)
        
        try:
            #等待页面包含元素
            elements = WebDriverWait(
                self.driver, timeout, 1
                ).until(EC.presence_of_all_elements_located(locator),'Page not contains element.')
            #等待页面显示元素
            elements = WebDriverWait(
                self.driver, timeout, 1
                ).until(EC.visibility_of_all_elements_located(locator),'element not visible .')
            
            self.log.info("find by '%s', element  '%s' find success" % locator)
        except TimeoutException:
            print("查找元素超时请检查元素")
        

        self.log.info("find by '%s', elements is '%s'." % locator)
        return elements


    def send_keys(self, by, value, text):
        '''
        输入文本:
        text为要输入的文本
        使用方式：bs.send_keys('css','#id','1111')
        '''
        el = self.get_element(by, value)
        el.clear()
        el.send_keys(text)
        self.log.info("Send '%s' to input box success." % text)

    def click(self, by, value):
        '''
        点击操作：
        使用方式：bs.click('css','#id')
        '''
        el = self.get_element(by, value)
        el.click()
        self.log.info("click element '%s' success" % value)

    def double_click(self, by, value):
        '''
        鼠标双击操作
        使用方式：bs.double_click('css','#id')
        '''
        el = self.get_element(by, value)
        ActionChains(self.driver).double_click(el).perform()
        self.log.info("double click element '%s' success" % value)

    def select(self, by, value, number):
        '''
        标准下拉框选择
        locator：为定位
        number：为option选项的索引
        index：为元素索引
        '''
        el = self.get_element(by, value)
        Select(el).select_by_index(number)
        self.log.info("select element '%s', success" % by)

    def move_to_element(self, by, value):
        '''
        鼠标悬停操作
        '''
        el = self.get_element(by, value)
        ActionChains(self.driver).move_to_element(el).perform()
        self.log.info('ActionChins move to element %s success' % by)

    def move_handle(self, by, value):
        '''
        使用鼠标移动滑块
        '''
        el = self.get_element(by, value)
        action=ActionChains(self.driver)
        #action.click_and_hold(element).perform()  #鼠标左键按下不放
        for i in range(200):
            try:
                #action.move_by_offset(2, 0).perform() #平行移动鼠标一次移动2个像素
                action.drag_and_drop_by_offset(el, 500, 0).perform()
            except Exception:
                break
            action.reset_actions()
            sleep(0.001)
        try:
            success_text = self.driver.switch_to.alert.text#得到警告框提示
        except Exception:
            success_text = 'not get alert message'

        self.log.info('ActionChins move handle %s success' % by)
        return success_text

    def context_click(self, by, value):
        '''
        鼠标右击操作
        el=driver.get_element(by, value)
        ActionChains(driver).context_click(el).perform()
        '''
        el = self.get_element(by, value)
        ActionChains(self.driver).context_click(el).perform()

        self.log.info('ActionChins context_click %s success' % by)

    def drag_and_drop(self, by, value):
        '''
        鼠标拖动操作
        element = self.get_element(by, value)
        target = self.get_element(by, value)
        ActionChains(driver).drag_and_drop(element,target).perform()
        '''

        # 待完善

        
        self.log.info('ActionChins drag_and_drop %s success' % by)

    def switch_frame(self, by, value):
        '''
        切到frame中(switch_to.frame())
        el=driver.get_element(by, value)
        driver.switch_to.frame(el)
        '''
        el = self.get_element(by, value)
        self.driver.switch_to.frame(el)

        self.log.info("switch to frame success")

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

    def switch_window(self,locator):
        '''
        切换窗口locator可以使用网页标题，或者网址
        例如： "title" 或者  "https://www.baidu.com/"
        '''
        msg = []
        handles = self.driver.window_handles
        for k in range(50):
            for i in handles:
                self.driver.switch_to.window(i)
                title = self.get_title()
                url = self.get_url()
                msg.append([i,title,url])
            for i in msg:
                for j in i:
                    if locator == j:
                        self.driver.switch_to.window(i[0])
                        result = 'success'
                        break
            if result == 'success':
                break
        self.log.info("switch window success")


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
        self.log.info('close Browser success!')
        self.kill_driver()

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

    def get_size(self, by, value):
        '''
        获取当元素大小
        '''
        element = self.get_element(by, value)
        self.log.info("get size success,by element '%s'." % by)
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

    def get_text(self, by, value):
        '''
        获取文本
        '''
        element = self.get_element(by, value)
        self.log.info("get text success,by element '%s'." % by)
        return element.text

    def get_attribute(self, by, value, name):
        '''
        获取属性
        '''
        element = self.get_element(by, value)
        self.log.info("get attribute success,by element '%s'." % by)
        return element.get_attribute(name)

    def get_html(self):
        '''
        获取当前网页HTML代码
        '''
        html = self.page_source
        self.log.info("get source html success")
        return html



    # 使用js进行元素操作

    def js_execute(self, js):
        '''
        执行js
        '''
        self.driver.execute_script(js)
        self.log.info('Execute js by %s success' % js)

    def js_get_html(self):
        '''
        使用js获取整个页面的html
        '''
        js = ("return document.documentElement.outerHTML")
        html = self.js_execute(js)
        self.log.info('use js get html success')

        return html

    def js_click(self,css, index=0):
        '''
        使用js执行点击,只能使用css定位
        js = "document.querySelectorAll('#id')[0].click()"
        driver.execute_script(js)
        '''
        self.get_element('css',css)
        js = "document.querySelectorAll(\'{}\')[{}].click()".format(css,index)
        self.js_execute(js)
        self.log.info('js_click success , by %s'%css)

    def js_input(self,css,text,index=0):
        '''
        使用js输入文本
        js = "document.querySelectorAll('#id')[0].value='text'"
        driver.execute_script(js)
        '''
        self.get_element('css',css)
        js = "document.querySelectorAll(\'{}\')[{}].value=\'{}\'".format(css,index,text)
        self.js_execute(js)
        self.log.info('js input text: %s success , by %s'%(text,css))

    def js_click_text(self, label, text, index=0):
        '''
        根据标签之间的文本使用JavaScript进行点击，
        label：是标签名称
        text：是标签之间的文本
        index：是元素索引
        '''
        el = self.get_element('xpath', '//{}[contains(string(),\"{}\")]'.format(label,text),index)
        js = "arguments[0].click()"
        self.driver.execute_script(js,el[index])
        self.log.info("click label '%s', success" % label)

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
        element = self.get_element('css','%s'%css)
        js = ("document.querySelector(\'%s\').scrollTop=\'%s\'"%(css,str(number)))
        self.js_execute(js)
        self.log.info('Roll div top to the %d!'%number)

    def js_div_scrollLeft(self,css,number):
        '''
        执行js操作内嵌式div滚动条，左右移动
        number为左右的位置输入数字
        '''
        element = self.get_element('css','%s'%css)
        js = ("document.querySelector(\'%s\').scrollLeft=\'%s\'"%(css,str(number)))
        self.js_execute(js)
        self.log.info('Roll div left to the %d!'%number)
