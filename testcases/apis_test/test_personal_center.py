#!/usr/bin/python
# coding:utf-8
from core.checkresult import check_codes_msg,check_datas
from core.rest_client import RestClient
from common.read_data import ReadFileData
from common import path_conf
from common.write_data import WriteFileData
import allure
import pytest
import os,sys


rd = ReadFileData()
wd = WriteFileData()
yaml_path = os.path.join(path_conf.BASE_DIR, "apidata", "personal_center.yaml")
yaml_data = rd.load_yaml(yaml_path)
ini_path = os.path.join(path_conf.BASE_DIR, "config", "setting.ini")
ini_data = rd.load_ini(ini_path)
reportpath = path_conf.REPORT_PATH
rooturl = ini_data['host']['api_root_url']


@pytest.mark.usefixtures('is_login')
@allure.feature("个人中心测试用例")
class Testpersonal_center():
    @allure.story('test_company_infor001')
    def test_company_infor001(self):
        #传入用例名称获取yaml数据字典
        func_name=sys._getframe().f_code.co_name
        data=yaml_data[func_name]

        #读取yaml接口参数信息
        loginurl =data['route']
        method = data['method']
        json_data = data['data']
        hd = data['headers']
        #请求头加入token
        hd['access-token']=ini_data['logininfo']['access_token']
        hd['refresh-token'] = ini_data['logininfo']['refresh_token']
        a = RestClient(rooturl)
        res = a.request(loginurl, method, json=json_data, headers=hd)
        check_codes_msg(res,data)
        check_datas(res,data,['companyName'])

    def test_user_infor002(self):
        #传入用例名称获取yaml数据字典
        func_name=sys._getframe().f_code.co_name
        data=yaml_data[func_name]

        #读取yaml接口参数信息
        loginurl =data['route']
        method = data['method']
        json_data = data['data']
        hd = data['headers']
        #请求头加入token
        hd['access-token']=ini_data['logininfo']['access_token']
        hd['refresh-token'] = ini_data['logininfo']['refresh_token']
        a = RestClient(rooturl)
        res = a.request(loginurl, method, json=json_data, headers=hd)
        check_codes_msg(res,data)
        check_datas(res,data,['_id','_createDept'])

    def test_modify_password003(self):
        #传入用例名称获取yaml数据字典
        func_name=sys._getframe().f_code.co_name
        data=yaml_data[func_name]

        #读取yaml接口参数信息
        loginurl =data['route']
        method = data['method']
        json_data = data['data1']
        hd = data['headers']
        #请求头加入token
        hd['access-token']=ini_data['logininfo']['access_token']
        hd['refresh-token'] = ini_data['logininfo']['refresh_token']
        a = RestClient(rooturl)
        res = a.request(loginurl, method, json=json_data, headers=hd)
        check_codes_msg(res,data)

        #调换新旧密码值，将密码改回
        json_data=data['data2']
        res = a.request(loginurl, method, json=json_data, headers=hd)
        check_codes_msg(res, data)


