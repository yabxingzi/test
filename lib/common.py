import tkinter.filedialog
from tkinter import *
import os


class common:
    def get_path(self):
        root = tkinter.Tk()    # 创建一个Tkinter.Tk()实例
        root.withdraw()       # 将Tkinter.Tk()实例隐藏
        default_dir = r"文件路径"
        file_path = tkinter.filedialog.askopenfilename(title='打开文件', initialdir=(os.path.expanduser(default_dir)))
        print(file_path)

        return file_path

    def select_dir(self):
        root = tkinter.Tk()    # 创建一个Tkinter.Tk()实例
        root.withdraw()       # 将Tkinter.Tk()实例隐藏
        default_dir = r"文件路径"
        file_path = tkinter.filedialog.askdirectory(title='选择目录', initialdir=(os.path.expanduser(default_dir)))
        print(file_path)

        return file_path

    def save_file(self):
        root = tkinter.Tk()    # 创建一个Tkinter.Tk()实例
        root.withdraw()       # 将Tkinter.Tk()实例隐藏
        default_dir = r"文件路径"
        file_path = tkinter.filedialog.asksaveasfilename(title='保存文件', initialdir=(os.path.expanduser(default_dir)), filetypes=[("MD", ".md")], defaultextension='.md')
        print(file_path)

        return file_path



if __name__ == '__main__':
    com = common()
    com.save_file()
    # com.get_path()
    # com.select_dir()

