from selenium import webdriver

import time

# 需要下载 phantomjs  https://phantomjs.org/download.html
# 初始化drive
driver = webdriver.PhantomJS(executable_path="D:\\develop\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
# 打开网页
driver.get("https://study.163.com/course/introduction/1006084069.htm")
# 睡15秒保证加载完成
time.sleep(15)
data = driver.find_element_by_id("j-coursehead").text

print(data)
# 取两个换行符之间的内容即销量
a = data.find("\n")
b = data[a + 1:].find("\n")
new_data = data[a + 1:a + 1 + b]
print(new_data)
# 关闭页面
driver.quit()


