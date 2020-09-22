#!/usr/bin/python
# coding:utf-8
from core.checkresult import check_codes_msg, check_datas
from core.rest_client import RestClient
from common.write_data import WriteFileData
from core.common_params import get_common_params
import json, sys, time, random
import allure
import pytest
from common import path_conf
from core import result_base
from common import get_root_url
from common.mysql_operate import db

reportpath = path_conf.REPORT_PATH
wd = WriteFileData()
rooturl = get_root_url.get_root_urls()
result = result_base.ResultBase()
a = RestClient(rooturl)


@pytest.mark.usefixtures("is_login")
@allure.feature("流程管理测试用例")
class Test_process_manage():
    @allure.story("查询流程")
    def test_search_process001(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("过滤所有类型流程")
    def test_screen_all002(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("过滤审批流")
    def test_screen_approval_folw003(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("过滤工作流")
    def test_screen_work_folw004(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("过滤停用流程")
    def test_screen_status_deactive005(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("过滤启用流程")
    def test_screen_status_active006(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("过滤所有状态的流程")
    def test_screen_status_all007(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)