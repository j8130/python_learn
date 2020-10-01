# Section0 开场
print("-" * 30 + "Begin Section 0 开场" + "-" * 30)
print("这是Python的第三次课程,主要讲Pandas第三方库,内容主要包括:")
print("1.Series\n2.DataFrame")
print("-" * 30 + "End Section 0 开场" + "-" * 30)
print('\n')

# 首先需要安装和引入pandas
import pandas as pd

# Series
print("-" * 30 + "Begin Section 1 Series" + "-" * 30)
# Series是一种类似于一维数组的对象，由一组数据和一组与之相关联的索引组成
# 默认的索引从0开始
print("传入列表,默认索引：")
S1 = pd.Series(['a', 'b', 'c', 'd'])
print(S1)

# 传入索引
print("传入列表，自定义索引：")
S2 = pd.Series(['a', 'b', 'c', 'd'], index=[1, 2, 3, 4])
print(S2)

# 传入字典，key为索引，value为数据
print("传入字典：")
S3 = pd.Series({1: 'a', 2: 'b', 3: 'c', 4: 'd'})
print(S3)

# index获得索引
print("index 获得索引：")
print(S1.index)
print(S2.index)

# values获得值
print("values 获得值：")
print(S1.values)
print(S2.values)

print("-" * 30 + "End Section 1 Series" + "-" * 30)
print("\n")

# DataFrame     二维，很像Excel
print("-" * 30 + "Begin Section 2 DataFrame" + "-" * 30)
# DataFrame是由一组数据与一对索引（行索引和列索引）组成的表格型数据结构
# 默认的行索引和列索引都是从0开始
print("传入列表，默认行索引和列索引：")
df1 = pd.DataFrame(['a', 'b', 'c', 'd'])
print(df1)

print("传入一个嵌套列表：")
df2 = pd.DataFrame([['a', 'A'], ['b', 'B'], ['c', 'C'], ['d', 'D']])
print(df2)

print("传入一个嵌套列表，里面是元组：")
df2 = pd.DataFrame([('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')])
print(df2)

print("指定行列索引：")
df3 = pd.DataFrame([['a', 'A'], ['b', 'B'], ['c', 'C'], ['d', 'D']], columns=["小写", "大写"], index=["一", "二", "三", "四"])
print(df3)

print("传入字典：")
df4 = pd.DataFrame({"小写": ["a", "b", "c", "d"], "大写": ["A", "B", "C", "D"]}, index=["一", "二", "三", "四"])
print(df4)

# columns 获取DataFrame的列
print("获取DataFrame的列：")
print(df2.columns)
print(df3.columns)

# index 获取DataFrame的行
print("获取DataFrame的行：")
print(df2.index)
print(df3.index)

# 获取 DataFrame的值 后续再讲

print("-" * 30 + "End Section 2 DataFrame" + "-" * 30)
print('\n')
