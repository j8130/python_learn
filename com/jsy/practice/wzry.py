from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')

driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)

# driver = webdriver.Chrome()

id = ''
password = ''

# 首页
driver.get(
    "https://pvp.qq.com/cp/a20161115tyf/page2.shtml")
time.sleep(2)

driver.find_element_by_xpath('/html/body/div[3]/div/a[2]').click()
time.sleep(2)

login_Iframe = driver.find_element_by_id('loginIframe')
driver.switch_to_frame(login_Iframe)

driver.find_element_by_id('switcher_plogin').click()
time.sleep(1)

driver.find_element_by_id('u').send_keys(id)
driver.find_element_by_id('p').send_keys(password)
driver.find_element_by_id('login_button').click()
time.sleep(2)

driver.find_element_by_xpath('/html/body/div[4]/div/div/div[6]/div[1]/ul/li[3]/a').click()
print('签到成功' + time.strftime("%Y/%m/%d: %H:%M:%S"))
driver.quit()
