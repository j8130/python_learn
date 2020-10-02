# Section0 开场
print("-" * 30 + "Begin Section 0 开场" + "-" * 30)
print("这是Python的第二次课程,内容主要包括:")
print("1.运算符\n2.循环语句\n3.条件语句\n4.函数\n5.模块")
print("-" * 30 + "End Section 0 开场" + "-" * 30)
print('\n')

# Section1 运算符
print("-" * 30 + "Begin Section 1 运算符" + "-" * 30)
# 运算符分算术运算符、比较运算符、逻辑运算符
print("算术运算符：")
print("10 + 20 = ", 10 + 20)
print("10 - 20 = ", 10 - 20)
print("10 * 20 = ", 10 * 20)
# 返回的是结果，如果是小数则返回小数
print("10 / 20 = ", 10 / 20)
print("10 % 20 = ", 10 % 20)
# 返回x的y次幂
print("10 ** 20 = ", 10 ** 20)
# 返回两数相除之后商的整数部分
print(" 10 // 20 = ", 10 // 20)
print("比较运算符：")
# 比较运算符就是大于、小于、等于之类的
print("10 == 20", 10 == 20)
print("10 != 20", 10 != 20)
print("10 > 20", 10 > 20)
print("10 < 20", 10 < 20)
print("10 >= 20", 10 >= 20)
print("10 <= 20", 10 <= 20)
print("逻辑运算符：")
# 就是与、或、非
print("(10 > 20) and (10 < 20)", (10 > 20) and (10 < 20))
print("(10 > 20) or (10 < 20)", (10 > 20) or (10 < 20))
print("not(10 > 20)", not (10 > 20))
print("-" * 30 + "End Section 1 运算符" + "-" * 30)
print("\n")

# Section2 循环语句
print("-" * 30 + "Begin Section 2 循环语句" + "-" * 30)
# For循环
# 1.for xxx in xxxx:
# 2.for里面的语句必须要有空格
# 成为数据分析师要学习下面四门功课
print("For循环：")
subjects = ["Excel", "SQL", "Python", "统计学"]
for sub in subjects:
    print("小飞目前正在学习：{}".format(sub))

# While循环
# 1.While condition :
# 		statement
# 2.当条件满足的时候，就继续执行；当条件不满足的时候，跳出循环
# 和小飞成为好朋友，必须要给小飞点10个赞
likeNum = 0;
while likeNum < 10:
    print("我和小飞还不是好朋友，因为我还只点了{}个赞".format(likeNum))
    likeNum += 1
print("我和小飞已经是好朋友了，因为我已经点了{}个赞".format(likeNum))
print("-" * 30 + "End Section 2 循环语句" + "-" * 30)
print("\n")

# Section3 条件语句
print("-" * 30 + "Begin Section 3 条件语句" + "-" * 30)
# If语句
# 1.if部分是必须的，elif语句可以没有，else如果有则必须放在最后面;
# 2.可以有多个elif，但只能有一个if 和 else
body_temperature = 78
if body_temperature > 42:
    print("此人体温超42度，请密切监控")
elif body_temperature > 38:
    print("此人体温超38度未超42度，请注意监控")
elif body_temperature > 37:
    print("此人体温超37度未超38,也需要监控")
else:
    print("此人体温正常，可以解封")
print("-" * 30 + "End Section 3 条件语句" + "-" * 30)
print("\n")

# Section4 函数
print("-" * 30 + "Begin Section 4 函数" + "-" * 30)


# 函数是在一个程序中可以被重复使用的一段程序
# 由函数名(必需)、参数、语句块(必需)、return,变量这几部分组成
# def 函数名(参数):
# 	  语句块
# 定义关键词是 def 
# 无返回值的函数
def learn_python(location):
    print("我正在{}上学Python".format(location))


learn_python("地铁")
learn_python("公交车")
learn_python("出租车")


# 有返回值的函数
def learn_python_with(location):
    doing = "我正在{}上学Python".format(location)
    return doing


ret = learn_python_with("飞机")
print(ret)


# 定义含有多个参数的函数
def learn_python_mul(location, people):
    doing = "我正在{}上学Python,人{}".format(location, people)
    return doing


ret = learn_python_mul("自行车", "只有我一个")
print(ret)
print("-" * 30 + "End Section 4 函数" + "-" * 30)
print("\n")

# Section5 模块
print("-" * 30 + "Begin Section 5 模块" + "-" * 30)
# 如果要使用函数，必须要在同一个文件中有相应的函数定义
# 但是如果把所有的代码都写在同一个文件中，这个文件会很大并且不容维护
# 所以会把一些功能相近的函数，抽成一个模块，然后通过import引进
# 例如我们接下来要学习Pandas,就是一个模块
import pandas as pd

S1 = pd.Series(['a', 'b', 'c', 'd'])
print(S1)
print("-" * 30 + "End Section 5 模块" + "-" * 30)
print("\n")
