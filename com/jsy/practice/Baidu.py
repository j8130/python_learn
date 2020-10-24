from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.PhantomJS(executable_path="D:\\develop\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
driver.get("https://www.baidu.com/")
time.sleep(2)

driver.save_screenshot('homepage.png')
driver.find_element_by_id('kw').send_keys('flink')

search = driver.find_element_by_id('su')
print(search)
search.click()

time.sleep(3)
driver.save_screenshot('searchresult.png')