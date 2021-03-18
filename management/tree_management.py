# -*- coding: utf-8 -*-
# Author: stevezhangz
# 2021/3/18
# If you use this software directly or indirectly, please strictly abide by the laws of the local government. If you
# agree, you can continue to use it
import sys
from pathlib import Path
import os


class file_tree():
    def __init__(self,pathname):
        assert os.path.exists(pathname)
        self.root_path=Path(pathname)
        self.pathname=Path(pathname)
        self.tree=""
    def get_path_name(self,pathname):
        self.pathname=Path(pathname)
    def get_file_name(self,filename):
        self.filename=filename
    def plot_tree(self,count=0,plot=True,plot_file=True):
        if self.pathname.is_file():
            if plot_file:
                self.tree+="       |"*count+"-*"*2+self.pathname.name+"\n"
        elif self.pathname.is_dir():
            self.tree += "       |" * count + "-*" * 2 + str(self.pathname.relative_to(self.pathname.parent)) +"\\"+ "\n"
            for son_path in self.pathname.iterdir():
                self.pathname=Path(son_path)
                self.plot_tree(count+1,plot_file=plot_file,plot=plot)
        if plot:
            print(self.tree)
        else:
            pass
        self.pathname=self.root_path

    def save_tree(self,file):
        with open(file,"w") as f:
            f.write(self.tree)

    def show(self,file):
        with open(file,"r") as f:
            a=f.read(f)
            print(a)

    def file_delete(self,file_name,model="accurate"):
        count=1
        if self.pathname.is_file():
            if self.pathname.name==file_name:
                print("find {} possible file".format(count),self.pathname)
                choice_cur=input("are you sure? Y or N")
                if choice_cur=='Y':
                    os.remove(str(self.pathname))
                    count+=1
                    print("successfully delete")
        elif self.pathname.is_dir():
            for son_path in self.pathname.iterdir():
                self.pathname = Path(son_path)
                self.file_delete(file_name)
    def path_iter_re(self):
        self.pathname = self.root_path
    def foler_delete(self,folder_name,count=0,model="accurate"):
        count = 1
        if self.pathname.is_file():
            pass
        elif self.pathname.is_dir():
            if self.pathname.name == folder_name:
                print("find {} possible file".format(count), self.pathname)
                choice_cur = input("are you sure? Y or N")
                if choice_cur == 'Y':
                    os.remove(str(self.pathname))
                    count += 1
                    print("successfully delete")
            for son_path in self.pathname.iterdir():
                self.pathname = Path(son_path)
                self.foler_delete(folder_name)

