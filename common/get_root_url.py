#!/usr/bin/python
# coding:utf-8

import os
from common.read_data import ReadFileData
from common import path_conf


def get_root_urls():
    datass = ReadFileData()
    ini_path = os.path.join(path_conf.BASE_DIR, "config", "setting.ini")
    ini_data = datass.load_ini(ini_path)
    rooturl = ini_data['host']['api_root_url']
    return rooturl


if __name__ == '__main__':
    print(get_root_urls())
