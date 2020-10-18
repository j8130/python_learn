# 原理是调用微信网页版api，所以前提是微信要支持登录网页版
# pip install itchat
# 由于idea显示二维码会乱，要用cmd窗口运行
# 放弃，微信网页版无法登录
import itchat

itchat.auto_login(enableCmdQR=True, hotReload=True)
friend = itchat.search_friends("")
print(friend)

itchat.send("hello~", toUserName=friend[0]["UserName"])
