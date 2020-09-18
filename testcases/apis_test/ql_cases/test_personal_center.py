#!/usr/bin/python
# coding:utf-8
from core.checkresult import check_codes_msg, check_datas
from core.rest_client import RestClient
from common.write_data import WriteFileData
from core.common_params import get_common_params
import json,sys
import allure
import pytest
from common import path_conf
from core import result_base
from common import get_root_url


reportpath = path_conf.REPORT_PATH
wd = WriteFileData()
rooturl = get_root_url.get_root_urls()
result = result_base.ResultBase()
a = RestClient(rooturl)


@pytest.mark.usefixtures("is_login")
@allure.feature("个人中心测试用例")
class Testpersonal_center():
    def test_company_infor001(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('personal_center.yaml',func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl,method=method,headers=headers)
        print(res.text)
        check_codes_msg(res,yamlvalue, mainkey)
        check_datas(res,yamlvalue)


    def test_user_infor002(self):
        #传入用例名称获取yaml数据字典
        func_name=sys._getframe().f_code.co_name
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('personal_center.yaml',func_name)
        a = RestClient(rooturl)
        res = a.request(csurl, method,headers=headers)
        print(res.text)
        check_codes_msg(res,yamlvalue, mainkey)
        check_datas(res,yamlvalue)

    def test_modify_password003(self):
        #传入用例名称获取yaml数据字典
        func_name=sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('personal_center.yaml',func_name)
        a = RestClient(rooturl)
        res = a.request(csurl, method, json=yamlvalue['data1'], headers=headers)
        check_codes_msg(res,yamlvalue, mainkey)

        #调换新旧密码值，将密码改回
        res = a.request(csurl, method, json=yamlvalue['data2'], headers=headers)
        check_codes_msg(res,yamlvalue, mainkey)


    def test_modify_user_info004(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('personal_center.yaml', func_name)
        r = RestClient(rooturl)
        res = r.request(csurl, method, json=yamlvalue['data1'], headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)
        print('-------企业信息已修改成功-------')
        res = r.request(csurl, method, json=yamlvalue['data2'], headers=headers)
        # check_codes_msg(res, yamlvalue,mainkey)
        res_dir=json.loads(res.text)
        pytest.assume(res_dir['data']['username'],yamlvalue['expectresult_renew']['data']['username'])
        pytest.assume(res_dir['data']['truename'],yamlvalue['expectresult_renew']['data']['truename'])
        pytest.assume(res_dir['data']['sex'],yamlvalue['expectresult_renew']['data']['sex'])
        print('-------企业信息修改已复原-------')

    def test_modify_conpany_info005(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey= get_common_params('personal_center.yaml', func_name)
        r = RestClient(rooturl)
        res = r.request(csurl, method, json=yamlvalue['data'], headers=headers)

        check_codes_msg(res, yamlvalue,mainkey)
        check_datas(res, yamlvalue)

    def test_change_phone_number006(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('personal_center.yaml',func_name)
        r = RestClient(rooturl)
        res = r.request(csurl, method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    def test_lookfor_notice007(self):
        #数据库插入消息


