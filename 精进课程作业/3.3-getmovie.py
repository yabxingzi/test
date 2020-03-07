# 批量下载V电影网站的视频 
from bs4 import BeautifulSoup
import requests

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
    # 标记了请求从什么设备，什么浏览器上发出
    }

# 获取数据
# 获取下载页面的网页以及评分
url = 'https://www.vmovier.com/channel/cut/new' # 初始网页
init_page = 2
end_page = 5
for page in range(init_page, end_page):   # 爬取2页内容
    res = requests.get(url)
    # res.encoding = 'gbk' # 不需要
    # 解析数据
    bs = BeautifulSoup(res.text, 'html.parser')
    # 提取数据
    list_info = bs.find('ul', id='post-list').find_all('li')
    for info in list_info[0:]:
        # 获取下载页面的网页链接
        herf_part = info.find('a')['href']
        # 获取评分
        star = info.find('div', class_='works-text').find('div', class_='works-ope').find('div', class_='rating')['data-score']
        # 获取电影标题
        name = info.find('a')['title']
        # print("{}  {}".format(herf_part, star))
        # 获取下载网页的地址
        pre_url = 'https://www.vmovier.com' + herf_part
        # print(pre_url)
        # 获取下载网页的数据
        res_pre = requests.get(pre_url, headers=headers)
        # # 解析数据
        bs_pre = BeautifulSoup(res_pre.text, 'html.parser')
        # 提取数据
        if len(bs_pre.find('body').find_all('script')) >= 11:
            pre_info = bs_pre.find('body').find_all('script')[11].text
            pre_info_num = pre_info.index('vid')
            # 找到下载网址存储网址，该网址为json格式
            herf_part_ = pre_info[(pre_info_num + 6):(pre_info_num + 19)]
            herf_ ='https://openapi-vtom.vmovier.com/v3/video/'+herf_part_+'?expand=resource&usage=xpc_web'
            res_ = requests.get(herf_, headers=headers)
            res_json = res_.json()
            # 获取有效下载链接地址
            herf_download = res_json['data']['resource']['default']['url']
            res_movie = requests.get(herf_download)
            movie = res_movie.content
            # 下载电影
            with open('movie-test\{}.mp4'.format(name), 'wb') as movie_file:
                movie_file.write(movie)
    # 进度打印
    print("{}of{}".format(page, end_page))
    # 翻页
    url ='https://www.vmovier.com/channel/cut/new/p/'+str(page)
print("successful!")

