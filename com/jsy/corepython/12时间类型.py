# Section0 开场
print("-" * 30 + "Begin Section 0 开场" + "-" * 30)
print("这是Python的第十二次课程,主要讲时间序列:")
print("1.获取当前时刻的时间\n2.指定日期和时间的格式\n3.字符串和时间格式的互换\n4.时间索引\n5.时间运算")
print("-" * 30 + "End Section 0 开场" + "-" * 30)
print('\n')

# py自带的库
from datetime import datetime

# Section1 获取当前时刻的时间

print("获取当前时刻的时间：")
print(datetime.now())

print("返回当前时刻的年、月、日")
# 年月日是属性，不需要加括号
print("年：", datetime.now().year)
print("月：", datetime.now().month)
print("日：", datetime.now().day)

print("返回今天是周几：")
# Python中周一返回0，周日返回6
print(datetime.now().weekday())

print("返回今天是一年中的第几周：")
print(datetime.now().isocalendar())
print("\n")

# Section2 指定日期和时间的格式
print("只显示日期：")
print(datetime.now().date())

print("只显示时间：")
print(datetime.now().time())

# strftime() 可以显示一些自定义格式
# 显示成 2020-08-09 15:08:15 这样子的格式
# string format time   可以百度，很多种格式可以写
print("strftime 显示自定义格式：")
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print('\n')

# Section3 字符串和时间格式互相转换
# now变量是一个时间类型
now = datetime.now()
print(now, type(now))

# 用str()就可以将任意类型转换成字符串
print(str(now), type(str(now)))

# 将字符串解析成时间
from dateutil.parser import parse

str_now = "2020-08-08"
time_now = parse(str_now)
print(time_now, type(time_now))
print("\n")

# Section4 时间索引
# 可以筛选从某个时刻到某个时刻的数据
import pandas as pd

df = pd.read_excel(r"D:\pycharm2019\project\python_learn\files\lesson12\Lesson12.xlsx")
print(df)

print("选择发布时间是2020-07-02的数据：")
print(df[df["发布时间"] == datetime(2020, 7, 2)])

print("选择发布时间在2020-07-05之后以及在2020-07-18之前的数据：")
# 7 不能写成 07
print(df[(df["发布时间"] > datetime(2020, 7, 5)) & (df["发布时间"] < datetime(2020, 7, 18))])
print("\n")

# Section5 时间运算
print("获得两个时间的差：")
# timedelta
delta = datetime(2020, 5, 21, 21, 59, 30) - datetime(2013, 5, 22, 23, 48, 12)
print("时间差：")
print(delta)
print("相差天数：")
print(delta.days)
print("相差秒数：")
print(delta.seconds)

# 时间加减，就是把时间往后一天或者提前一小时 引入3个方法
from pandas.tseries.offsets import Day, Hour, Minute

date = datetime(2008, 8, 8, 20, 0, 0)

print("往后推迟一天：")
# Day(1) 时间类型
print(date + Day(1))

print("往后推迟10分钟：")
print(date + Minute(10))

print("往前提前2个小时：")
print(date - Hour(2))
