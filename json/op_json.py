import json
# -*- coding: UTF-8 -*-
def loadFont():
    f = open("Settings.json", encoding='utf-8')
    # 设置以utf-8解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
    setting = json.load(f)
    name=setting['name']
    score = setting['study']['score']
    age = setting['age']
    return name,score,age
if __name__=='__main__':
    name,score, age = loadFont()
    print(name,score,age)

