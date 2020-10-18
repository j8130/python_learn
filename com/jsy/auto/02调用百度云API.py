# encoding:utf-8

import base64

import requests

ak = ""
sk = ""
# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + ak + '&client_secret=' + sk
response = requests.get(host)
if response:
    print(response.json())

# json_loads = json.loads(response.json())
token = response.json().get('access_token')

print("token is" + token)
'''
通用文字识别
'''

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
# 二进制方式打开图片文件
f = open('E:\\11.png', 'rb')
img = base64.b64encode(f.read())

params = {"image": img}
access_token = token
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print(response.json())
