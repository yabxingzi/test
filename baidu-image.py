import requests
from aip import AipOcr
import lib.common as com

com = com.common()
file = open(com.get_path(), 'rb')
image = file.read()
# image = requests.get('https://note.youdao.com/yws/api/personal/file/278D191C8E894BFC83A13DE0964D02EE?method=download&shareKey=52048bdc2247d7e4593eb075fff73260').content


APP_ID = '16149264'
API_KEY = 'yxYg9r4OuAs4fYvfcl8tqCYd'
SECRET_KEY = 'yWg3KMds2muFsWs7MBSSFcgMQl8Wng4s'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
res = client.basicGeneral(image)
for item in res['words_result']:
    print(item['words'])
