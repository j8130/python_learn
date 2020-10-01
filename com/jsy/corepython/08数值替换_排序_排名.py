# Section0 开场
print("-" * 30 + "Begin Section 0 开场" + "-" * 30)
print("这是Python的第八次课程,主要讲数据操作:")
print("1.数值替换\n2.数值排序\n3.数值排名")
print("-" * 30 + "End Section 0 开场" + "-" * 30)
print('\n')

import pandas as pd

df = pd.read_excel(r"D:\pycharm2019\project\python_learn\files\lesson8\Lesson8.xlsx")
df1 = df
print(df, "\n")

# Section1 数值替换
# 一对一替换
# 将顶踩比例 200.00% 替换成 100.00%
# 一定要重新赋值给顶踩比例
print("将顶踩比例 200.00% 替换成 100.00%")
df['顶踩比例'] = df['顶踩比例'].replace(2.000, 1.000)
print(df, '\n')

df = df1
# 也可以将所有2.000 替换成 1.000
print("将所有的 2.000 替换成 1.000")
df = df.replace(2.000, 1.000)
print(df, '\n')

# 多对一替换
df = df1
# 将 480 或 342 的替换成 1314
print("多对一替换：")
df = df.replace([480, 342], 1314)
print(df, '\n')

# 多对多替换
df = df1
print("多对多替换：")
# 字典，把480 替换成 400，把 342 替换成 300
df = df.replace({480: 400, 342: 300})
print(df, '\n')

df = df1

# Section2 数值排序

# 按照观看次数升序排列    默认为True
print("按照观看次数升序排列：")
print(df.sort_values(by=["观看次数"], ascending=True))

print("按照观看次数降序排列：")
print(df.sort_values(by=["观看次数"], ascending=False))

# 将第二行的发布时间设为None
df.loc[[1], ["发布时间"]] = None
print("将第二行的发布时间设为None：")
print(df)

# 按照发布时间从晚到早拍，空值排在最开始
print("按照发布时间从晚到早拍，空值排在最开始：")
print(df.sort_values(by=["发布时间"], ascending=False, na_position="first"))

print("按照发布时间从早到晚拍，空值排在最后：")
print(df.sort_values(by=["发布时间"], na_position="last"))

# 按照多列排序
# 按照顶踩比例降序，观看次数升序排列
print("先按照顶踩比例降序，再观看次数升序排列：")
print(df.sort_values(by=["顶踩比例", "观看次数"], ascending=[False, True]))

# Section3 数值排名
# 用rank(ascending,method)函数进行排名
# ascending表明是升序还是降序，method有average、first、min、max 这4种取值
# 按照顶踩比例，降序排列
print("顶踩比例：")
print(df["顶踩比例"])
# average   重复排名取平均，比如第一名和第二名一样，则 （1+3）/2 两人都是1.5名
print(df["顶踩比例"].rank(ascending=False, method="average"))

# first  谁在前面就按照谁的排名大        应该是最常用
print(df["顶踩比例"].rank(ascending=False, method="first"))

# min      取最小值，第一名和第二名一样，则两人都是第一名
print(df["顶踩比例"].rank(ascending=False, method="min"))

# max      取最大值，第一名和第二名一样，则两人都是第二名
print(df["顶踩比例"].rank(ascending=False, method="max"))
