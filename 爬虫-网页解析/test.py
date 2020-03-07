import requests
from bs4 import BeautifulSoup
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html') 
soup = BeautifulSoup(res.text,'html.parser')
print(type(soup))   # 查看soup的类型
print(soup)         # 打印soup
