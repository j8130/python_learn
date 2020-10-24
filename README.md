# python_learn

python基础学习记录

根据菜鸟教程

https://www.runoob.com/python3/python3-basic-syntax.html

后面第3-15小节是 pandas 操作表格实现自动化的案例





## Python操作浏览器配置

Selenium与phantomJS 有兼容问题，不建议使用



安装Chromedriver[下载地址](https://sites.google.com/a/chromium.org/chromedriver/home) 

> win :将解压后的exe放到Python的Scripts目录下

### Linux下环境安装

~~~shell
[root@localhost ~]# pip install selenium
~~~



~~~shell
1、安装chrome
# 用下面的命令安装最新的 Google Chrome

yum install https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
# 也可以下载到本地再安装
wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
yum install ./google-chrome-stable_current_x86_64.rpm

# 安装必要的库
yum install mesa-libOSMesa-devel gnu-free-sans-fonts wqy-zenhei-fonts

2、安装 chromedriver
chrome官网 wget https://chromedriver.storage.googleapis.com/2.38/chromedriver_linux64.zip
淘宝源（推荐）wget http://npm.taobao.org/mirrors/chromedriver/2.41/chromedriver_linux64.zip 

# 将下载的文件解压，放在如下位置
unzip -d /usr/bin chromedriver_linux64.zip

# 给予执行权限
chmod +x /usr/bin/chromedriver

~~~



新建测试代码 main.py

~~~python
from selenium import webdriver
import time

# 这三行是为了linux执行不弹窗
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')

driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)
driver.get('https://www.baidu.com/')

time.sleep(5)
print(driver.page_source)

~~~

运行

~~~shell
/usr/anaconda3/bin/python3.8 /home/jsy/kafka-consumer/NJUBookListener.py
~~~

