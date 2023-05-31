# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from toollib import autodriver
# 从seleniumwire中引入webdriver，使用driver.requests获取页面的请求头数据
# from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# from pathlib2 import Path
import os, random, sys, time
import os.path
from retry import retry

from common.log import Logger


class Kill:

    def __init__(self):
        pass

    def kill_driver(self):
        '''
        关闭IE和谷歌浏览器的驱动
        '''
        # os.system('taskkill /f /im IEDriverServer.exe')
        # os.system('taskkill /f /im chromedriver.exe')
        # os.system('taskkill /f /im geckodriver.exe')

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
    USER_AGENTS = [
    # 用户头列表
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    ]


    log = Logger().getlog()
    
    def __init__(self, browser="gc"):

        if browser=="ie":
            driver=webdriver.Ie()
        elif browser=="gc":
            # 配置选项
            options = webdriver.ChromeOptions()
            #谷歌文档提到需要加上这个属性来规避bug
            options.add_argument('--disable-gpu')
            # #指定浏览器分辨率
            # options.add_argument('--window-size=1920,1080')
            # options.add_argument("--start-maximized")
            #不加载图片, 提升速度
            options.add_argument('blink-settings=imagesEnabled=false')
            #隐藏滚动条, 应对一些特殊页面
            options.add_argument('--hide-scrollbars')
            #手动指定使用的浏览器位置
            #options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" 
            # 忽略证书错误
            options.add_argument('--ignore-certificate-errors')
            # 忽略 Bluetooth: bluetooth_adapter_winrt.cc:1075 Getting Default Adapter failed.
            # 去除“Chrome正受到自动测试软件的控制”的显示
            options.add_experimental_option('useAutomationExtension', False)
            options.add_experimental_option('excludeSwitches', ['enable-automation'])
            # 忽略 DevTools listening on ws://127.0.0.1... 提示
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            filepath = os.path.dirname(os.path.realpath(sys.argv[0])) #获取到文件真实地址
            driver_path = autodriver.chromedriver(platform='win64', driver_dir=filepath)  #自动下载驱动（platform默认为win64）
            # print ('driver_path', driver_path)
            driver = webdriver.Chrome(options=options, service=Service(driver_path))

        elif browser=="gc_headless":
            options=self.gc_headless()
            filepath = os.path.dirname(os.path.realpath(sys.argv[0])) #获取到文件真实地址
            driver_path = autodriver.chromedriver(platform='win64', driver_dir=filepath)  #自动下载驱动（platform默认为win64）
            driver = webdriver.Chrome(options=options, service=Service(driver_path))
            # 设置headers
            driver.execute_cdp_cmd("Network.setExtraHTTPHeaders",
                                {"headers":
                                    {"User-Agent": random.choice(self.USER_AGENTS),
                                    }
                                })
            
            # 防止网站检测selenium的webdriver
            driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                    "source": """
                        Object.defineProperty(navigator, 'webdriver', {
                            get: () => False
                        })
                    """})

        
        elif browser=="ff":
            driver=webdriver.Firefox()
        elif browser=="ff_headless":
            options=self.ff_headless()
            driver=webdriver.Firefox(options=options)
        self.driver = driver
        self.refresh()

    def gc_headless(self):
        # 谷歌浏览器使用无头模式，linux、window、Mac均可使用
        options=webdriver.ChromeOptions()
        #解决DevToolsActivePort文件不存在的报错
        options.add_argument('--no-sandbox')
        #浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
        options.add_argument('--headless')
        #谷歌文档提到需要加上这个属性来规避bug
        options.add_argument('--disable-gpu')
        #指定浏览器分辨率
        options.add_argument('--window-size=1920,1080')
        options.add_argument("--start-maximized")
        #不加载图片, 提升速度
        options.add_argument('blink-settings=imagesEnabled=false')
        #隐藏滚动条, 应对一些特殊页面
        options.add_argument('--hide-scrollbars')
        #手动指定使用的浏览器位置
        #options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" 
        #防止有的元素在无头模式下无法操作，加入谷歌浏览器的user-agent信息,版本信息不能超过驱动的版本，否则无头模式会报错
        options.add_argument( "User-Agent={}".format( random.choice(self.USER_AGENTS) ) )
        options.add_argument('--disable-dev-shm-usage') #克服有限的资源问题  【但是用于Linux系统】
        # 配置选项
        # 忽略证书错误
        options.add_argument('--ignore-certificate-errors')
        # 忽略 Bluetooth: bluetooth_adapter_winrt.cc:1075 Getting Default Adapter failed.
        # 去除“Chrome正受到自动测试软件的控制”的显示
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 忽略 DevTools listening on ws://127.0.0.1... 提示
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        return  options

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
        firefox_options.add_argument('blink-settings=imagesEnabled=false')
        #隐藏滚动条, 应对一些特殊页面
        firefox_options.add_argument('--hide-scrollbars')
        #手动指定使用的浏览器位置
        #firefox_options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" 
        #防止有的元素在无头模式下无法操作，加入火狐浏览器的user-agent信息
        firefox_options.add_argument( "User-Agent={}".format( random.choice(self.USER_AGENTS) ) )
        
        return  firefox_options

    @retry(tries=6, delay=1) #错误重试
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
        
        element = None
        try:
            #等待页面包含元素
            element = WebDriverWait(
                self.driver, timeout, 1
                ).until(EC.presence_of_element_located(locator),'Page not contains element.')
            #等待页面显示元素
            element = WebDriverWait(
                self.driver, timeout, 1
                ).until(EC.visibility_of_element_located(locator),'element not visible .')
            
            self.log.debug("find by '%s', element  '%s' find success" % locator)
        except TimeoutException:
            self.log.error("查找元素超时请检查元素: find by '%s', element  '%s' find error" % locator)
            # 时间戳名称，防止覆盖
            name = time.strftime("%H.%M.%S")
            # 异常截图保存在本地
            self.driver.get_screenshot_as_file('%s.png'%name)
            self.js_refresh() #获取元素失败，刷新一下网页重试
            raise
    
        return element

    @retry(tries=6, delay=1) #错误重试
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
        
        elements = None
        try:
            #等待页面包含元素
            elements = WebDriverWait(
                self.driver, timeout, 1
                ).until(EC.presence_of_all_elements_located(locator),'Page not contains element.')
            #等待页面显示元素
            elements = WebDriverWait(
                self.driver, timeout, 1
                ).until(EC.visibility_of_all_elements_located(locator),'element not visible .')
            
            self.log.debug("find by '%s', element  '%s' find success" % locator)
        except TimeoutException:
            self.log.error("查找元素超时请检查元素: find by '%s', element  '%s' find error" % locator)
            # 时间戳名称，防止覆盖
            name = time.strftime("%H.%M.%S")
            # 异常截图保存在本地
            self.driver.get_screenshot_as_file('%s.png'%name)
            self.js_refresh() #获取元素失败，刷新一下网页重试
            raise
        
        self.log.debug("find by '%s', elements is '%s'." % locator)
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
        self.log.debug("Send '%s' to input box success." % text)

    def click(self, by, value):
        '''
        点击操作：
        使用方式：bs.click('css','#id')
        '''
        el = self.get_element(by, value)
        el.click()
        self.log.debug("click element '%s' success" % value)

    def double_click(self, by, value):
        '''
        鼠标双击操作
        使用方式：bs.double_click('css','#id')
        '''
        el = self.get_element(by, value)
        ActionChains(self.driver).double_click(el).perform()
        self.log.debug("double click element '%s' success" % value)

    def select(self, by, value, number):
        '''
        标准下拉框选择
        locator：为定位
        number：为option选项的索引
        index：为元素索引
        '''
        el = self.get_element(by, value)
        Select(el).select_by_index(number)
        self.log.debug("select element '%s', success" % by)

    def move_to_element(self, by, value):
        '''
        鼠标悬停操作
        '''
        el = self.get_element(by, value)
        ActionChains(self.driver).move_to_element(el).perform()
        self.log.debug('ActionChins move to element %s success' % by)

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

        self.log.debug('ActionChins move handle %s success' % by)
        return success_text

    def context_click(self, by, value):
        '''
        鼠标右击操作
        el=driver.get_element(by, value)
        ActionChains(driver).context_click(el).perform()
        '''
        el = self.get_element(by, value)
        ActionChains(self.driver).context_click(el).perform()

        self.log.debug('ActionChins context_click %s success' % by)

    def drag_and_drop(self, by, value):
        '''
        鼠标拖动操作
        element = self.get_element(by, value)
        target = self.get_element(by, value)
        ActionChains(driver).drag_and_drop(element,target).perform()
        '''

        # 待完善

        
        self.log.debug('ActionChins drag_and_drop %s success' % by)

    def switch_frame(self, by, value):
        '''
        切到frame中(switch_to.frame())
        el=driver.get_element(by, value)
        driver.switch_to.frame(el)
        '''
        el = self.get_element(by, value)
        self.driver.switch_to.frame(el)

        self.log.debug("switch to frame success")

    def default_content(self):
        '''
        从frame中切回主文档(switch_to.default_content())
        '''
        self.driver.switch_to.default_content()
        self.log.debug("switch to default_content success,by element .")

    def parent_frame(self):
        '''
        嵌套frame的操作(switch_to.parent_frame()),返回上一层frame
        '''
        self.driver.switch_to.parent_frame()
        self.log.debug("switch to parent_frame success,by element ")

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
        self.log.debug("switch window success")


    def get(self,url):
        '''
        打开网址
        driver.get(url)
        '''
        self.driver.get(url)
        self.log.debug("Open url:'%s' success" % url)

    def max(self):
        '''
        最大化浏览器
        driver.maximize_window()
        '''
        self.driver.maximize_window()
        self.log.debug('maximize_window')

    def size(self,x,y):
        '''
        设置浏览器的宽和高
        driver.set_window_size(480,900)
        '''
        self.driver.set_window_size(x,y)
        self.log.debug('set window size')

    def refresh(self):
        '''
        刷新页面
        driver.refresh()
        '''
        self.driver.refresh()
        self.log.debug('refresh url')

    def back(self):
        '''
        浏览器的后退
        driver.back()
        '''
        self.driver.back()
        self.log.debug('back driver!')

    def forward(self):
        '''
        浏览器的前进
        driver.forward()
        '''
        self.driver.forward()
        self.log.debug('forward driver!')

    def close(self):
        '''
        关闭当前页面
        driver.close()
        '''
        self.driver.close()
        self.log.debug('close window!')

    def quit(self):
        '''
        关闭浏览器
        driver.quit()
        '''
        self.driver.quit()
        self.log.debug('close Browser success!')
        self.kill_driver()

    def alert_text(self):
        '''
        返回 alert/confirm/prompt 中的文字信息
        driver.switch_to_alert().text()
        '''
        text=self.driver.switch_to_alert().text()
        self.log.debug("get alert text success")
        return text

    def alert_accept(self):
        '''
        点击确认按钮
        driver.switch_to_alert().text()
        '''
        self.driver.switch_to_alert().accept()
        self.log.debug("click alert accept success")

    def alert_dismiss(self):
        '''
        点击取消按钮
        driver.switch_to_alert().text()
        '''
        self.driver.switch_to_alert().dismiss()
        self.log.debug("click alert dismiss success")

    def alert_send_keys(self,text):
        '''
        输入值，这个 alert\confirm 没有对话框就不能用了
        driver.switch_to_alert().send_keys()
        '''
        self.driver.switch_to_alert().send_keys(text)
        self.log.debug("send text to alert success")

    def get_size(self, by, value):
        '''
        获取当元素大小
        '''
        element = self.get_element(by, value)
        self.log.debug("get size success,by element '%s'." % by)
        return element.size

    def get_window_size(self):
        '''
        获取当前页面大小
        '''
        element = self.driver.get_window_size()
        self.log.debug("get size success")
        return element

    def get_title(self):
        '''
        获取title
        '''
        self.log.debug('get dirver title.')
        return self.driver.title

    def get_url(self):
        '''
        获取当前页面URL
        '''
        self.log.debug('get dirver current_url.')
        return self.driver.current_url

    def get_text(self, by, value):
        '''
        获取文本
        '''
        element = self.get_element(by, value)
        self.log.debug(f"get text success,by{by} element '{value}'.")
        return element.text

    def get_attribute(self, by, value, name):
        '''
        获取属性
        '''
        element = self.get_element(by, value)
        self.log.debug("get attribute success,by element '%s'." % by)
        return element.get_attribute(name)

    def get_html(self):
        '''
        获取当前网页HTML代码
        '''
        html = self.driver.page_source
        self.log.debug("get source html success")
        return html



    # 使用js进行元素操作

    def js_refresh(self):
        '''
        使用js强制刷新页面
        '''
        js = "location.reload()"
        self.driver.execute_script(js)
        self.log.debug('js_refresh success')

    def js_get_page_html(self):
        '''
        使用js获取整个页面的html
        '''
        js = ("return document.documentElement.outerHTML")
        html = self.driver.execute_script(js)
        self.log.debug('use js get html success')

        return html

    def js_get_inner_html(self,css, index=0):
        '''
        使用js获取元素内部的html
        '''
        self.get_element('css',css)
        js = "return document.querySelectorAll(\'{}\')[{}].innerHTML".format(css,index)
        html = self.driver.execute_script(js)
        self.log.debug('js_get_inner_html success , by %s'%css)

        return html

    def js_click(self,css, index=0):
        '''
        使用js执行点击,只能使用css定位
        js = "document.querySelectorAll('#id')[0].click()"
        driver.execute_script(js)
        '''
        self.get_element('css',css)
        js = "document.querySelectorAll(\'{}\')[{}].click()".format(css,index)
        self.driver.execute_script(js)
        self.log.debug('js_click success , by %s'%css)

    def js_new_window(self):
        '''
        使用js打开新的窗口
        '''
        js = "window.open('','_blank');"
        self.driver.execute_script(js)
        handles = self.driver.window_handles #获取到所有页面handle
        self.driver.switch_to.window(handles[-1]) #跳转到最新页面
        self.log.debug('js_new_window success ')

    def js_input(self,css,text,index=0):
        '''
        使用js输入文本
        js = "document.querySelectorAll('#id')[0].value='text'"
        driver.execute_script(js)
        '''
        self.get_element('css',css)
        js = "document.querySelectorAll(\'{}\')[{}].value=\'{}\'".format(css,index,text)
        self.driver.execute_script(js)
        self.log.debug('js input text: %s success , by %s'%(text,css))

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
        self.log.debug("click label '%s', success" % label)

    def js_scroll_Top(self,number):
        '''
        滚动到顶部
        '''
        js = "window.scrollTo(0,%s)"%number
        self.driver.execute_script(js)
        self.log.debug('Roll to the top!')

    def js_scroll_End(self):
        '''
        滚动到底部
        '''
        js = "window.scrollTo(0,document.body.scrollHight)"
        self.driver.execute_script(js)
        self.log.debug('Roll to the end!')

    def js_div_scrollTop(self,css,number):
        '''
        执行js操作内嵌式div滚动条，上下移动
        number为上下的位置输入数字
        '''
        element = self.get_element('css','%s'%css)
        js = ("document.querySelector(\'%s\').scrollTop=\'%s\'"%(css,str(number)))
        self.driver.execute_script(js)
        self.log.debug('Roll div top to the %d!'%number)

    def js_div_scrollLeft(self,css,number):
        '''
        执行js操作内嵌式div滚动条，左右移动
        number为左右的位置输入数字
        '''
        element = self.get_element('css','%s'%css)
        js = ("document.querySelector(\'%s\').scrollLeft=\'%s\'"%(css,str(number)))
        self.driver.execute_script(js)
        self.log.debug('Roll div left to the %d!'%number)
