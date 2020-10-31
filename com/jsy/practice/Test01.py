from easygui import buttonbox, msgbox  # 导入easygui中的buttonbox,msgbox
import datetime  # 导入datetime
from random import choice  # 从random导入choice


def bs():  # 定义一个报时函数
    end = datetime.datetime.strptime('16:30:0', '%H:%M:%S')  # 下班时间
    now = datetime.datetime.today()  # 现在时间
    delta = end - now  # 用delta存储两个时间的时间差   下班时间-现在时间

    hour = int(delta.seconds / 60 / 60)  # 小时数，秒/60/60
    minute = int((delta.seconds - hour * 60 * 60) / 60)  # 分钟数，总-60*60*小时/60
    second = int(delta.seconds - hour * 60 * 60 - minute * 60)  # 秒数

    hour_str = '距离下班还有:' + str(hour) + '小时' + str(minute) + '分' + str(second) + '秒'
    minute_str = '距离下班还有:' + str(minute + 60 * hour) + '分' + str(second) + '秒'
    second_str = '距离下班还有:' + str(second + minute * 60 + 60 * hour * 60) + '秒'

    return hour_str, minute_str, second_str  # 返回小时，分钟，秒


coms = ['中国人的喜酒，今世缘为您报时：',
        '中国高端中度白酒，国源为您报时：',
        '茅台王子酒，为您报时：',
        '迎驾贡酒，为您报时：',
        '蓝色经典，梦之蓝为您报时：',
        '茅台集团，习酒为您报时：',
        '成功汽车，为您报时：',
        '郎酒红花郎，为您报时：',
        '郎牌特曲，为您报时：',
        '茅台集团，为您报时：']  # 报时公司列表

time_str = bs()

hour_str = time_str[0]  # 第0个，小时
minute_str = time_str[1]  # 第1个，分钟
second_str = time_str[2]  # 第2个，秒

com = choice(coms)  # 随机从列表中选择一个报时公司
cs = buttonbox(msg=com + '\n' + hour_str + '\n' + minute_str + '\n' + second_str, title="第1次为您报时",
               choices=("知道啦，退下吧！", "再次报时！"))
# 用buttonbox来进行选择

if cs == "知道啦，退下吧！":  # 如果知道了就结束
    pass
num = 2  # 第2次
while cs == "再次报时！":
    time_str = bs()
    hour_str = time_str[0]
    minute_str = time_str[1]
    second_str = time_str[2]
    cs = buttonbox(msg=com + '\n' + hour_str + '\n' + minute_str + '\n' + second_str, title="第" + str(num) + "次为您报时",
                   choices=("知道啦，退下吧！", "再次报时！"))
    num += 1  # +1

end = datetime.datetime.strptime('16:30:0', '%H:%M:%S')
now = datetime.datetime.today()

while now == end:
    msgbox("千万别忘了打卡！", title="重要提醒", ok_button="知道啦")  # 提醒打卡！