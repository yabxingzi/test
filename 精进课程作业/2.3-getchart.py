# 题⽬要求：你需要爬取的是⽹上书店[Books to Scrape](http://books.toscrape.com/)Tra
# 这类书中，所有书的书名、评分、价格三种信息，并且打印提取到的信息。
# ⽹⻚URL:http://books.toscrape.com/catalogue/category/books/travel_2/index.html

import requests
from bs4 import BeautifulSoup
# 获取数据
url = 'http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html'

res = requests.get(url)
# 解析数据
bs = BeautifulSoup(res.text,'html.parser')
# 提取数据
list_bookinfo = bs.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
for bookinfo in list_bookinfo:
    # 书名
    booktitle = bookinfo.find('h3').find('a').text
    # price
    bookprice = bookinfo.find('div', class_='product_price').find('p', class_='price_color').text
    # star
    bookstar = bookinfo.find('article', class_='product_pod').find('p')['class'][1]
    print("{}  {}  {}".format(booktitle, bookprice[1:], bookstar))
