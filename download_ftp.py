from ftpsync.targets import FsTarget
from ftpsync.ftp_target import FtpTarget
from ftpsync.synchronizers import DownloadSynchronizer
import path_config
import os


def download_prolog():

    localpath = path_config.local_ftp_path # 本地保存的ftp目录
    os.makedirs(localpath, 0o777)  # 创建本地日志文件夹

    local = FsTarget(localpath)
    remote = FtpTarget(path_config.ftp_remotepath, path_config.ftp_server, username=path_config.ftp_username, password=path_config.ftp_password)
    opts = {"resolve": "skip", "verbose": 1}

    s = DownloadSynchronizer(local, remote, opts) # 下载ftp日志文件夹
    s.run()

    return localpath