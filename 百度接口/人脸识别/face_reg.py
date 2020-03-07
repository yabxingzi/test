import sys
sys.path.append(r'D:\GitHub\test')
import lib.common as com
import base64
from aip import AipFace

APP_ID = '18710688'
API_KEY = '	I5cziBig8fOLWUdUmOt7Hfjr'
SECRET_KEY = 'D8pwGGnFcVxC5QvGQkB8gB39wBODdsyP'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

def face_check(img_data):
    """
    人脸识别demo
    :param img_data: 二进制的图片数据
    :return:
    """
    data = base64.b64encode(img_data)
    image = data.decode()
    imageType = "BASE64"
    groupId = 'group_test'
    userId = 'YanAoBo'
    """ 调用人脸注册 """
    client.addUser(image, imageType, groupId, userId)
    """ 如果有可选参数 """
    options = {}
    options["user_info"] = "user's info"
    options["quality_control"] = "NORMAL"
    options["liveness_control"] = "LOW"
    options["action_type"] = "REPLACE"

    """ 带参数调用人脸注册 """
    res = client.addUser(image, imageType, groupId, userId, options)
    print(res)
    try:
        res_list = res['result']
    except Exception as e:
        res_list = None

    return res_list

if __name__ == "__main__":
    read = com.common()
    read_file_path = read.get_path()
    with open(read_file_path, "rb") as f:
        data = f.read()

    res = face_check(data)
    print(res)