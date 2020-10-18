# 网站 http://www.buchang.com/zbt1jl/bbs/reg.asp?action=apply
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from PIL import Image
import base64
import requests


driver = webdriver.PhantomJS(executable_path="D:\\develop\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
driver.get("http://www.buchang.com/zbt1jl/bbs/reg.asp?action=apply")
time.sleep(3)

# 有反爬机制，所以找上层,然后去里面找
driver.find_element_by_id('theForm').find_elements_by_tag_name('input')[0].send_keys("carter00")

driver.save_screenshot('luntan1.png')

# 验证码需要点击一下输入框才可以显示出来,发一个空值让光标进到输入框
driver.find_element_by_id('codestr').send_keys('')
time.sleep(2)
driver.save_screenshot('verify_code.png')

# 百度识别验证码
# 1. 定位图片  先定位左上角  然后加长宽
verify_code_element = driver.find_element_by_id('imgid')
left = int(verify_code_element.location['x']-0)
top = int(verify_code_element.location['y']-10)
right = int(verify_code_element.location['x'] + 64)
bottom = int(verify_code_element.location['y'] + 30)

im = Image.open('verify_code.png')
im = im.crop((left, top, right, bottom))
im.save('verify_code2.png')








# # 手工输入验证码
# verify_code = input("手工输入验证码：")
# driver.find_element_by_id('codestr').send_keys(verify_code)
# driver.save_screenshot('luntan3.png')
#
#
# driver.find_element_by_id('theForm').find_elements_by_tag_name('input')[4].send_keys("123jia")
# driver.find_element_by_id('theForm').find_elements_by_tag_name('input')[5].send_keys("123jia")
# driver.find_element_by_id('theForm').find_elements_by_tag_name('input')[6].send_keys("123456@qq.com")
# driver.save_screenshot('luntan4.png')
#
# # 提交
# driver.find_element_by_id('bt_save').click()
#
# time.sleep(3)
# driver.save_screenshot('luntan5.png')


def verify_security_code(n):
    driver.refresh()
    driver.find_element_by_id('codestr').send_keys('')
    time.sleep(1)
    driver.save_screenshot('verify_code.png')

    # 找图片
    verify_code_element = driver.find_element_by_id('imgid')
    left = int(verify_code_element.location['x'] - 0)
    top = int(verify_code_element.location['y'] - 10)
    right = int(verify_code_element.location['x'] + 64)
    bottom = int(verify_code_element.location['y'] + 30)

    im = Image.open('verify_code.png')
    im = im.crop((left, top, right, bottom))
    im.save('verify_code2.png')

    def get_verfy_code():
        ak = "893hWMYo8P1GxPTPpefSs5KO"
        sk = "GXZ2Py1ZXuL0eGamXNvE4cHiC4lkvOeO"
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
        f = open('D:\\pycharm2019\\project\\python_learn\\com\\jsy\\auto\\verify_code2.png', 'rb')
        # 使用base64 把文字或图片转成base64
        img = base64.b64encode(f.read())

        params = {"image": img}
        access_token = token
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            print(response.json())
            words_result = response.json().get('words_result')
            try:
                for i in words_result:
                    return i["words"]
            except :
                return 'error'

    verfy_code = get_verfy_code()
    driver.find_element_by_id('codestr').clear()
    driver.find_element_by_id('codestr').send_keys(verfy_code)
    driver.find_element_by_id('codestr').send_keys(Keys.TAB)
    driver.save_screenshot('test'+str(n)+'.png')
    n+=1

    right_url="skins/Default/note_ok.gif"
    now_url=driver.find_element_by_id('isok_codestr').find_element_by_tag_name('img').get_attribute('src')
    if now_url == right_url:
        driver.save_screenshot('ok.png')
    else:
        print('error'+n)
        verify_security_code(n)

verify_security_code(0)