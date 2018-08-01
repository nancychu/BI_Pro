#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
from ftplib import FTP

def ftpconnect():
    ftp_server = '192.168.0.104'

    ftp=FTP()
    ftp.set_debuglevel(2) #打开调试级别2，显示详细信息
    ftp.connect(ftp_server, 2121) #连接
    ftp.login() #登录，如果匿名登录则用空串代替即可

    return ftp

def downloadfile(ftp, remotepath):
    localpath = os.path.basename(remotepath)
    fp = open(localpath,'wb') #以写模式在本地打开文件
    ftp.retrbinary('RETR ' + remotepath, fp.write) #接收服务器上文件并写入本地文件
    ftp.set_debuglevel(0) #关闭调试
    fp.close()

def _remove_empty(array):
    return [x for x in array if x !='']

class Download:
    def __init__(self, ftp, parent_abs):
        self._ftp = ftp
        self._parent_abs = parent_abs
        self._file_list = []

    def downloadfilebypath(self, path):
        filename = _remove_empty(path.split(' '))

        filename = ' '.join(filename[8:]) #这里是得到文件名，不同的ftp版本，可能结果不一样
        if filename.endswith('.jpg'):
            self._file_list.append(filename)

    def startdown(self):
        for fn in self._file_list:
            remotepath = os.path.join(self._parent_abs, fn)
            print "Downfile file:" + remotepath
            downloadfile(self._ftp, remotepath)


f = ftpconnect()
d = Download(f, "DCIM/Camera")
f.dir('DCIM/Camera/', d.downloadfilebypath)

d.startdown()