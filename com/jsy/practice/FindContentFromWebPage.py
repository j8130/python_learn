from selenium import webdriver
import time
from kafka import KafkaProducer
import json

# 这三行是为了linux执行不弹窗
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
#
# driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)

driver = webdriver.Chrome()


def send(bookName):
    producer = KafkaProducer(
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        bootstrap_servers=['10.10.110.12:9092']
    )
    producer.send('pyTest', bookName)
    producer.close()


# 首页
driver.get(
    "https://www.52pojie.cn/thread-1311004-1-1.html")
time.sleep(2)

contains__ = driver.page_source.__contains__("久坐")
if (contains__):
    print("存在")

driver.quit()
