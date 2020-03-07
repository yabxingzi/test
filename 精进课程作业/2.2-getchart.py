# 题⽬要求：你需要爬取的是⽹上书店(http://books.toscrape.com/)中所有书的分类类型，并
# 且将它们打印出来。⽹⻚URL:http://books.toscrape.com/
import requests
from bs4 import BeautifulSoup
# 获取数据
url = 'http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html'

res = requests.get(url)
# 解析数据（转换格式）
bs = BeautifulSoup(res.text,'html.parser')
# 提取数据
# 查找数据 find的类型是Tag型，find_all是ResultSet型是Tag的列表型
# print(type(bs.find('ul', class_='nav')))
# print(type(bs.find_all('ul', class_='nav')))
list_kind = bs.find('ul', class_='nav').find('ul').find_all('li')
# 提取有用数据
for kind in list_kind:
    # strip()去掉多余字符\n 空格
    print(kind.text.strip())
