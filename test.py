import os,sys

path = 'F:/project/BI_LogTest/FTP/zhj'
filenames = []
for parent,dirnames,basefilenames in os.walk(path):

    for filename in basefilenames:
        if filename.endswith('.log') or filename.endswith('.txt'):
            filenames.append(filename)
print(filenames)
print(len(filenames))