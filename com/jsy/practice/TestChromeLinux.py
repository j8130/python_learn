from selenium import webdriver
import time

# 这三行是为了linux执行不弹窗
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')

# driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)

driver = webdriver.Chrome()

# 首页
driver.get('https://www.baidu.com')  # get方式访问百度.
time.sleep(2)
print('[' + time.strftime("%Y/%m/%d: %H:%M:%S") + '] ' + 'the book [] can not borrow')

print('success')

# 都可以退出   一般用quit
# quit方法就是直接退出并关闭所有关联的tab窗口。close方法一般关闭一个tab，quit方法才是我们认为的完全关闭浏览器方法，
driver.quit()
# close方法是关闭当前窗口
# driver.close
