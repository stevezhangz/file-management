# -*- coding: utf-8 -*-
# Author: stevezhangz
# 2021/3/18
# If you use this software directly or indirectly, please strictly abide by the laws of the local government. If you
# agree, you can continue to use it

import os
import sys
import csv
import json
import shutil
from management.tree_management import *
def main():
    check_initialization()
    file_info_update()
    while(1):
        show_list()
        op=choice()
        if op==1:
            print("Good bye!")
            break
def check_initialization():
    if not os.path.exists("options.txt"):
        try:
            file_path = software_initializer()
            with open("options.txt", "w") as f:
                while(1):
                    print("please set some User information")
                    user_name = input("user name")
                    passward = input("password")
                    print("your user information are shown here:","user_name :",user_name ,"passward",passward)
                    choice_cur=input("confim? Y or N")
                    if choice_cur=='Y':
                        f.write(json.dumps({"file_path": file_path, "Initialized": 1,"User information":{"user_name ":user_name ,"passward":passward}}))
                        f.close()
                        break
        except:
            print("file lost!")
    else:
        with open("options.txt", "r") as f:
            file_info = json.load(f)
            if file_info["Initialized"] == 1:
                pass
            else:
                file_path = software_initializer()
                with open("options.txt", "w") as f:
                    f.write(json.dumps({"file_path": file_path, "Initialized": 1}))
                    f.close()
def path_check(path):
    if not os.path.exists(path):
        return 0
    else:
        return path
def software_initializer():
    print("Hi, nice to meet you, I'm paper management. We need to set some path information to cooperation in the future")
    print("If you use this software directly or indirectly, please strictly abide by the laws of the local government. If you agree, you can continue to use it")
    oneofliscenses = input("agree 1 or disagree 0:")
    if int(oneofliscenses)==1:
        path=input("Which path do you want to save the paper:")
        while(1):
            path=path_check(path)
            if path==0:
                correct_choice=input("Path not exist, please re-make or input a correct path: 1. make a path 2. Input a right path")
                while(1):
                    if correct_choice==1 or correct_choice==2:
                        break
                    else:
                        correct_choice = input(
                            "Path not exist, please re-make or input a correct path: 1. make a path 2. Input a right path")
                if correct_choice==1:
                    path=input("path")
                    os.makedirs(path)
                if correct_choice==2:
                    path = input("1.Which path do you want to save the paper")
            else:
                break
        folder_name = input("Give your game archive a cool name!")
        path=path+ folder_name
        os.makedirs(path)
        with open("file_info.txt",'w') as f:
            f.write(json.dumps({"file_path":path }))
            f.close()
        print("Thank you for your cooperation. Everything gose well with your job!")
        return path
    else:
        print("sorry, we only can coperate when you agree obey the law of local government")

def show_list():
    print("\t\t\t\t***********************************************************************************\t\t\t\t")
    print("\t\t\t\t  Hello, smart. Welcome to the file management!                                    \t\t\t\t")
    print("\t\t\t\t  What can I do for you?                                                           \t\t\t\t")
    print("\t\t\t\t              1. Show me the list of papers                                        \t\t\t\t")
    print("\t\t\t\t              2. I want to open a paper                                            \t\t\t\t")
    print("\t\t\t\t              3. I want to delete  files                                           \t\t\t\t")
    print("\t\t\t\t              4. I want to save files                                              \t\t\t\t")
    print("\t\t\t\t              5. Add a new branch                                                  \t\t\t\t")
    print("\t\t\t\t              6. Destroy all                                                       \t\t\t\t")
    print("\t\t\t\t              7. Quit                                                              \t\t\t\t")
    print("\t\t\t\t***********************************************************************************\t\t\t\t")

def choice():
    # This operation is used to ensure that the index you enter is the corresponding index in the directory
    def int_check(num):
        if not isinstance(num, int):
            try:
                num = int(num)
                return num
            except:
                return 0
    a = input("Please make a choice:")
    while(1):
        a=int_check(a)
        if a>=1 and a<=7:
            break
        else:
            a=input("Please re-choice, thank you!")

    if a==1:
        choice1()
    if a==2:
        choice2()
    if a==3:
        choice3()
    if a==4:
        choice4()
    if a == 5:
        choice5()
    if a == 6:
        choice6()
    if a==7:
        choice = input("Are you sure? Y or N:")
        if choice == "Y":
            return 1
        else:
            return 0
def choice1():
    with open("file_info.txt", "r+") as f:
        file_info = f.readline()
        file_info = eval(file_info)
        file_path = file_info["file_path"]
        tree_manager = file_tree(file_path)
        if "paper_list" not in file_info.keys():
            tree_manager.plot_tree()
        else:
            print(file_info["paper_list"])
def choice2():
    pass
def choice3():
    with open("file_info.txt", "r+") as f:
        file_info = f.readline()
        file_info = eval(file_info)
        file_path = file_info["file_path"]
        tree_manager = file_tree(file_path)
        tree_manager.plot_tree(plot=False)
        if "paper_list" not in file_info.keys():
            tree_manager.plot_tree()
        else:
            print(file_info["paper_list"])
        while(1):
            try:
                file_name=input("do you want to delete a paper or folder (Y or N)")
                if file_name=="Y":
                    file_name=input("please tell me the title of it")
                    tree_manager.file_delete(file_name=file_name)
                    quit=input("quit? 0 or1")
                    if quit:
                        tree_manager.path_iter_re()
                        tree_manager.plot_tree(plot=False)
                        break
                if file_name=="N":
                    folder_name = input("please tell me the folder name")
                    foler_delete_path=tree_manager.foler_delete(folder_name)
                    quit = input("quit? 0 or1")
                    if quit:
                        tree_manager.path_iter_re()
                        tree_manager.plot_tree(plot=False)
                        break
            except:
                pass
def choice4():
    with open("file_info.txt","r+") as f:
        file_info=f.readline()
        file_info=eval(file_info)
        file_path=file_info["file_path"]
        tree_manager=file_tree(file_path)
        tree_manager.plot_tree(plot_file=False,plot=False)
        tree=tree_manager.tree
        print(tree)
        while(1):
            folder_name=input("Folders are shown as below, so which folder do you prefer:")
            foler_path=file_path+"//"+folder_name
            if os.path.exists(foler_path):
                break
        f.close()
    done =0
    while (1):
        try:
            paper_list = input("please tell me whether move a set of papers or just several(Y or N):")
            if paper_list == 'Y':
                paper_path = input("please tell the path of your papers now:")
                assert os.path.exists(paper_path)
                done=file_move_foler(paper_path, foler_path)
            if paper_list == 'N':
                while(1):
                    try:
                        file=input("path of a paper:")
                        file_move_single(file,foler_path)
                    except:
                        print("path wrong")
                    quit_signle = input("quit? 0 or1")
                    if quit_signle:
                        break
            if done:
                with open("file_info.txt", "r+") as f:
                    file_info = f.readline()
                    file_info = eval(file_info)
                    file_path = file_info["file_path"]
                    tree_manager = file_tree(file_path)
                    tree_manager.plot_tree(plot=False)
                    f.close()
                with open("file_info.txt", "w+") as f:
                    file_info["paper_list"] = tree_manager.tree
                    f.write(json.dumps(file_info))
                    f.close()
                break
        except:
            pass
def choice5():
    with open("file_info.txt","r+") as f:
        file_info=f.readline()
        file_info=eval(file_info)
        file_path=file_info["file_path"]
        tree_manager=file_tree(file_path)
        choice_cur=input("Do you want to check the root? Y or N:")
        if choice_cur=="Y":
            if "paper_list" not in file_info.keys():
                tree_manager.plot_tree()
            else:
                print(file_info["paper_list"])
        else:
            pass
        new_brunch=input("name of the new bunch you want to add: 0 represent cancel")
        if new_brunch!=0:
            try:
                os.makedirs(file_path+"\\"+new_brunch)
            except:
                raise FileExistsError
            tree_manager.plot_tree(plot=False)
        else:
            pass
        f.close()
    if new_brunch!=0:
        with open("file_info.txt", "w+") as f:
            file_info["paper_list"] =tree_manager.tree
            f.write(json.dumps(file_info))
            f.close()
def choice6():
    ensure=input("are you sure? Y or N")
    if ensure=='Y':
        with open("options.txt", "r+") as f:
            file_info = f.readline()
            file_info = eval(file_info)
            user_information = file_info["User information"]
            f.close()
        print(" please input your user information to confirm")
        user_name=input("user name")
        passward=input("passward")
        check = {"user_name ": user_name, "passward": passward}
        while(1):
            if check==user_information:
                with open("file_info.txt", "r+") as f:
                    file_info = f.readline()
                    file_info = eval(file_info)
                    file_path = file_info["file_path"]
                    os.remove(file_path)
                    os.remove("file_info.txt")
                    os.remove("options.txt")
                    print("clear all!")
            else:
                choice_quit=input("continue or quit Y or N")
                if choice_quit=='Y':
                    user_name = input("user name")
                    passward = input("passward")
                    check = {"user_name ": user_name, "passward": passward}
                if choice_quit=='N':
                    print("files remain")
                    break

def file_move_single(filepath,target_path):
    check_path=Path(filepath)
    assert check_path.is_file()
    shutil.move(filepath,target_path)
def file_move_foler(filepath,target_path,all_move=False):
    filepath=Path(filepath)
    count=0
    count1=0
    if not all_move:
        for p in filepath.iterdir():
            shutil.move(str(p),target_path)
            if p.is_file():
                count+=1
            if p.is_dir():
                count1+=1
    else:
        for p in filepath.iterdir():
            if p.is_file():
                shutil.move(str(p),target_path)
                count+=1
            if p.is_dir():
                file_move_foler(str(p),target_path)

    if not all_move:
        print("total {} files and {} folders".format(count,count1))

    else:
        print("total {} files".format(count))
    return 1
def file_info_update():
    with open("file_info.txt","r+") as f:
        file_info=f.readline()
        file_info=eval(file_info)
        file_path=file_info["file_path"]
        tree_manager=file_tree(file_path)
        tree_manager.plot_tree(plot=False)
        f.close()
    with open("file_info.txt", "w+") as f:
        file_info["paper_list"] =tree_manager.tree
        f.write(json.dumps(file_info))
        f.close()











