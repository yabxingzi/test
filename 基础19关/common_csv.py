import sys
sys.path.append(r'D:\GitHub\test')
import lib.common
import csv


class csvop(lib.common.common):     # 多层目录继承方式

    header = ['None']
    file_path = ''
    dict = {}
    # content = []
    room = 0
    info = []

    def header_csv(self):
        self.file_path = self.save_file()   # 调用父类的函数需要加self
        with open(self.file_path, 'a', newline='') as csvfile:
            self.writer = csv.writer(csvfile, dialect='excel')
            self.writer.writerow(self.header)

    def content_csv(self, content):
        dire = ['', '南北', '东西']
        if '' != self.file_path:
            with open(self.file_path, 'a', newline='')as csvfile:
                writer = csv.writer(csvfile, dialect='excel')
                # 二级字典{1:{101:[1,100], 102:[1, 100]}, 2:{202:[1,140]}}转列形
                for sub_dict in self.dict.values():
                    for self.room, self.info in sub_dict.items():
                        content.append(self.room)
                        content.append(dire[self.info[0]])
                        content.append(self.info[1])
                        writer.writerow(content)
                        for i in range(3):
                            content.pop()


        else:
            pass


if __name__ == '__main__':
    csvop = csvop()
    # 添加表头
    csvop.header = ['小区名称', '地址', '建筑年份', '楼栋', '单元', '户室', '朝向', '面积']
    csvop.header_csv()
    # 填充内容
    csvop.dict = {1:{101:[1, 80], 102:[1, 80]},
                  2:{201:[1, 70], 202:[1, 70]}
                 }

    title = '江临天下'
    address = '湖北宜昌'
    year = '2010'
    block = '1'
    unit = '1'
    content = [title, address, year, block, unit]
    csvop.content_csv(content)
