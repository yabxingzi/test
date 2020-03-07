import requests
# 获取数据
url = 'https://res.pandateacher.com/2019-01-12-15-29-33.png'
res = requests.get(url)
# 以二进制数据的形式返回
pic = res.content
# 存储数据
# 新建一个文件，图片内容以二进制wb只写
with open(r'精进课程作业\spider.jpg', 'wb') as photo:
    photo.write(pic)
print('下载图片成功！')
