# encoding:utf-8
import sys
sys.path.append(r'D:\GitHub\test')
import lib.common as com
import requests
import base64

object_ = 'plant'

if object_ == 'animal':
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/animal"
elif object_ == 'plant':
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/plant"
else:
    print('object_error')
# 二进制方式打开图片文件
local = 1
if local == 1:  # 来自于本地
    read = com.common()
    read_file_path = read.get_path()
    f = open(read_file_path, 'rb')
    img = base64.b64encode(f.read())
else:
    image_url ='https://note.youdao.com/yws/api/personal/file/9436028FDBEC4EADABCAA2F380625DB6?method=download&shareKey=15486e87e7f1af0f1791a8923821aa1f'
    f = requests.get(image_url).content
    img = base64.b64encode(f)
params = {"image": img}
access_token = '24.e6627b0bf316d4ef4ecb8a591dacdf73.2592000.1586099116.282335-18706711'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())