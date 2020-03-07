import requests


# 获取数据
url = 'https://user.guancha.cn/comment/cmt-list.json?codeId=446144&codeType=1&pageNo=1&order=1&ff=www'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
    # 标记了请求从什么设备，什么浏览器上发出
    }
res = requests.get(url, headers=headers)
# 解析数据
res_json = res.json() # json格式转化成list格式
list_items = res_json['items'] 

# 提取数据
for item in list_items:
    print(item['content'])
    print("")
    with open('test.txt', 'a', encoding='utf-8') as file:
        file.write(str(item['content']))

print("successful")  

