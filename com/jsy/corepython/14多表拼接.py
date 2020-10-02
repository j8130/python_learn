# Section0 开场
print("-" * 30 + "Begin Section 0 开场" + "-" * 30)
print("这是Python的第十四次课程,主要讲多表拼接:")
print("1.表的横向拼接\n2.表的纵向拼接")
print("-" * 30 + "End Section 0 开场" + "-" * 30)
print('\n')

import pandas as pd

# Section1 表的横向拼接
# 连接表的类型
# 一对一,表示两个表的公共列中都是没有重复值的  公共列是指没有重复的列

filePath = r"D:\pycharm2019\project\python_learn\files\lesson14\Lesson14.xlsx"
df1 = pd.read_excel(filePath, sheet_name="Sheet1")
df2 = pd.read_excel(filePath, sheet_name="Sheet2")
print("df1:")
print(df1)

print("df2:")
print(df2)

print("一对一连接：")
print(pd.merge(df1, df2))

# 多对一，表示两个表的公共列，一个有重复值，一个没有
df3 = pd.read_excel(filePath, sheet_name="Sheet3")
print("df3:")
print(df3)

print("多对一拼接：")
# 会拼成多条
print(pd.merge(df1, df3))

# 多对多，表示两个表的公共列都是有重复值
df4 = pd.read_excel(filePath, sheet_name="Sheet4")
print("df4:")
print(df4)

print("多对多拼接：")
print(pd.merge(df3, df4))

# 连接键的类型
# 默认是以公共列为键
# 用 on 指定键
df5 = pd.read_excel(filePath, sheet_name="Sheet5")
print("df5:")
print(df5)
print("多个列作为键拼接：")
print(pd.merge(df1, df5, on=["姓名", "学号"]))

# 可以分别指定左右连接键
df6 = pd.read_excel(filePath, sheet_name="Sheet6")
print("df6:")
print(df6)
print("分别指定左右连接键：")
print(pd.merge(df1, df6, left_on="姓名", right_on="名字"))

# 可以把索引列作为键
print("指定索引列为键：")
print(pd.merge(df1, df6, left_index=True, right_index=True))

# 连接方式
# 当公共列中左表的值无法在右表全部找到，或者右表的值无法在左表中全部找到
df7 = pd.read_excel(filePath, sheet_name="Sheet7")
print("df1:")
print(df1)
print("df7:")
print(df7)

# 内链接是默认的，选两个都有的    交集
print("内链接：")
print(pd.merge(df1, df7, how="inner"))

# 左链接，以左表为主   右表没有填充空值
print("左链接：")
print(pd.merge(df1, df7, how="left"))

# 右链接，以右表为主
print("右链接：")
print(pd.merge(df1, df7, how="right"))

# 外链接，选两个的并集
print("外链接：")
print(pd.merge(df1, df7, how="outer"))

# Section2 表的纵向拼接
df8 = pd.read_excel(filePath, sheet_name="Sheet8")
df9 = pd.read_excel(filePath, sheet_name="Sheet9")
print("df8:")
print(df8)
print("df9:")
print(df9)

print("普通拼接：")
print(pd.concat([df8, df9]))

print("索引设置：")
# ignore_index=True 忽略之前的index，重新指定index
print(pd.concat([df8, df9], ignore_index=True))

# 有重复值
df10 = pd.read_excel(filePath, sheet_name="Sheet10")
print("df10:")
print(df10)

print("存在重复值：")
print(pd.concat([df9, df10], ignore_index=True))

print("删除重复值：")
print(pd.concat([df9, df10], ignore_index=True).drop_duplicates())
