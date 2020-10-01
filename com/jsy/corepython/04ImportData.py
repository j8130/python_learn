# Section0 开场
print("-" * 30 + "Begin Section 0 开场" + "-" * 30)
print("这是Python的第四次课程,主要讲Pandas去获取数据源:")
print("1.导入数据\n2.熟悉数据")
print("-" * 30 + "End Section 0 开场" + "-" * 30)
print('\n')

import pandas as pd

print("-" * 30 + "Begin Section 1 导入数据" + "-" * 30)
# Section1 导入数据
# 导入数据主要用到的是read_x()方法，x表示待导入文件的格式
# 导入.xlsx文件，用read_excel()
# 这里需要先安装软件 pip install xlrd
# 把文件拖到终端就能得到路径 读路径一定要加 r
df = pd.read_excel(r"D:\pycharm2019\project\python_learn\files\lesson4\Lesson4.xlsx")
print("1.excel的数据是", "*" * 15)
print(df, "\n")

# 指定哪个sheet
df = pd.read_excel(r"D:\pycharm2019\project\python_learn\files\lesson4\Lesson4.xlsx", sheet_name="Sheet1")
print("2.excel的数据是", "*" * 15)
print(df, "\n")

# 或者指定sheet的顺序,从0开始
df = pd.read_excel(r"D:\pycharm2019\project\python_learn\files\lesson4\Lesson4.xlsx", sheet_name=0)
print("3.excel的数据是", "*" * 15)
print(df, "\n")

# 指定哪一列做为行索引  不指明是从0开始，递增作为行索引
df = pd.read_excel(r"D:\pycharm2019\project\python_learn\files\lesson4\Lesson4.xlsx", index_col=0)
print("4.excel的数据是", "*" * 15)
print(df, "\n")

# 指定哪一行作为列索引
df = pd.read_excel(r"D:\pycharm2019\project\python_learn\files\lesson4\Lesson4.xlsx", header=0)
print("5.excel的数据是", "*" * 15)
print(df, "\n")

# 指定导入列,传入需要保存的列数列表  期望只导入第1列和第4列
df = pd.read_excel(r"D:\pycharm2019\project\python_learn\files\lesson4\Lesson4.xlsx", usecols=[0, 3])
print("6.excel的数据是", "*" * 15)
print(df, "\n")

# csv是把Excel的内容以 分隔符 分隔开，没有那么多格式，文件更小，Excel另存为有两种编码格式 gbk 与 utf8，最好存为utf8
# 导入.csv文件,用read_csv()
df = pd.read_csv(r"D:\pycharm2019\project\python_learn\files\lesson4\Lesson4_csv.csv")
print("1.csv的数据是", "*" * 15)
print(df, "\n")

# csv的间隔符不是,需要指明间隔符
# 错误
df = pd.read_csv(r"D:\pycharm2019\project\python_learn\files\lesson4\Lesson4_csv_blank.csv")
print("2.csv的数据是", "*" * 15)
print(df, "\n")

# 正确
df = pd.read_csv(r"D:\pycharm2019\project\python_learn\files\lesson4\Lesson4_csv_blank.csv", sep=' ')
print("3.csv的数据是", "*" * 15)
print(df, "\n")

# 指明读取行数,nrows
df = pd.read_csv(r"D:\pycharm2019\project\python_learn\files\lesson4\Lesson4_csv_blank.csv", sep=' ', nrows=2)
print("4.csv的数据是", "*" * 15)
print(df, "\n")

# 如果另存的是 CSV(逗号分隔)(*.csv) 则需要指定编码格式为gbk
df = pd.read_csv(r"D:\pycharm2019\project\python_learn\files\lesson4\Lesson4_csv_gbk.csv", encoding="gbk")
print("5.csv的数据是", "*" * 15)
print(df, "\n")

# 导入txt文件
# read_table(),是导入利用分隔符分开文件的通用函数
# 不仅可以导入.txt文件，还可以导入.csv文件
df = pd.read_table(r"D:\pycharm2019\project\python_learn\files\lesson4\Lesson4_csv_blank.txt", sep=" ")
print("1.txt的数据是", "*" * 15)
print(df, "\n")
print("-" * 30 + "End Section 1 导入数据" + "-" * 30)
print("\n")

# Section 2熟悉数据
print("-" * 30 + "Begin Section 2 熟悉数据" + "-" * 30)
# 用head()控制显示前几行,默认是5行
print("显示前3行数据:")
print(df.head(3), "\n")

# 用shape获取数据表的大小
print("数据表的大小:")
print(df.shape, "\n")

# 用info获取数据类型
print("数据类型:")
print(df.info(), "\n")

# 获取数据分布  只会统计数值类型的，不会统计String类型的
print("数据分布:")
print(df.describe(), "\n")
print("-" * 30 + "End Section 2 熟悉数据" + "-" * 30)
print("\n")
