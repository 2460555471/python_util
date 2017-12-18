# -*- coding: utf-8 -*-
import os
# 递归打印出当前路径下的所有文件名字（包括目录）
# topdown参数指明了是否是从上至下，或者是从下至上遍历
if __name__=='__main__':
    for root, dirs, files in os.walk(".", topdown=True):
        for name in files:
            print(os.path.join(root, name))
            # os.remove(os.path.join(root, name)) #删除文件的操作
        for name in dirs:
            print(os.path.join(root, name))
            # os.rmdir(os.path.join(root, name))  #删除目录的操作
