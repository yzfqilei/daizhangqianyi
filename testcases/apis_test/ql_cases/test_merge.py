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
@allure.feature("归集用例")
class Test_merge():
    @allure.story("创建归集")
    def test001_create_merge(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('merge.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, json=yamlvalue['data'], headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)
        dict = json.loads(res.text)
        data = dict['data']
        id = data['id']
        return id

    @allure.story("删除归集")
    def test002_delete_merge(self):
        id = Test_merge.test001_create_merge(self)
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('merge.yaml', func_name)
        a = RestClient(rooturl)
        url = csurl + str(id)
        res = a.request(url=url, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("搜索过滤归集")
    def test003_screen_merge(self):
        id = Test_merge.test001_create_merge(self)
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('merge.yaml', func_name)
        a = RestClient(rooturl)
        url = csurl + str(id)
        res = a.request(url=url, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)