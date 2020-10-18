from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# PhantomJS 本质上是一个没有窗口的浏览器
# 1. 自动输入
driver = webdriver.PhantomJS(executable_path="D:\\develop\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
driver.get("https://www.baidu.com/")
time.sleep(3)

print(driver.get_cookies())
# 截图
driver.save_screenshot('baidu.png')

driver.find_element_by_id('kw').send_keys('123')
driver.save_screenshot('baidu2.png')

# 2. 模拟点击  模拟点击也是一种常用反 反爬的方式
# 2.1 键盘模拟点击
# 回车
# driver.find_element_by_id('kw').send_keys(Keys.RETURN)
# time.sleep(5)
# driver.back()  # 后退
# driver.forward() # 前进
# driver.refresh() # 刷新
# driver.save_screenshot('baidu3.png')

# ctrl+a
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')
# driver.save_screenshot('baidu4.png')

# 清除输入内容
# driver.find_element_by_id('kw').clear()

# 2.2 鼠标点击
driver.find_element_by_id('su').click()
time.sleep(3)
driver.save_screenshot('baidu5.png')

