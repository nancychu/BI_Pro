from ftplib import FTP
import path_config
import os
# import ftplib

def ftpconnect():
    ftp_server = path_config.ftp_server  
    username = path_config.ftp_username  
    password = path_config.ftp_password  

    ftp=FTP()  
    ftp.set_debuglevel(2)  # 打开调试级别2，显示详细信息
    ftp.connect(ftp_server,21)  # 连接,host,端口
    ftp.login(username,password)  # 登录，如果匿名登录则用空串代替即可

    return ftp  

def downloadfile(ftp, remotepath):
    # remotepath = "/fsywl/2018/04/13/9001/GamePlay.log"
    # ftp = ftpconnect()  
    # print(ftp.getwelcome())  # 显示ftp服务器欢迎信息
    localpath = os.path.basename(remotepath) # basename返回Path的最后一个文件名
    bufsize = 1024  # 设置缓冲块大小
    # localpath = 'F:\\project\\BI_LogTest\\FTP\\GamePlay.log'  
    fp = open(localpath,'wb')  # 以写模式在本地打开文件
    ftp.retrbinary('RETR ' + remotepath,fp.write,bufsize)  # 接收服务器上文件并写入本地文件
    ftp.set_debuglevel(0)  # 关闭调试
    fp.close()
    # ftp.quit()  # 退出ftp服务器

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


f = ftpconnect() # 链接登录ftp服务器
d = Download(f, "DCIM/Camera")
f.dir('DCIM/Camera/', d.downloadfilebypath)

d.startdown()









def downloadfile():
    remotepath = "/fsywl/2018/04/13/9001/GamePlay.log"
    ftp = ftpconnect()  
    print(ftp.getwelcome())  # 显示ftp服务器欢迎信息
    bufsize = 1024  # 设置缓冲块大小
    localpath = 'F:\\project\\BI_LogTest\\FTP\\GamePlay.log'  
    fp = open(localpath,'wb')  # 以写模式在本地打开文件
    ftp.retrbinary('RETR ' + remotepath,fp.write,bufsize)  # 接收服务器上文件并写入本地文件
    ftp.set_debuglevel(0)  # 关闭调试
    fp.close()
    ftp.quit()  # 退出ftp服务器


def getftpdir(path):
    dirpaths = ftp.nlst(path)
    for dirname in dirnames:
        local_filename = os.path.join('path',filename)

def test():
    remotepath = "/zhj"
    ftp = ftpconnect()  
    print("serverInfo: " + ftp.getwelcome())  # 显示ftp服务器欢迎信息
    filenames = ftp.nlst(remotepath)
    print(len(filenames))
    for i in range(len(nlst)):
        print(nlst[i])
        ftppath = remotepath + nlst[i]
        print(ftppath)
        for filename in filenames:
        local_filename = os.path.join('C:\\test\\', filename)
        file = open(local_filename, 'wb')
        ftp.retrbinary('RETR '+ filename, file.write)

        file.close()
    ftp.set_debuglevel(0)  # 关闭调试
    ftp.quit()  # 退出ftp服务器


if __name__ == '__main__':
    #downloadfile()
    test()

#os.path.isfile(path) 
# ftp相关命令操作
# ftp.cwd(pathname)                 #设置FTP当前操作的路径
# ftp.dir()                         #显示目录下所有目录信息
# ftp.nlst()                        #获取目录下的文件
# ftp.mkd(pathname)                 #新建远程目录
# ftp.pwd()                         #返回当前所在位置
# ftp.rmd(dirname)                  #删除远程目录
# ftp.delete(filename)              #删除远程文件
# ftp.rename(fromname, toname)#将fromname修改名称为toname。
# ftp.storbinaly("STOR filename.txt",file_handel,bufsize)  #上传目标文件
# ftp.retrbinary("RETR filename.txt",file_handel,bufsize)  #下载FTP文件