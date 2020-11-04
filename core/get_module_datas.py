#!/usr/bin/python
# coding:utf-8

import os
from common.read_data import ReadFileData
from common import path_conf


def get_datas(filename):
    """取模块datas方法"""
    datass = ReadFileData()
    yaml_path = os.path.join(path_conf.BASE_DIR, "apidata", filename)
    yaml_data = datass.load_yaml(yaml_path)
    yamlvalue = yaml_data['data']
    return yamlvalue


def get_pre_data(filename, dataname):
    """取模块预置datas方法"""
    datass = ReadFileData()
    yaml_path = os.path.join(path_conf.BASE_DIR, "api_pre_data", filename)
    yaml_data = datass.load_yaml(yaml_path)
    yamlvalue = yaml_data[dataname]
    return yamlvalue


if __name__ == '__main__':
    print(get_pre_data('pre_qy_datas.yaml', "personel_value"))
