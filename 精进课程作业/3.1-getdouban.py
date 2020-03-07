# 爬取豆瓣电影名、推荐语、评分
import requests, random, bs4

# 添加浏览器信息
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
    # 标记了请求从什么设备，什么浏览器上发出
    }
# 获取数据
for page in range(10):
    url = 'https://movie.douban.com/top250?start='+str(page*25)+'&filter='
    res = requests.get(url, headers=headers)
# 解析数据
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
# 提取数据
    list_movieinfo = bs.find('ol', class_='grid_view').find_all('li')
    for movie in list_movieinfo:
        # 序号
        num = movie.find('em', class_='')
        # 电影名
        title = movie.find('span', class_='title')
        # 评分
        star = movie.find('span', class_='rating_num')
        # 推荐语
        comment = movie.find('span', class_='inq')
        if comment != None:
            print('{}\n{}\n{}\n{}\n\n'.format(num.text, title.text, comment.text, star.text))
        else:
            print('{}\n{}\n{}\n\n'.format(num.text, title.text, star.text))


