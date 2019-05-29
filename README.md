# test
python+selenium自动化测试框架
这是我自己使用的一个自动化框架，包含组织用例，批量运行，生成运行日志，html报告，
自动发送邮件到指定邮箱（公司外网有限制，我的不能使用）
使用po设计模式封装，

注：没有生成excel报告，多浏览器、多线程、分布式执行等模块，后续会继续添加，丰富自动化框架
常用的文件在soft文件夹中

清华大学开源软件镜像站：https://mirror.tuna.tsinghua.edu.cn/help/gitlab-ce/

各种浏览器驱动下载地址：https://www.seleniumhq.org/download/
火狐：  https://github.com/mozilla/geckodriver/releases
谷歌：  http://chromedriver.storage.googleapis.com/index.html
IE：    http://selenium-release.storage.googleapis.com/index.html
Edge： https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
Opera：https://github.com/operasoftware/operachromiumdriver/releases
PhantomJS：http://phantomjs.org/

附上谷歌对照表：
chromedriver版本	支持的Chrome版本
v2.46	v71-73
v2.45	v70-72
v2.44	v69-71
v2.43	v69-71
v2.42	v68-70
v2.41	v67-69
v2.40	v66-68
v2.39	v66-68
v2.38	v65-67
v2.37	v64-66
v2.36	v63-65
v2.35	v62-64
v2.34	v61-63
v2.33	v60-62
v2.32	v59-61
v2.31	v58-60
v2.30	v58-60
v2.29	v56-58
v2.28	v55-57
v2.27	v54-56
v2.26	v53-55
v2.25	v53-55
v2.24	v52-54
v2.23	v51-53


https://blog.csdn.net/xueyingqi/article/details/53216506

Python中strip用法：https://blog.csdn.net/u012671171/article/details/52024874
https://yq.aliyun.com/articles/35613


https://blog.csdn.net/bsfz_2018/article/details/79505929

按Win+R键打开运行对话框，输入 regedit.exe ，准备修改注册表； 
找到 HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Explorer； 
新建一个键名称为 “Max Cached Icons” 数据设置为 “2000”； 
重启一下电脑，图标就可以显示了。



Python链接数据库
https://blog.csdn.net/fanyingkk/article/details/79708706

读取
https://blog.csdn.net/kongxx/article/details/7107661

Oracle不能链接
https://blog.csdn.net/hzs8716/article/details/68924850

html5
http://www.w3school.com.cn/tags/html_ref_audio_video_dom.asp

CSS font-family中文字体英文名称展示
https://www.zhangxinxu.com/study/201703/font-family-chinese-english.html

https://www.cnblogs.com/cwp-bg/p/python.html

字体和英文对照
https://www.zhangxinxu.com/study/201703/font-family-chinese-english.html

https://blog.csdn.net/allan_shore_ma/article/details/62066775

Jenkins插件下载
https://mirrors.tuna.tsinghua.edu.cn/jenkins/plugins/


EF
https://ec.ef.com.cn/partner/englishcenters/cn

配置sublime运行rbotframework
https://www.jianshu.com/p/07ae62d2c63f

Docker教程：http://www.runoob.com/docker/windows-docker-install.html
https://blog.csdn.net/u011681409/article/details/82695087

sublime插件下载：https://packagecontrol.io/browse

学习网站：http://www.runoob.com/

w3cscholl：https://www.w3cschool.cn/
http://www.w3school.com.cn/index.html

python上传文件：
  PyUserInput：https://github.com/PyUserInput/PyUserInput
  pyHook：https://www.lfd.uci.edu/~gohlke/pythonlibs/
  使用：https://blog.csdn.net/shij19/article/details/53046048
  
  
 cmd常用命令：
 https://www.cnblogs.com/yongfengnice/p/6752211.html
https://jingyan.baidu.com/article/4b07be3c907e6f48b280f36d.html

Mac搭建
Python中strip用法：https://blog.csdn.net/u012671171/article/details/52024874Python
Python中strip用法：https://blog.csdn.net/u012671171/article/details/5202487

MAC搭建Python+Selenium环境
把驱动放到:/usr/local/bin下即可
python官方文档:https://tappy.readthedocs.io/en/latest/producers.html#examples

linux常用插件下载：http://mirrors.163.com/centos/7/os/x86_64/Packages/
linux配置环境变量：https://jingyan.baidu.com/article/b87fe19e6b408852183568e8.html

selenium的chromedriver参数add_argument
https://peter.sh/experiments/chromium-command-line-switches/
https://blog.csdn.net/weixin_43968923/article/details/87899762
启动参数	作用
--user-data-dir 用户配置文件路径
--user-agent=""	设置请求头的User-Agent
--window-size=1366,768	设置浏览器分辨率（窗口大小）
--headless	无界面运行（无窗口）
--start-maximized	最大化运行（全屏窗口）
--incognito	隐身模式（无痕模式）
--disable-javascript	禁用javascript
--disable-infobars	禁用浏览器正在被自动化程序控制的提示

https://blog.csdn.net/weixin_43968923/article/details/87899762
chrome_options.add_argument('--user-agent=""')  # 设置请求头的User-Agent
chrome_options.add_argument('--window-size=1280x1024')  # 设置浏览器分辨率（窗口大小）
chrome_options.add_argument('--start-maximized')  # 最大化运行（全屏窗口）,不设置，取元素会报错
chrome_options.add_argument('--disable-infobars')  # 禁用浏览器正在被自动化程序控制的提示
chrome_options.add_argument('--incognito')  # 隐身模式（无痕模式）
chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
chrome_options.add_argument('--disable-javascript')  # 禁用javascript
chrome_options.add_argument('--blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面

chrome_options.add_argument('--ignore-certificate-errors')  # 禁用扩展插件并实现窗口最大化
chrome_options.add_argument('--disable-gpu')  # 禁用GPU加速
chrome_options.add_argument('–disable-software-rasterizer')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--start-maximized')

--disable-infobars	禁用浏览器正在被自动化程序控制的提示
