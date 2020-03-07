import sys
sys.path.append(r'D:\GitHub\test')
import lib.common as com
import requests
import base64

'''
通用文字识别
'''
requests_ = "高精度"

if requests_ == "高精度含位置":
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate"
elif requests_ == "高精度":
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
else:
    print("request_error")
# 二进制方式打开图片文件
read = com.common()
read_file_path = read.get_path()
f = open(read_file_path, 'rb')
img = base64.b64encode(f.read())

params = {"image": img}
access_token = '24.84dc180d60c52a0b93bdaf390beb68c3.2592000.1586101739.282335-18707117'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())