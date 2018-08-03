import download_ftp
import os,sys


def log_localrootpath():
    rootpath = download_ftp.download_prolog() # 从FTP服务器下载项目日志文件
    return rootpath


def log_list():
    log_rootpath = log_localrootpath() # 从FTP服务器下载项目日志文件并获得根目录返回值
    loglist = []

    for parent,dirnames,basefilenames in os.walk(log_rootpath):

        for filename in basefilenames:
            if filename.endswith('.log') or filename.endswith('.txt'):
                loglist.append(filename)

    return loglist


def singel_log_contxt():
    loglist = log_list()

    for logfile in loglist:
        scanlog(logfile)


def scanlog(logfile):
    logfile = 0
    pass

log_list()