import csv
#引用csv模块。
csv_file = open(r'D:\GitHub\test\csv-excel\demo.csv', 'w+', newline='',encoding='utf-8')
#创建csv文件，我们要先调用open()函数，传入参数：文件名“demo.csv”、写入模式“w”、newline=''、encoding='utf-8'。
writer = csv.writer(csv_file)
# 用csv.writer()函数创建一个writer对象。

reader = csv.reader(csv_file)
print(reader)
for row in reader:
    print(row)

writer.writerow(['电影','豆瓣评分'])
#调用writer对象的writerow()方法，可以在csv文件里写入一行文字 “电影”和“豆瓣评分”。
writer.writerow(['银河护卫队','8.0'])
#在csv文件里写入一行文字 “银河护卫队”和“8.0”。
writer.writerow(['复仇者联盟','8.1'])
#在csv文件里写入一行文字 “复仇者联盟”和“8.1”。
csv_file.close()

csv_file = open(r'D:\GitHub\test\csv-excel\demo.csv', 'r+', newline='',encoding='utf-8')

reader = csv.reader(csv_file)
for row in reader:
    print(row)

csv_file.close()

