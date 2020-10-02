# Section0 开场
print("-" * 30 + "Begin Section 0 开场" + "-" * 30)
print("这是Python的第十三次课程,主要讲数据分组:")
print("1.数据分组\n2.数据透视表")
print("-" * 30 + "End Section 0 开场" + "-" * 30)
print('\n')

import pandas as pd

df = pd.read_excel(r"D:\pycharm2019\project\python_learn\files\lesson13\Lesson13.xlsx")
print(df)
# Section1 数据分组
# 用groupby(列名)

print("数据分组：")
print(df.groupby("客户分类"))

print("数据分组加上聚合函数count：")
# 根据客户分类分组，其他列count
print(df.groupby("客户分类").count())
print("数据分组加上聚合函数sum：")
print(df.groupby("客户分类").sum())

print("按照多列进行分组count：")
print(df.groupby(["客户分类", "区域"]).count())

print("按照多列进行分组sum：")
print(df.groupby(["客户分类", "区域"]).sum())

# 如果我们想要知道A,B,C类客户分别有多少
print("统计A、B、C类客户数量：")
print(df.groupby("客户分类")["用户ID"].count())

# aggregate函数
# 就是可以一次性输出多个聚合函数的结果
print("按照客户分类进行分组count,sum：")
print(df.groupby("客户分类").aggregate(["count", "sum"]))

print("按照客户分类进行分组，对用户ID列进行count，7月销量列进行sum，8月销量列进行sum")
print(df.groupby("客户分类").aggregate({"用户ID": "count", "7月销量": "sum", "8月销量": "sum"}))

# 对分组之后的数据重制索引,转换成标准的DataFrame类型   从DataFrameGroupBy 转成DataFrame
print("重置索引：")
print(df.groupby("客户分类").sum().reset_index())

# Section2 数据透视表
# pivot_table(data,values=None,index = None,columns = None,aggfunc="mean",
# fill_value = None,margins = False,dropna = True,margins_name = "All")
# data:整张表
# value：透视表的数据
# index:行索引
# columns：列索引
# aggfunc:聚合函数
# fill_value:对空值的填充值
# margins:表示是否显示合计列
# dropna:是否删除缺失，如果为true，就会删除有缺失值的行
# margins_name:合计列的列名

print("统计各个区域的各种客户类型7月销量：")
print(pd.pivot_table(df, values="7月销量", index="客户分类", columns="区域", aggfunc="sum"))

print("增加合计列：")
print(pd.pivot_table(df, values="7月销量", index="客户分类", columns="区域", aggfunc="sum", margins=True))

print("重命名合计列为总和：")
print(pd.pivot_table(df, values="7月销量", index="客户分类", columns="区域", aggfunc="sum", margins=True, margins_name="总和"))

print("将缺失值设为0：")
print(pd.pivot_table(df, values="7月销量", index="客户分类", columns="区域", aggfunc="sum", margins=True, margins_name="总和",
                     fill_value=0))

print("有多种values：")
print(pd.pivot_table(df, values=["7月销量", "8月销量", "9月销量"], index="客户分类", columns="区域", aggfunc={"7月销量": "sum",
                                                                                               "8月销量": "sum",
                                                                                               "9月销量": "sum"},
                     margins=True, margins_name="总和", fill_value=0))

print("重置索引：")
print(pd.pivot_table(df, values=["7月销量", "8月销量", "9月销量"], index="客户分类", columns="区域", aggfunc={"7月销量": "sum",
                                                                                               "8月销量": "sum",
                                                                                               "9月销量": "sum"},
                     margins=True, margins_name="总和", fill_value=0).reset_index())
