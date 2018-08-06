#!/usr/bin/python
#coding:utf-8
"""
Logs parse and format than write to the rigth dir
Author by Qfeian @20131130
"""
import os
import re
from urllib import unquote
import hashlib
import datetime
#from time import sleep
def hour(n=0):
    """Timeformat for hours the default is the current time """
    now = datetime.datetime.now()
    h = now + datetime.timedelta(hours=n)
    return h.strftime('%Y%m%d'), h.strftime('%Y%m%d%H')
def hash_str(str):
    """md5 encryption"""
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()
def unquote_str(str):
    """urldecode by unquote"""
    s = unquote(str)
    return s
def dir_query(str):
    """Check the dir if not exist create it """
    s = os.path.isdir(str)
    if not s:
        os.makedirs(str)
def path_query(paths,str):
    """如果第一次创建文本，则写入第一行内容"""
    s1 = os.path.isfile(paths)
    if not s1:
        f1 = open(paths,'a')
        f1.write(str)
        f1.close()
def main():
    log_dir = "/usr/local/nginx/logs/click.master.com_log/" #需要分析日志的路径
    S_dir = "/data/app/click.master.com/logs/dlogs/" #分析后日志保存路径
    str1 = "tm #*# uid #*# os #*# br #*# ip #*# ul #*# pt #*# pm #*# tl #*# co\n"
    """"format last hour  time """
    (D, H) = hour(-1)
    log_name = 'click.master.com_access.log-' + H  #上小时nginx日志文件
    log_path = os.path.join(log_dir, log_name)
    logfile = open(log_path, 'r')
    crg = re.compile(ur"(^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
                     ur".*&dm=(.*?)"
                     ur"&ul=(.*?)"
                     ur"&tm=(.*?)"
                     ur"&os=(.*?)"
                     ur"&br=(.*?)"
                     ur"&.*?&uid=(\d+)"
                     ur"&pt=(.*?)"
                     ur"&tl=(.*?)"
                     ur"&co=(.*?)&")
    for lines in logfile.readlines():
        """ check up on the  nginx logs by regular"""
        a = crg.findall(lines)
        """ if matching write to the logfile """
        if a:
            (ip, dm, ul, tm, OS, br, uid, pt, tl, co) = a[0]
            pt = unquote_str(pt)
            tl = unquote_str(tl)
            co = unquote_str(co)
            pm = hash_str(pt)
            s = "%s #*# %s #*# %s #*# %s #*# %s #*# %s #*# %s #*# %s #*# %s #*# %s\n" % \
                (tm, uid, OS, br, ip, ul, pt, pm, tl, co)
            W_log = os.path.join(S_dir, dm, D, H)
            W_log = W_log + '.log'
            W_dir = os.path.dirname(W_log)
            """ check  logdir and logpath"""
            dir_query(W_dir)
            path_query(W_log,str1)
            """ write logs """
            f = open(W_log, 'a')
            f.write(s)
#            print s
#            print dm, "\n"
#            sleep(1)
    f.close()
    logfile.close()
if __name__ == "__main__":
    main()