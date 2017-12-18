# -*- coding: utf-8 -*-
import os
import shutil

if __name__=='__main__':
    dir_path = u"E:/results/"
    list = os.listdir(dir_path)
    for i in list:
        aa, bb = i.split(".")

        oldname = dir_path + aa + "." + bb
        newname = "test_images/"+aa + "." + bb
        shutil.copyfile(oldname, newname)


# import os
# for root, dirs, files in os.walk(".", topdown=True):
#     for name in files:
#         print(os.path.join(root, name))
#     for name in dirs:
#         print(os.path.join(root, name))


import os
for root, dirs, files in os.walk('.', topdown=True):
    for name in files:
        aa,bb=name.split('.')
        if bb=='jpg':
            os.remove(os.path.join(root, name))
    for name in dirs:
        os.rmdir(os.path.join(root, name))