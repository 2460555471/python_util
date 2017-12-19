# -*- coding: utf-8 -*-
import os
import shutil

# 复制一个目录下的所有文件到另外一个目录
if __name__=='__main__':
    dir_path = u"E:/results/"
    list = os.listdir(dir_path)
    for i in list:
        aa, bb = i.split(".")
        aa, bb = i.split(".")


        oldname = dir_path + aa + "." + bb
        newname = "test_images/"+aa + "." + bb
        shutil.copyfile(oldname, newname)