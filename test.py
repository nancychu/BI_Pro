
import os,csv
import path_config
import text_datafile


def log_list(logtype):  # logtype:name, path 说明：返回

    log_rootpath = path_config.local_ftp_path # 从FTP服务器下载项目日志文件并获得根目录返回值
    # rename_logtocsv(log_rootpath)  # 将日志文件转换为csv格式
    lognamelist = []
    logfullpath = []

    for parent,dirnames,basefilenames in os.walk(log_rootpath):

        for filename in basefilenames:

            if filename.endswith('.log') or filename.endswith('.txt') or filename.endswith('.csv'):

                lognamelist.append(filename)  # 将每个日志文件名 都加到lognamelist中

                curndir = os.getcwd() # 获取当前路径，即log_rootpath
                os.chdir(parent)  # 设置当前路径为目标目录，即filename所在目录
                newdir = os.getcwd()

                curfilepath = newdir + '\\' + filename
                logfullpath.append(curfilepath)
                os.chdir(curndir)

    if logtype == 'name':
        return lognamelist # 返回所有目录下的log文件，List

    if logtype == 'path':
        return logfullpath  # 返回所有目录下的完整log文件路径，list

    else:
        print("log_list()参数请输入'name'或'path'")


def scanlog():
    logfullpathlist = log_list('path')  # 获取文件路径，已转为csv格式
    valuelen = len(text_datafile.datalist)
    # print(logfullpathlist[0])
    with open(logfullpathlist[0],'r') as log_csvfile:

        reader = csv.reader(log_csvfile)
        firstline = next(reader)  # 日志首行数据，list

        print('firstline:start checking log value length...')
        # print("Chencking log value length: 日志字段数 " + str(len(firstline)) + "数据文档字段数： " + str(valuelen))
        if len(firstline) == valuelen:
            print("Chencking log value length: pass")
        else:
            print("Chencking log value length: fail 日志字段数 " + str(len(firstline)) + "数据文档字段数： " + str(valuelen))
            log_csvfile.close()

        print('firstline:start checking if value null...')
        nullindex = []
        for value in firstline:

            if value.strip() == '' or value.isspace():
                nullindex.append({value : firstline.index(value)})
                # print(nullindex)
            else:
                # print(value + ' pass')
                continue

        if nullindex:
            print("firstline:FAIL, 存在空字段：" + str(nullindex))
        # print('firstline: NOT NULL pass')
        # print(firstline)
        # print(next(reader))
    print('--------------------------------------')

scanlog()





# path = 'F:\project\BI_LogTest\FTP'
# filenames = []
# for parent, dirnames, basefilenames in os.walk(path):
#
#     for filename in basefilenames:
#
#         if filename.endswith('.log') or filename.endswith('.txt'):   # 这里是记录所有日志文件名，返回一个filenames的list
#
#             fullist = filename.split('.')    # 防止文件名中包含.  https://www.jianshu.com/p/d6ccc8d9ff73
#             print('fullist: ')
#             print(fullist)
#             namelist = fullist[:-1]  # list切片
#             print('namelist: ')
#             print(namelist)
#             file_name = ''
#             for i in namelist:
#                 file_name = file_name + i + '.'
#                 print(file_name)
#
#             curndir = os.getcwd()    #获取当前路径
#             print (curndir)
#
#             os.chdir(parent)            #设置当前路径为目标目录
#             newdir = os.getcwd()    #验证当前目录
#             print (newdir)
#
#             filetype = filename.split('.')[-1]    #获取目标文件格式
#
#             if filetype == 'log' or filetype == 'txt':    #修改目标目录下指定后缀的文件（包含子目录）
#                 os.rename(filename,file_name + 'csv')
#
#             else:
#                 print(curndir + " ：没有文件后缀名")
#
#             os.chdir(curndir)    #回到之前的路径




