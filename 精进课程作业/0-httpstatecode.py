import requests


url = 'https://localprod.pandateacher.com/python-manuscript/crawler-html/exercise/HTTP响应状态码.md'
res = requests.get(url)
print(res.status_code)
context = res.text
print(context)

