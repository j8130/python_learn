# Section0 开场
print("-" * 30 + "Begin Section 0 开场" + "-" * 30)
print("这是Python的第十五次课程,主要讲结果导出:")
print("1.导出为.xlsx文件\n2.导出为.csv文件\n")
print("-" * 30 + "End Section 0 开场" + "-" * 30)
print('\n')

import pandas as pd

filePath = r"D:\pycharm2019\project\python_learn\files\lesson15\Lesson15.xlsx"
df1 = pd.read_excel(filePath, sheet_name="Sheet1")
df2 = pd.read_excel(filePath, sheet_name="Sheet2")
print("df1:")
print(df1)
print("df2:")
print(df2)

df3 = pd.concat([df1, df2], ignore_index=True)
print("df3:")
print(df3)

# Section1 导出为.xlsx文件
# pip install xlsxwriter
resultPath = r"D:\pycharm2019\project\python_learn\files\lesson15\result.xlsx"

# 最简单的
# na_rep,设置缺失值，inf_rep，设置无穷值（类似于一个数除以0这样）    index = False 不导出行索引
# df3.to_excel(resultPath, sheet_name="汇总", index=False, na_rep=0, inf_rep=0)

# 导入到多张Sheet
writer = pd.ExcelWriter(resultPath, engine="xlsxwriter")

df3.to_excel(writer, sheet_name="班级汇总有索引")

df3.to_excel(writer, sheet_name="班级汇总无索引", index=False)
# 导出部分列
df3.to_excel(writer, sheet_name="只导出姓名列和成绩列", index=False, columns=["姓名", "成绩"])

writer.save()  # 实际保存操作

# Section2 导出为.csv文件
# 没有sheet_name 和 inf_rep
resultCSVPath = r"D:\pycharm2019\project\python_learn\files\lesson15\result.csv"
df3.to_csv(resultCSVPath, index=False, na_rep=0)
