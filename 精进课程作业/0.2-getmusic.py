import requests

# 获取数据
url = 'https://static.pandateacher.com/Over The Rainbow.mp3'
res = requests.get(url)
music = res.content

# 存储数据
with open(r'精进课程作业\music.mp3', 'wb') as music_file:
    music_file.write(music)
print('下载音乐成功')