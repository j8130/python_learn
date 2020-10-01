# Section0 开场
print("-" * 30 + "Begin Section 0 开场" + "-" * 30)
print("这是Python的第五次课程,主要讲数据的预处理:")
print("1.缺失值处理\n2.重复值处理")
print("-" * 30 + "End Section 0 开场" + "-" * 30)
print('\n')

import pandas as pd
import datetime

# Section1 缺失值处理
# 对于缺失值，我们一般有两种处理方式
# 1.删除 2.用某个值填充

# 缺失值查找
# 用info()

df = pd.read_excel(r"D:\pycharm2019\project\python_learn\files\lesson5\Lesson5.xlsx")
# NaN not a number    NaT not a time
print(df, '\n')
print("用df查找缺失值:", '*' * 15)
print(df.info(), '\n')

# 单元格时空值返回true
print("用isnull()查找缺失值:", '*' * 15)
print(df.isnull(), '\n')

# 缺失值删除，dropna()
df1 = df
print("刪除存在空值的行", "*" * 15)
print(df.dropna())

df = df1
print("只刪除全为空值的行", "*" * 15)
print(df.dropna(how="all"))

# 缺失值填充，用fillna()
df = df1
print("将缺失值填充为0", "*" * 15)
print(df.fillna(0), '\n')

# 也可以根据不同的列填充不同的值
df = df1
print("将顶踩比例填充为0，将发布时间填充为2020/7/20", "*" * 15)
dateTime_p = datetime.datetime.strptime("2020/7/20 00:00:00", r'%Y/%m/%d %H:%M:%S')
# 根据列索引填充不同的值
print(df.fillna({"顶踩比例": 0, "发布时间": dateTime_p}))

# Section2 重复值处理
# 对重复值一般做删除处理
df = pd.read_excel(r"D:\pycharm2019\project\python_learn\files\lesson5\Lesson5.xlsx", sheet_name="Sheet2")
df1 = df
# 用drop_duplicates()，用keep设置保留第几个,默认第一个,first,last,false(表明都删除)
print("删除名称相同的行:", "*" * 15)
print(df.drop_duplicates(subset="名称", keep="last"), "\n")

# 也可以传入多个列名，表示都相同时才删除，其中几个一样不删除
print("删除名称和观看次数都相同的行", "*" * 15)
print(df.drop_duplicates(subset=["名称", "观看次数"]), "\n")
