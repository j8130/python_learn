# Section 0 开场
print("-" * 30 + "Begin Section 0 开场" + "-" * 30)
print("大家好，我是小飞！！！\n我今天主要讲一些Python的基础知识，分下面几大部分：")
print("1.数\n2.变量\n3.字符串\n4.列表\n5.字典\n6.元组")
print("每一个部分我都通过代码实例来讲解，大家可以更加加深理解")
print("看完之后大家可以照着我的代码，重新敲一边。因为写代码还是需要培养自己的代码感觉的")
print("-" * 30 + "End Section 0 开场" + "-" * 30)
print("\n")

# Section 1 数
print("-" * 30 + "Begin Section 1 数" + "-" * 30)
# 6是整数,符号是int
6
# 1.6是浮点数,就是数学中带小数的数字,符号是float
1.6
print("用type函数可以得到对应的类型")
print("6是", type(6));
print("1.6是", type(1.6))
print("-" * 30 + "End Section 1 数" + "-" * 30)
print("\n")

# Section 2 变量
print("-" * 30 + "Begin Section 2 变量" + "-" * 30)
# variable是变量,里面存着1
variable = 1
print("variable是变量,现在里面存放着", variable)
print("***variable现在重新赋值***")
# 因为variable是变量，所以可以重新赋值
variable = 2
print("variable是变量,现在里面改变为", variable)
# 变量命名必须以字母或者_开始
_variable = 3
# 变量是区分大小写的
Variable = 4
print("Python区分大小写，variable 和 Variable的值分别为", variable, Variable)
# 有些是python保留的名字，例如if，你就不能将变量名取为if
print("-" * 30 + "End Section 2 变量" + "-" * 30)
print("\n")

# Section 3 字符串
print("-" * 30 + "Begin Section 3 字符串" + "-" * 30)
# 字符串是由零个或多个字符组成的，用单引号或者双引号括起来的
# 强烈建议零个或者只有一个字符的时候，用单引号
# 有超过一个字符的时候，用双引号
# 符号是str
print('a是', type('a'));
print("程序员小飞是", type("程序员小飞"))
print('空字符串也是', type(''))
# 字符串拼接
print("程序员" + "小飞")
# 字符串复制
print("程序员小飞" * 3)
# 获取字符串长度,用len()函数
print("程序员小飞一共", len("程序员小飞"), "个字")
# 字符串查找，查找A字符串是否在B字符串中，用in
print("小飞是在程序员小飞里面吗？", "小飞" in "程序员小飞")
print("小张飞是在程序员小飞里面吗？", "小张飞" in "程序员小飞")
# 除了in，还有not in
print("小张飞不在程序员小飞里面吗？", "小张飞" not in "程序员小飞")
# find函数查找某一字符是否在字符串里面，找到返回其位置，找不到返回-1
print("小飞在程序员小飞的哪个位置", "程序员小飞".find("小飞"))
print("小张飞在程序员小飞的哪个位置", "程序员小飞".find("小张飞"))
# 字符的索引，就是指字符在字符串的位置，注意第一个是从0开始的
tmp = "程序员小飞"
print("程序员小飞索引为0的字符串为", tmp[0])
# 字符串分隔，split函数
# 以逗号为分隔符，将程序员,小飞分开
print("程序员,小飞".split(','))
print("-" * 30 + "End Section 3 字符串" + "-" * 30)
print("\n")

print("-" * 30 + "Begin Section 4 列表" + "-" * 30)
# 列表就是用[]表示的一组有序数据，每个数据之间用逗号隔开
# 创建之后可以增加或者删除数据
# 其中数据类型可以是不一样的
# 新建一个空列表
null_list = []
print("这是一个空列表", null_list)
# 或者里面全部是数类型的列表
num_list = [1, 2.1, 3]
print("这是数据类型都是数类型的列表", num_list)
# 或者里面是str类型的列表
str_list = ["2", "2", "3"]
print("这是数据类型是字符串的列表", str_list)
# 或者里面的不同类型的列表
kinds_list = ["1", 2.1, 3]
print("这是数据类型不同的列表", kinds_list)
# 列表的复制
print("将num_list复制两份", num_list * 2)
# 列表的合并
print("将num_list和str_list合并", num_list + str_list)
# 向列表插入新元素,会直接改变原列表
# 往列表末尾插入4
num_list.append(4)
print("往num_list末尾插入4", num_list)
# 往列表第4位插入5
num_list.insert(3, 5)
print("往num_list第4位插入5", num_list)
# 获取列表中值出现的次数
print("str_list中字符2出现了", str_list.count('2'), '次')
# 获取值在列表的位置
print("str_list中字符第一个2出现在位置", str_list.index('2'))
# 获取列表中指定位置的值
print("kinds_list中第一个的值为", kinds_list[0])
# 获取一定的位置范围的值,切片索引包括前面的，不包括后面的
print("kinds_list中第一个到第二个的值分别为", kinds_list[0:2])
# 删除列表中的值
# pop根据位置删除，删除第3个
num_list.pop(2);
print("将num_list中第3个删除", num_list)
# remove按值删除，删除值1
num_list.remove(1)
print("将num_list中的5删除", num_list)
# 对列表进行排序，默认是升序
num_list.sort()
print("将num_list升序排列", num_list)
print("-" * 30 + "End Section 4 列表" + "-" * 30)
print('\n')

print("-" * 30 + "Begin Section 5 字典" + "-" * 30)
# 字典是一种键值对的结构，类似于通过联系人姓名找到他的手机号码
# 是以{key1:value1,key2:value2}方式表示
# 键(key)必须是唯一的，但是值(value)可以重复
# 新建一个空字典
test_dict = {}
# 往字典插入新值
test_dict["小飞"] = 18868504913
test_dict["小王"] = 17967297533
print("新建了一个字典", test_dict)
# keys()方法用来获取字典内所有的键
print("新建的字典中所有的键为", test_dict.keys())
# values()方法用来获取字典内所有的值
print("新建的字典中所有的值为", test_dict.values())
# items()方法用来获取字典内一组组的键值对
print("新建的字典中所有的键值对为", test_dict.items())
print("-" * 30 + "End Section 5 字典" + "-" * 30)
print('\n')

print("-" * 30 + "Begin Section 6 元组" + "-" * 30)
# 元组和列表和相似，但是还有两点不同
# 元组的元素不能改变，但是列表能够改变
# 元组是用小括号()表示，但是列表是[]表示
# 新建一个元组
tup = (1, 2, 3, 4, 5)
print("新建了一个元组", tup)
# 获取元组的长度
print("元组的长度为", len(tup))
# 获取元组内的元素
print("元组的第三个元素是", tup[2])
# 获取元组内一段范围的元素
print("元组的第二到第三个元素是", tup[1:3])
# 元组和列表的互换
# 用list()将元组转换为列表
print("将元组转换为列表", list(tup))
# 用tuple()将列表转换为元组
li = [1, 2, 3, 4, 5]
print("将列表转换为元组", tuple(li))
