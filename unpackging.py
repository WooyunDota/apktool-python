#!/usr//bin/env python
#-*- coding:UTF-8 -*- 

'Author : qiuyu'

import os

class unpacking():
    def unpack(self):    
        #获取当前目录
        print(os.getcwd())
        path = os.getcwd()+'\\apk'
        #当前目录文件信息
        listfile = os.listdir(path)
        print(listfile)
        #执行apktool方法
        index = 1
        for filename in listfile:
            apkpath = 'apktool d '+path+'\\'+filename
            os.system(apkpath + ' -o ' + 'out\\' + str(index))
            print(apkpath + ' -o ' + 'out\\' + str(index))
            index += 1

    def repack(self):
        print(os.getcwd())
        path = os.getcwd()+'\\out'
        #当前目录文件信息
        listfile = os.listdir(path)
        print(listfile)
        #执行apktool方法
        index = 1
        for filename in listfile:
            apkpath = 'apktool b '+path+'\\'+filename
            os.system(apkpath + ' -o ' + 'unsigned\\' + str(index) + '.apk')
            print(apkpath + ' -o ' + 'out\\' + str(index) + '.apk')
            index += 1

    def signed(self):
        print(os.getcwd())
        path = os.getcwd()+'\\unsigned'
        outputpath = os.getcwd() +'\\signed'
        #当前目录文件信息
        listfile = os.listdir(path)
        print(listfile)
        #执行apktool方法
        index = 1
        for filename in listfile:
            apkpath = 'java -jar signapk.jar platform.x509.pem platform.pk8 '+path+'\\'+filename 
            os.system(apkpath + ' signed\\' + str(index) + '.apk')
            print(apkpath + ' signed\\' + str(index) + '.apk')
            index += 1


if __name__ == '__main__':
    useapktool = unpacking()
    #apktool d
    useapktool.unpack()
    #apktool b
    useapktool.repack()
    #sign
    useapktool.signed()