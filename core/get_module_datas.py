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


if __name__ == '__main__':
    print(get_datas('module_datas.yaml'))
