import os
import time

# print(os.path.basename(r'D:\GitHub\test\baidu-image.py'))   # 返回文件名
# print(os.path.dirname(r'D:\GitHub\test\baidu-image.py'))    # 返回目录路径
# print(os.path.split(r'D:\GitHub\test\baidu-image.py'))      # 分割文件名与路径
# print(os.path.join('root', 'test', 'runoob.txt'))          # 将目录和文件名合成一个路径 ouput:root\test\runoob.txt


file = r'D:\GitHub\test\baidu-image.py' # 文件路径
 
# print(os.path.getatime(file))   # 输出最近访问时间
# print(os.path.getctime(file))   # 输出文件创建时间
# print(os.path.getmtime(file))   # 输出最近修改时间
# print(time.gmtime(os.path.getmtime(file)))  # 以struct_time形式输出最近修改时间
# print(os.path.getsize(file))   # 输出文件大小（字节为单位）
# print(os.path.abspath(file))   # 输出绝对路径
# print(os.path.normpath(file))  # 规范path字符串形式
print(os.path.splitext(file))   # ('D:\\GitHub\\test\\baidu-image', '.py')
print(os.path.splitunc(file))   # ('D:\\GitHub\\test\\baidu-image', '.py')

# list =[r'\root\abc', r'\root\abc\sss']
# print(os.path.commonprefix(list))
