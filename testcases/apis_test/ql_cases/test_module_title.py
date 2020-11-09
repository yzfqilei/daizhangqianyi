#!/usr/bin/python
# coding:utf-8
from core.checkresult import check_codes_msg, check_datas
from core.rest_client import RestClient
from common.write_data import WriteFileData
from common.read_data import ReadFileData
from core.common_params import get_common_params
import json, sys, time, random
import allure
import pytest
from common import path_conf
from core import result_base
from common import get_root_url
from common.mysql_operate import db
from common.convert import convert_json_to_yaml

reportpath = path_conf.REPORT_PATH
wd = WriteFileData()
rd = ReadFileData()
rooturl = get_root_url.get_root_urls()
result = result_base.ResultBase()
a = RestClient(rooturl)

# @pytest.mark.usefixtures("is_login")
@pytest.mark.usefixtures("is_login","preset_module_data")
@allure.feature("模块菜单表头用例")
class Test_module_title():
    @allure.story("设置’联系人‘查询字段")
    def test001_set_contact_search(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('test_module_title.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, json=yamlvalue['data'], headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("查询不存在的联系人")
    def test002_search_contact_nonexist(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('test_module_title.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, json=yamlvalue['data'], headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("查询存在的联系人")
    def test003_search_contact_exist(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('test_module_title.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, json=yamlvalue['data'], headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("设置’手机号码‘查询字段")
    def test004_set_phone_search(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('test_module_title.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, json=yamlvalue['data'], headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("查询不存在的手机号")
    def test005_search_phone_nonexist(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('test_module_title.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, json=yamlvalue['data'], headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("查询存在的手机号")
    def test006_search_phone_exist(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('test_module_title.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, json=yamlvalue['data'], headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("设置’数量1‘查询字段")
    def test007_set_number1_search(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('test_module_title.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, json=yamlvalue['data'], headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("查询不存在的数量1")
    def test008_search_number1_nonexist(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('test_module_title.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, json=yamlvalue['data'], headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("查询存在的数量1")
    def test009_search_number1_exist(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('test_module_title.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, json=yamlvalue['data'], headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("创建筛选：数量1等于数量2")
    def test010_create_screen_equal(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('test_module_title.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, json=yamlvalue['data'], headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)
        #获取筛选id
        dict = json.loads(res.text)
        data = dict['data']
        equal_id = data['id']
        wd.write_yaml(yaml_path, 'variable', 'equal_id', equal_id)

    @allure.story("筛选：数量1等于数量2，展示筛选结果")
    def test011_screen_result(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('test_module_title.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, json=yamlvalue['data'], headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("删除筛选：数量1等于数量2")
    def test012_del_equal(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('test_module_title.yaml', func_name)
        a = RestClient(rooturl)
        url = csurl + rd.load_yaml_value(yaml_path,'variable','equal_id')
        res = a.request(url=url, method=method, json=yamlvalue['data'], headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("创建筛选：数量1不等于数量2")
    def test013_create_screen_neq(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('test_module_title.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, json=yamlvalue['data'], headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)
        #获取筛选id
        dict = json.loads(res.text)
        data = dict['data']
        neq_id = data['id']
        wd.write_yaml(yaml_path, 'variable', 'neq_id', neq_id)

    @allure.story("筛选：数量1不等于数量2，展示筛选结果")
    def test014_screen_result(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('test_module_title.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, json=yamlvalue['data'], headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("删除筛选：数量1不等于数量2")
    def test015_del_neq(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('test_module_title.yaml', func_name)
        a = RestClient(rooturl)
        url = csurl + rd.load_yaml_value(yaml_path, 'variable', 'neq_id')
        res = a.request(url=url, method=method, json=yamlvalue['data'], headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

