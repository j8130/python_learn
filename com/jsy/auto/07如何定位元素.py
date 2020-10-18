# 定位单个元素  多一个根据id定位  优先使用id，定位准确

# 定位多个元素  element -> elements

from selenium import webdriver

import time

driver = webdriver.PhantomJS(executable_path="D:\\develop\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
driver.get("https://www.python.org/")
time.sleep(3)

# 1. by_id = driver.find_element_by_id("downloads").get_attribute("innerHTML")
# print(by_id)

# 2. by_name = driver.find_element_by_name("q").get_attribute("placeholder")
# print(by_name)

# 3. 根据xpath  .text 获取内部文字，即两个a标签之间的内容
# by_xpath = driver.find_element_by_xpath('//*[@id="touchnav-wrapper"]/header/div/div[1]/a').text
# print(by_xpath)

# 4. 根据超链接  是定位到a标签
# by_link_text = driver.find_element_by_link_text('Start with our Beginner’s Guide').get_attribute('href') # 全部超链接文字
# by_partial_link_text = driver.find_element_by_partial_link_text('Beginner’s Guide').get_attribute("href") # 部分超链接文字
# print(by_link_text)
# print(by_partial_link_text)

# 5. 根据tag name  针对表格等需要多个同类的，要获取所有信息
# 不加s返回的是第一个
# by_tag_name = driver.find_element_by_tag_name('meta').get_attribute('outerHTML')
# print(by_tag_name)
#
# by_tag_names = driver.find_elements_by_tag_name('meta')
# for i in by_tag_names:
#     print(i.get_attribute("outerHTML"))

# 6. 根据class name  class很有可能重复  tip :outer 是整个标签，inner 是标签内部
# by_class_name = driver.find_element_by_class_name('jump-to-menu').get_attribute('outerHTML')
# print(by_class_name)

# 7. 标签名+class名 的组合   <span class="menu-icon">
by_css_selector = driver.find_element_by_css_selector('span.menu-icon').get_attribute('outerHTML')
print(by_css_selector)



driver.close()