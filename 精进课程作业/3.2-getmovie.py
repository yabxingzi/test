# 爬取电影链接并批量下载
# 步骤分析：输入名字-查搜索结果-进入下载页面-找到下载链接
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote


# 获取数据（爬取网页数据）
# 输入电影名
# movietitle = input('请输入下载的电影名：')
movietitle = '无名之辈'
gbkmovietitle = movietitle.encode('gbk')
urlmovietitle = quote(gbkmovietitle)
# 进入下载页面
url = 'http://s.ygdy8.com/plus/s0.php?typeid=1&keyword='+str(urlmovietitle)
res = requests.get(url)
bs = BeautifulSoup(res.text, 'html.parser')
href_part = bs.find_all('table')[1].find('a')['href']
if href_part:   # 有些没有电影要做判断
    prehref = 'https://www.ygdy8.com'+href_part
    # 找到下载链接
    # 获取数据
    res_download = requests.get(prehref)
    # 确定网页编码格式
    res_download.encoding = 'gbk'
    # 解析数据
    bs_download = BeautifulSoup(res_download.text, 'html.parser')
    # 提取数据
    url_download = bs_download.find('div', id='Zoom').find('span').find('table').find('a')['href']
    print(url_download)
else:
    print('没有'+movietitle)
