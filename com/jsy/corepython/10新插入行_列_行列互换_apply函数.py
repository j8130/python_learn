# Section0 开场
print("-" * 30 + "Begin Section 0 开场" + "-" * 30)
print("这是Python的第十次课程,主要讲数据操作:")
print("1.插入新的行或列\n2.行列互换\n3.apply()与applymap()函数\n")
print("-" * 30 + "End Section 0 开场" + "-" * 30)
print('\n')

import pandas as pd
import copy

df1 = pd.read_excel(r"D:\pycharm2019\project\python_learn\files\lesson10\Lesson10.xlsx", sheet_name="Sheet1")
df2 = pd.read_excel(r"D:\pycharm2019\project\python_learn\files\lesson10\Lesson10.xlsx", sheet_name="Sheet2")
print(df1)
print(df2)

# Section 1 插入新的行或列
# 插入行，相当于将合并两个文件, 前提是两个文件列索引是一样的
print("合并两个excel文件")
df = pd.concat([df1, df2])
df.index = [0, 1, 2, 3, 4, 5, 6]
df3 = df.copy()

# 插入列，插入顶的人数列
# insert(),需要知道插入的位置，列的名称，以及数据
print("在第四列插入顶的人数列")
df.insert(3, "顶的人数", [10, 13, 15, 19, 12, 20, 24])

df = df3.copy()

# 直接增加一列在最后面
print("在最后一列加入顶的人数列")
df["顶的人数"] = [10, 13, 15, 19, 12, 20, 24]
print(df)

# Section 2 行列互换
print("行列互换：")
print(df.T)

df = df3.copy()
# Section3 apply()与applymap()函数
for index in range(len(df["观看次数"])):
    df.loc[index, "观看次数"] = df.loc[index, "观看次数"] + 1

print("将观看次数列每个都加1：")
# 深拷贝，必须要在内存里面新开辟一个地方，不然修改df会同时修改
# df3
df = df3.copy()

print("用apply实现将观看次数都加1：")
# lambda 表示匿名函数
df["观看次数"] = df["观看次数"].apply(lambda x: x + 1)

print(df)

print("applymap() 就是针对整张表格的apply，但是要注意每列的数据类型不一样，比如说时间加1，程序就不知道如何处理了，就会报错")
