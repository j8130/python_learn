# 爬取有道查单词
from bs4 import BeautifulSoup
import requests

word = "word"
url = "https://fanyi.baidu.com/?aldtype=16047#en/zh/" + word

# 整个网页的代码
webData = requests.get(url).text
# print(text)

# 对webData进行解析
soup = BeautifulSoup(webData, "lxml")

# 网页上右键copy selector
# [0].get_text 是获取标签里的内容
select = soup.select("#left-result-container > div > div > div.output-bd.clearfix > div.dictionary-output > div.dictionary-title > h3")

print(select)