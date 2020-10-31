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
driver.quit()
