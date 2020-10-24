from selenium import webdriver
import time

print("24小时格式：" + time.strftime("%H:%M:%S"))
print("12小时格式：" + time.strftime("%I:%M:%S"))
print("今日的日期：" + time.strftime("%d/%m/%Y"))

print("今日的日期：" + time.strftime("%Y/%m/%d: %H:%M:%S"))
