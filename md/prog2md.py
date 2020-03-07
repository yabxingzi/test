import sys
sys.path.append(r'D:\GitHub\test')
import lib.common as com

read = com.common()
write = com.common()
read_file_path = read.get_path()
write_file_path = write.save_file()

with open(read_file_path, 'r', encoding='utf-8') as file:
    with open(write_file_path, 'w', encoding='utf-8') as save_file:
        lines = file.readlines()
        save_file.write('# 代码\n```C++\n')
        for line in lines[2:10]:
            save_file.write(line)

        save_file.write('```')


