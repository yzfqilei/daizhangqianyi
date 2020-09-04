#!/usr/bin/python
# coding:utf-8

import os
from common.read_data import ReadFileData
from common import path_conf


def get_common_params(filename, mainkey):
    """取通用参数方法"""
    datass = ReadFileData()
    yaml_path = os.path.join(path_conf.BASE_DIR, "apidata", filename)
    yaml_data = datass.load_yaml(yaml_path)
    ini_path = os.path.join(path_conf.BASE_DIR, "config", "setting.ini")
    ini_data = datass.load_ini(ini_path)
    access_token = ini_data['logininfo']['access_token']
    refresh_token = ini_data['logininfo']['refresh_token']
    rooturl = ini_data['host']['api_root_url']
    yamlvalue = yaml_data[mainkey]
    if isinstance(yamlvalue['expectresult']['data'], dict):
        checkkeys = yamlvalue['expectresult']['data'].keys()
    else:
        checkkeys = None
    csurl = yamlvalue['route']
    method = yamlvalue['method']
    head = yamlvalue['headers']
    head['access_token'] = access_token
    head['refresh_token'] = refresh_token

    return rooturl, csurl, method, head, yamlvalue, yaml_path, checkkeys


if __name__ == '__main__':
    aa = get_common_params("login.yaml", "用户名错误,密码正确")
    print(aa)
