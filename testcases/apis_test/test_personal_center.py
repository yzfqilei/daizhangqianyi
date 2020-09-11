#!/usr/bin/python
# coding:utf-8
from core.checkresult import check_codes_msg,check_datas
from core.rest_client import RestClient
from common.read_data import ReadFileData
from common import path_conf
from common.write_data import WriteFileData
import allure
import pytest
import os,sys,json
from core.common_params import get_common_params
from common.mysql_operate import db
from common import get_id
import requests
import ast
from core.result import Result

wd = WriteFileData()
reportpath = path_conf.REPORT_PATH


@pytest.mark.usefixtures("is_login")
@allure.feature("个人中心测试用例")
class Testpersonal_center():
    @pytest.fixture(scope='module', autouse=True)
    def test_company_infor001(self):
        func_name = sys._getframe().f_code.co_name
        rooturl, csurl, method, headers, yamlvalue, yaml_path, checkkeys = get_common_params('personal_center.yaml',func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl,method=method,headers=headers)
        print(res.text)
        check_codes_msg(res,yamlvalue)
        check_datas(res,yamlvalue,['companyName'])



    def test_user_infor002(self, xinzeng):
        #传入用例名称获取yaml数据字典
        func_name=sys._getframe().f_code.co_name
        func_name = sys._getframe().f_code.co_name
        rooturl, csurl, method, headers, yamlvalue, yaml_path, checkkeys = get_common_params('personal_center.yaml',
                                                                                             func_name)
        a = RestClient(rooturl)
        res = a.request(csurl, method,headers=headers)
        print(res.text)
        check_codes_msg(res,yamlvalue)
        check_datas(res,yamlvalue,['_id','_createDept'])
        aa = xinzeng[0]
        xinzeng[1]

    def test_modify_password003(self):
        #传入用例名称获取yaml数据字典
        func_name=sys._getframe().f_code.co_name
        rooturl, csurl, method, headers, yamlvalue, yaml_path, checkkeys = get_common_params('personal_center.yaml',func_name)
        a = RestClient(rooturl)
        res = a.request(csurl, method, json=yamlvalue['data1'], headers=headers)
        check_codes_msg(res,yamlvalue)

        #调换新旧密码值，将密码改回
        res = a.request(csurl, method, json=yamlvalue['data2'], headers=headers)
        check_codes_msg(res,yamlvalue)
        setattr(Result,'a','111')


    def test_modify_user_info004(self):
        func_name = sys._getframe().f_code.co_name
        rooturl, csurl, method, headers, yamlvalue, yaml_path, checkkeys = get_common_params('personal_center.yaml', func_name)
        r = RestClient(rooturl)
        res = r.request(csurl, method, json=yamlvalue['data1'], headers=headers)
        check_codes_msg(res, yamlvalue)
        check_datas(res, yamlvalue, ['username', 'truename','sex'])
        print('-------企业信息已修改成功-------')
        res = r.request(csurl, method, json=yamlvalue['data2'], headers=headers)
        check_codes_msg(res, yamlvalue)
        res_dir=json.loads(res.text)
        pytest.assume(res_dir['data']['username'],yamlvalue['expectresult_renew']['data']['username'])
        pytest.assume(res_dir['data']['truename'],yamlvalue['expectresult_renew']['data']['truename'])
        pytest.assume(res_dir['data']['sex'],yamlvalue['expectresult_renew']['data']['sex'])
        print('-------企业信息修改已复原-------')
        self.id = '1111'

    #企业信息修改功能异常
     # def test_modify_conpany_info005(self):
     #    func_name = sys._getframe().f_code.co_name
     #    rooturl, csurl, method, headers, yamlvalue, yaml_path, checkkeys = get_common_params('personal_center.yaml', func_name)
     #    r = RestClient(rooturl)
     #    res = r.request(csurl, method, json=yamlvalue['data1'], headers=headers)
     #    check_codes_msg(res, yamlvalue)
     #    check_datas(res, yamlvalue, ['username', 'truename','sex'])

    def test_change_phone_number006(self):
        func_name = sys._getframe().f_code.co_name
        rooturl, csurl, method, headers, yamlvalue, yaml_path, checkkeys = get_common_params('personal_center.yaml',func_name)
        r = RestClient(rooturl)
        res = r.request(csurl, method, headers=headers)
        check_codes_msg(res, yamlvalue)
        check_datas(res, yamlvalue)

    def test_lookfor_notice007(self):
        #数据库插入notice数据
        id=get_id()
        print(id)
        # db.execute_db('')

