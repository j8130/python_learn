# Section0 开场
print("-" * 30 + "Begin Section 0 开场" + "-" * 30)
print("这是Python的第七次课程,主要讲数据的选择:")
print("1.列选择\n2.行选择\n3.行列同时选择")
print("-" * 30 + "End Section 0 开场" + "-" * 30)
print('\n')

import pandas as pd

# Section1 列选择
df = pd.read_excel(r"D:\pycharm2019\project\python_learn\files\lesson7\Lesson7.xlsx")
df.index = ["一", "二", "三", "四", "五"]
print("读入的表格内容为：")
print(df, '\n')

# 只选择名称列
print("只选择了名称列：")
print(df["名称"], '\n')

# 选择名称列和观看次数列
print("选择了名称和观看次数列：")
# 外面的方括号表示要选择列，里面方括号表示列表，列表有多个列
print(df[["名称", "观看次数"]], "\n")

# 通过第几列来选择
# 前面表示第几行，：表示所有行
# 后面表示第几列
print("通过第几列来选择：")
# index location  ：表示想选所有的行   [0, 2] 表示想选择第一列和第三列
print(df.iloc[:, [0, 2]], '\n')

# 想要选择连续几列
print("选择从第一列到第四列（不包括第四列）：")
print(df.iloc[:, 0:3], '\n')

# Section2 行选择

# 只选择第一行  选择行要加location，选择列不需要
print("只选择第一行：")
print(df.loc["一"], "\n")

# 选择第一行和第三行
print("选择第一行和第三行：")
print(df.loc[["一", "三"]], "\n")

# 通过第几行来选择
print("通过第几行来选择：")
print(df.iloc[0], "\n")

print("通过行数来选择第一行和第三行：")
print(df.iloc[[0, 2]], '\n')

# 选择连续的行数
print("选择第一行到第四行（不包括第四行）：")
print(df.iloc[0:3], '\n')

# 选择满足条件的数据
# 记得多个条件加括号  不加可能会出问题
print("选择观看次数超过300以及评论数超过20的数据：")
print(df[(df["观看次数"] > 300) & (df["评论数"] > 20)], "\n")

# Section3 行列同时选择
# loc,iloc
# loc传入的是行/列索引名称，iloc传入的是行/列数
print("行和列都是索引名称：")
print(df.loc[["一", "三"], ["名称", "观看次数"]], "\n")

print("行和列都是索引数：")
print(df.iloc[[0, 2], [0, 1]], '\n')

print("行列中有切片索引：")
print(df.iloc[0:3, [0, 1]], '\n')

# 还有一些根据条件来选择的
print("根据不同的条件来选择：")
# 先选择观看次数大于300，再选择名称和观看次数列查看
print(df[df["观看次数"] > 300][["名称", "观看次数"]], '\n')
