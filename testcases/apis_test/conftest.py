#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
import pytest
import os
from common.read_data import ReadFileData
import requests

BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

data = ReadFileData()


def get_data_ini(ini_file_name):
    try:
        data_file_path = os.path.join(BASE_PATH, "config", ini_file_name)
        ini_data = data.load_ini(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return ini_data


# @pytest.fixture(scope='session')
def is_login():
    """登录"""
    inidata = get_data_ini("setting.ini")
    root_url = inidata['host']['api_root_url']
    login_data = eval(inidata['logininfo']['data'])
    lgurl = inidata['logininfo']['loginurl']
    login_url = root_url + lgurl
    hd = {"Content-Type": "application/json"}
    r = requests.post(login_url, json=login_data,headers=hd)
    result = json.loads(r.text)
    print(result)


if __name__ == '__main__':
    is_login()
