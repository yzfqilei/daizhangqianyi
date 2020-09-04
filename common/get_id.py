#!/usr/bin/python
# coding:utf-8

import random
import string
import time
import os
from common.read_data import ReadFileData
from common import path_conf
from common.write_data import WriteFileData


def getid():
    """数据库id生成器，每次使用后+1"""
    wd = WriteFileData()
    datass = ReadFileData()
    ini_path = os.path.join(path_conf.BASE_DIR, "config", "setting.ini")
    ini_data = datass.load_ini(ini_path)
    sqlid_start = ini_data['other']['sql_id']
    sqlid_end = int(sqlid_start) + 1
    data_file_path = os.path.join(path_conf.INI_PATH, 'setting.ini')
    wd.write_ini(data_file_path, 'other', 'sql_id', str(sqlid_end))
    return sqlid_start


if __name__ == '__main__':
    print(getid())
