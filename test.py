import os,sys

path = 'D:\PyProject\BI_Pro-master\BI_Pro-master\FTP'
filenames = []
for parent, dirnames, basefilenames in os.walk(path):

    for filename in basefilenames:
        if filename.endswith('.log') or filename.endswith('.txt'):
            filenames.append(filename)

            # 防止文件名中包含.  https://www.jianshu.com/p/d6ccc8d9ff73
        fullist = filename.split('.')
        print('fullist: ')
        print(fullist)
        namelist = fullist[:-1]  # list切片
        print('namelist: ')
        print(namelist)
        file_name = ''
        for i in namelist:
            file_name = file_name + i + '.'
            print(file_name)

print(filenames)
print(len(filenames))
