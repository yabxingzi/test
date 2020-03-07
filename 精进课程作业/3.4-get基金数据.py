from bs4 import BeautifulSoup
from selenium import webdriver
import requests

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
    # 标记了请求从什么设备，什么浏览器上发出
    }

url = 'http://api.fund.eastmoney.com/f10/lsjz'

driver=webdriver.Firefox()
driver.maximize_window()

params = {
    'callback': 'jQuery18305005375759728037_1583587460049',
    'fundCode': '001595',
    'pageIndex': '1',
    'pageSize': '20',
    'startDate': '',
    'endDate': '',
    '_': '1583587988279',
    }
# 将参数封装为字典
'''
requests.get(url, parms=parmas) 效果,'?'为分割符号
http://api.fund.eastmoney.com/f10/lsjz?callback=jQuery18305005375759728037_1583587460049&fundCode=001595&pageIndex=1&pageSize=20&startDate=&endDate=&_=1583587988279
'''
driver.get(url, headers=headers, params=params)
data = driver.page_source
soup = BeautifulSoup(data, 'lxml')
grades = soup.find_all('tr')
for grade in grades:
    if '<td>' in str(grade):
        print(grade.get_text())


