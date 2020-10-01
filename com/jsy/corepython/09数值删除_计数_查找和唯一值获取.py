# Section0 开场
print("-" * 30 + "Begin Section 0 开场" + "-" * 30)
print("这是Python的第九次课程,主要讲数据操作:")
print("1.数值删除\n2.数值计数\n3.唯一值获取\n4.数值查找\n")
print("-" * 30 + "End Section 0 开场" + "-" * 30)
print('\n')

import pandas as pd

df = pd.read_excel(r"D:\pycharm2019\project\python_learn\files\lesson9\Lesson9.xlsx")
df.index = ["0a", "1b", "2c", "3d", "4e"]
df1 = df
print(df)

# Section1 数值删除
# drop()函数,axis = 1 表示删除列
# 传入列名删除列
print("删除名称和顶踩比例列：")
print(df.drop(["名称", "顶踩比例"], axis=1))

# 传入列号删除列
print("删除第1列和第4列：")
print(df.drop(df.columns[[0, 3]], axis=1))

# axis = 0 表示删除行
# 传入行名删除行
print("删除0a行和2c行：")
print(df.drop(["0a", "2c"], axis=0))

# 传入行号删除行
print("删除第一行和第三行：")
print(df.drop(df.index[[0, 2]], axis=0))

# Section2 数值计数
# 查看某个值出现的次数
print("查看顶踩比例中的数值的出现次数分布：")
print(df["顶踩比例"].value_counts())

print("查看顶踩比例中的数值出现的百分比：")
print(df["顶踩比例"].value_counts(normalize=True))

# Section3 获取唯一值
# 获取某列的非重复值  如果有两个
# 先把那列复制一份，然后用unique来获取
print("获取顶踩比例列中唯一值：")
print(df["顶踩比例"].unique())

# Section4 数值查找
# 可以是针对某列的，也可以是针对整张表格
# 只要是包含列表中其中一个就返回true
print("查看观看次数列有没有480和235：")
print(df["观看次数"].isin([480, 235]))

print("查看全表中是否有480和235：")
print(df.isin([480, 235]))
