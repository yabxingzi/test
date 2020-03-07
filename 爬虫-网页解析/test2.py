import requests # 调用requests库
from bs4 import BeautifulSoup # 调用BeautifulSoup库
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')# 返回一个Response对象，赋值给res
html = res.text# 把Response对象的内容以字符串的形式返回
soup = BeautifulSoup( html,'html.parser') # 把网页解析为BeautifulSoup对象
print(type(soup))
items = soup.find_all(class_='books') # 通过匹配标签和属性提取我们想要的数据
print(items) # 打印items
print(type(items)) #打印items的数据类型
