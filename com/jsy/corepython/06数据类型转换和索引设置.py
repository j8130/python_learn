# Section0 开场
print("-" * 30 + "Begin Section 0 开场" + "-" * 30)
print("这是Python的第六次课程,主要讲数据的预处理:")
print("1.数据类型转换\n2.索引设置")
print("-" * 30 + "End Section 0 开场" + "-" * 30)
print('\n')

import pandas as pd

# Section1 数据类型转换
df = pd.read_excel(r"D:\pycharm2019\project\python_learn\files\lesson6\Lesson6.xlsx")
df1 = df
# python里面有6种主要的类型，int，float，object，string，unicode，datetime64[ns]
# 我们现在主要掌握四种 int，float，string，datetimes
# 查看某一列的数据类型，dtype
print("查看观看次数列的数据类型：")
print(df["观看次数"].dtype, "\n")
print("查看发布时间列的数据类型：")
print(df["发布时间"].dtype, '\n')
# 转换某一列的数据类型,astype()
# 将观看次数列的数据类型转换为float
print(df["观看次数"].astype("float64"))
print('\n')

# Section2 索引设置
# 索引就是行标和列标
# 用columns,index来设置
print(df, '\n')
df.index = [1, 2, 3, 4, 5]
print("给表格添加行索引：")
print(df, '\n')
# 用set_index(),指明要用做行索引的列的名称
print("指明名称列当作行索引：")
# 不会改变原先的表格，所以要赋值  上面的 .index 会改变原表格
df = df.set_index("观看次数")
# df.set_index("观看次数")
print(df, '\n')

df = df1
# 重命名列索引
df = df.rename(columns={"发布时间": "新发布时间"})
print("将发布时间改名为新发布时间：")
print(df, '\n')

df = df1
df = df.rename(index={1: "一", 2: "二", 3: "三"})
print("将行索引1，2，3改为一，二，三")
print(df, '\n')
