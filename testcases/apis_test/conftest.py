#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
import pytest
import os
from common.read_data import ReadFileData
import requests
from common.write_data import WriteFileData
from common.get_root_url import get_root_urls
from core.rest_client import RestClient
from core.get_module_datas import get_datas

BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

data = ReadFileData()

wd = WriteFileData()


def get_data_ini(ini_file_name):
    try:
        data_file_path = os.path.join(BASE_PATH, "config", ini_file_name)
        ini_data = data.load_ini(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return ini_data


@pytest.fixture(scope='session')
def is_login():
    """登录"""
    inidata = get_data_ini("setting.ini")
    root_url = inidata['host']['api_root_url']
    login_data = eval(inidata['logininfo']['data'])
    lgurl = inidata['logininfo']['loginurl']
    login_url = root_url + lgurl
    hd = {"Content-Type": "application/json"}
    r = requests.post(login_url, json=login_data, headers=hd)
    result = json.loads(r.text)
    # 获取token，写入setting.ini
    r_dir_data = result['data']
    access_token = r_dir_data['access_token']
    refresh_token = r_dir_data['refresh_token']
    data_file_path = os.path.join(BASE_PATH, "config", 'setting.ini')
    wd.write_ini(data_file_path, 'logininfo', 'access_token', access_token)
    wd.write_ini(data_file_path, 'logininfo', 'refresh_token', refresh_token)
    yield access_token, refresh_token  # 返回token


@pytest.fixture(scope='session')
def customer_moduleid(is_login):
    """客户模块id查询"""
    rooturl = get_root_urls()
    csurl = '/apis/crm-web/module/code/customer'
    a = RestClient(rooturl)
    head = {'access-token': is_login[0], 'refresh-token': is_login[1]}
    r = a.request(csurl, 'GET', headers=head)
    return json.loads(r.text)['data']['id']


@pytest.fixture(scope='session')
def user_moduleid(is_login):
    """人员模块id查询"""
    rooturl = get_root_urls()
    csurl = '/apis/crm-web/module/find/module'
    a = RestClient(rooturl)
    head = {'access-token': is_login[0], 'refresh-token': is_login[1]}
    r = a.request(csurl, 'POST', headers=head)
    return json.loads(r.text)['data'][0]['id']


@pytest.fixture(scope='session')
def insert_module_data(is_login):
    """批量插入跟进记录表单数据"""
    module_datas = get_datas('module_datas.yaml')
    rooturl = get_root_urls()
    csurl = '/apis/crm-web/module/genjinjilu/insert'
    a = RestClient(rooturl)
    head = {'access-token': is_login[0], 'refresh-token': is_login[1], 'Content-Type': 'application/json;charset=UTF-8'}
    dataid_list = []
    for jdata in module_datas:
        r_in = a.request(csurl, 'POST', json=jdata, headers=head)
        dataid_list.append(json.loads(r_in.text)['data']['_id'])
    yield dataid_list
    # csurl_de = '/apis/crm-web/module/genjinjilu/'
    # for de_id in dataid_list:
    #     a.request(csurl_de + de_id, 'DELETE', headers=head)
    # print('delete success')


if __name__ == '__main__':
    is_login()
