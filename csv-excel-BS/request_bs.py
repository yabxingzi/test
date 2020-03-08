import requests
from bs4 import BeautifulSoup
#引入requests和bs

url='https://www.zhihu.com/people/zhang-jia-wei/posts?page=1'
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
#使用headers是一种默认的习惯，默认你已经掌握啦~
res=requests.get(url,headers=headers)
#用resquest模块发起请求，将响应的结果赋值给变量res。
print(res.status_code)
#检查状态码
bstitle=BeautifulSoup(res.text,'html.parser')
#用bs进行解析
content=bstitle.findAll(class_='ContentItem-title')
#提取我们想要的标签和里面的内容
print(len(content))
print(content[1].text)
#打印title