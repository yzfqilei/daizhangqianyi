#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
import pytest
import os
import arrow
from common.mysql_operate import db
from common.read_data import ReadFileData
import requests
from common.write_data import WriteFileData
from common.get_root_url import get_root_urls
from core.rest_client import RestClient
from core.get_module_datas import get_datas, get_pre_data

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
    # 获取token，写入setting.pip
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
    module_datas = get_pre_data('module_datas.yaml', 'data')
    rooturl = get_root_urls()
    csurl = '/apis/crm-web/module/genjinjilu/insert'
    a = RestClient(rooturl)
    head = {'access-token': is_login[0], 'refresh-token': is_login[1], 'Content-Type': 'application/json;charset=UTF-8'}
    dataid_list = []
    for jdata in module_datas:
        r_in = a.request(csurl, 'POST', json=jdata, headers=head)
        dataid_list.append(json.loads(r_in.text)['data']['_id'])
    yield dataid_list
    csurl_de = '/apis/crm-web/module/genjinjilu/'
    for de_id in dataid_list:
        a.request(csurl_de + de_id, 'DELETE', headers=head)
    print('delete success')


@pytest.fixture(scope='session')
def query_sysuser(is_login):
    """查询人员列表数据"""
    rooturl = get_root_urls()
    csurl = '/apis/crm-web/module/sysUser/list'
    a = RestClient(rooturl)
    jdata = {"conditions": {"status": "正常"}, "pageIndex": 1, "pageSize": 10000}
    head = {'access-token': is_login[0], 'refresh-token': is_login[1], 'Content-Type': 'application/json;charset=UTF-8'}
    r_in = a.request(csurl, 'POST', json=jdata, headers=head)
    sysuser_list = json.loads(r_in.text)['data']
    return sysuser_list


@pytest.fixture(scope='session')
def preset_module_data(is_login):
    """批量插入跟进记录表单数据"""
    module_datas = get_pre_data('preset_data.yaml', 'data')
    rooturl = get_root_urls()
    csurl = '/apis/crm-web/module/genjinjilu/insert'
    a = RestClient(rooturl)
    head = {'access-token': is_login[0], 'refresh-token': is_login[1], 'Content-Type': 'application/json;charset=UTF-8'}
    dataid_list = []
    for jdata in module_datas:
        r_in = a.request(csurl, 'POST', json=jdata, headers=head)
        dataid_list.append(json.loads(r_in.text)['data']['_id'])
    yield dataid_list
    csurl_de = '/apis/crm-web/module/genjinjilu/'
    for de_id in dataid_list:
        a.request(csurl_de + de_id, 'DELETE', headers=head)
    print('delete success')


@pytest.fixture(scope='class')
def pre_company_data():
    """前置插入企业看板（客户数量和员工价值）数据"""
    utc = arrow.now()
    lastnt = utc.shift(months=-1)  # 取上个月
    ym = int(lastnt.format("YYYYMM"))
    ntime = utc.format("YYYY-MM-DD HH:mm:ss")
    cus_datas = get_pre_data("pre_qy_datas.yaml", "customer_num")
    personel_data = get_pre_data("pre_qy_datas.yaml", "personel_value")
    sql_cus = cus_datas % (ym, ym, ym, ntime, ym, ntime, ntime)
    sql_per = personel_data % (ym, ym)
    sql_list_cus = sql_cus.split(';')
    sql_list_per = sql_per.split(';')
    all_sql_list = sql_list_cus + sql_list_per
    for sql in all_sql_list:
        if sql:
            db.execute_db(sql)
    yield
    delete_cus_datas = get_pre_data("pre_qy_datas.yaml", "delete_customer_num")
    delete_per_datas = get_pre_data("pre_qy_datas.yaml", "delete_personel_value")
    update_qz_datas = get_pre_data("pre_qy_datas.yaml", "update_qz")
    db.execute_db(delete_cus_datas)  # 删除预置客户数量数据
    db.execute_db(delete_per_datas)  # 删除预置员工价值数据
    db.execute_db(update_qz_datas) # 还原权重比重为默认值


if __name__ == '__main__':
    is_login()
