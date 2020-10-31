from selenium import webdriver
import time
from kafka import KafkaProducer
import json

# 这三行是为了linux执行不弹窗
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')

driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)

# driver = webdriver.Chrome()

book_list = ["Flink内核原理与实现", "Spark大数据编程实用教程", "Flink原理、实战与性能优化.大数据技术丛书", "Flink基础教程.图灵程序设计丛书"]


def can_borrow():
    flag = driver.find_element_by_class_name('can_borrow').get_attribute('innerHTML').strip() == '可借'
    return flag


def send(bookName):
    producer = KafkaProducer(
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        bootstrap_servers=['192.168.124.102:9092']
    )
    producer.send('pyTest', bookName)
    producer.close()


# 首页
driver.get(
    "http://weixin.libstar.cn/weixin/getIndexPage?mappingPath=njulib&pubId=2&groupCode=200027&code=041yaf0w3yFV2V2Sgf0w36cJIQ1yaf0R&state=STATE")
time.sleep(2)

for bookName in book_list:
    driver.find_element_by_id('searchFieldContent').send_keys(bookName)
    driver.find_element_by_xpath('/html/body/div[1]/a/i').click()
    time.sleep(3)

    # 搜索结果页
    className = driver.find_elements_by_class_name('weui-media-box__title')
    # 遍历搜索结果
    for name in className:
        if (name.get_attribute('innerHTML') == bookName):
            name.click()
            time.sleep(2)
            flag = can_borrow()
            if flag:
                print('[' + time.strftime("%Y/%m/%d: %H:%M:%S") + '] ' + 'the book [' + bookName + '] can borrow')
                send(bookName)
            else:
                print('[' + time.strftime("%Y/%m/%d: %H:%M:%S") + '] ' + 'the book [' + bookName + '] can not borrow')
            break
    # 回退初始位置
    driver.back()
    driver.back()
    driver.refresh()
    time.sleep(2)
