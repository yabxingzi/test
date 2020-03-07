# encoding:utf-8
import requests 

# client_id 为官网获取的AK， client_secret 为官网获取的SK
AK='I5cziBig8fOLWUdUmOt7Hfjr'
SK='D8pwGGnFcVxC5QvGQkB8gB39wBODdsyP'
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(AK,SK)
response = requests.get(host)
if response:
    print(response.json())