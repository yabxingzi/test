# 爬取所有类型书的书名、价格、星级
import requests
from bs4 import BeautifulSoup
# 获取数据
url = 'http://books.toscrape.com/catalogue/category/books_1/index.html' # 初始网站

for page in range(2, 10):
    res = requests.get(url)
    # 解析数据
    bs = BeautifulSoup(res.text, 'html.parser')
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
    url = 'http://books.toscrape.com/catalogue/category/books_1/page-'+str(page)+'.html'
