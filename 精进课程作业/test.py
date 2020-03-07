from urllib.parse import quote
a = '无名之辈'
# 将汉字，用GBK格式编码
b = a.encode('gbk')
print(quote(b))
