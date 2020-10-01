#!/usr/bin/python3
# print("hello world")
import keyword

# py保留字
# kwlist = keyword.kwlist
# print(kwlist)

# 第一个注释
# 第二个注释

'''
第三注释
第四注释
'''

"""
第五注释
第六注释
"""

# 行与缩进
# python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {}
# 缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。实例如下：
if True:
    print("True")
else:
    print("false")

if True:
    print("Answer")
    print("True")
else:
    print("Answer")
print("False")  # 缩进不一致，会导致运行错误

# 多行语句
total = 'item_one' + \
        'item_two' + \
        'item_three'
print(total)
# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)，例如
total2 = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
print(total2)


