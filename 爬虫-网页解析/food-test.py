import requests
# 引用requests库
from bs4 import BeautifulSoup
# 引用BeautifulSoup库

res_foods = requests.get('https://www.meishij.net/chufang/diy/')
# 获取数据
bs_foods = BeautifulSoup(res_foods.text,'html.parser')
# 解析数据
print(type(res_foods.text))
print(type(bs_foods))
# 打印解析结果