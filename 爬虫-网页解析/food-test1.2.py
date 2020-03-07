import requests
# 引用requests库
from bs4 import BeautifulSoup
# 引用BeautifulSoup库

res_foods = requests.get('https://www.meishij.net/chufang/diy/')
# 获取数据
bs_foods = BeautifulSoup(res_foods.text,'html.parser')
# 解析数据
list_foods = bs_foods.find_all('div',class_='i_w')
# 查找最小父级标签
print(len(list_foods))
list_all = []
# for food in list_foods:
#     tag_a = food.find('div',class_='c1')
#     name = tag_a.find('strong')
#     star = tag_a.find('span')
#     author = tag_a.find('em')
#     list_all.append([name.text, star.text[:1], author.text])
# print(list_all)

for x in range(len(list_foods)):
    food = [list_foods[x].find('strong').text, list_foods[x].find('span').text[:1]]
    list_all.append(food)

print(list_all)
