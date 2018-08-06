import download_ftp
import os,sys
import path_config


def log_list():
    log_rootpath = path_config.local_ftp_path # 从FTP服务器下载项目日志文件并获得根目录返回值
    loglist = []

    for parent,dirnames,basefilenames in os.walk(log_rootpath):

        for filename in basefilenames:
            if filename.endswith('.log') or filename.endswith('.txt'):
                loglist.append(filename)

    return loglist # 返回所有目录下的log文件，List


def singel_log_contxt():
    loglist = log_list() # 获取log文件list

    for logfileName in loglist:
        scanlog(logfileName)  # 检查所有Log文件 ，logfile 单个log文件名


def scanlog(logfileName):
    logfilepath = path_config.local_ftp_path + '/' + logfileName
    with open(logfilepath,'r') as f:
        reader = 11


log_list()

if __name__ == '__main__':
    download_ftp.download_prolog()  # 从FTP服务器下载项目日志文件
