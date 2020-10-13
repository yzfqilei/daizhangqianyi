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

reportpath = path_conf.REPORT_PATH
wd = WriteFileData()
rd = ReadFileData()
rooturl = get_root_url.get_root_urls()
result = result_base.ResultBase()
a = RestClient(rooturl)

@pytest.mark.usefixtures("is_login")
@allure.feature("映射用例")
class Test_merge():
    @allure.story("创建映射")
    def test001_create_merge(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('merge.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, json=yamlvalue['data'], headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)
        #获取映射id
        dict = json.loads(res.text)
        data = dict['data']
        merge_id = data['id']
        wd.write_yaml(yaml_path, 'variable', 'merge_id', merge_id)

    @allure.story("源模块搜索过滤映射")
    def test002_source_screen_merge(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('merge.yaml', func_name)
        a = RestClient(rooturl)
        url = csurl + '/756585727382392832'
        res = a.request(url=url, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)

    @allure.story("列表查询")
    def test003list_merge(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('merge.yaml', func_name)
        data= {"pageIndex": 1, "pageSize": 10}
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, json=data, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        pytest.assume('756585727382392832' in res.text)
        pytest.assume('756585730700087298' in res.text)
        pytest.assume('756585727382392833' in res.text)
        pytest.assume('756585730700087325' in res.text)


    @allure.story("源模块字段搜索过滤映射")
    def test004_sourceField_screen_merge(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('merge.yaml', func_name)
        data = {"pageIndex": 1, "pageSize": 10, "sourceModuleId": "756585727382392832", "sourceFieldId": "756585730700087298"}
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, json=data, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("目标模块搜索过滤映射")
    def test005_target_screen_merge(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('merge.yaml', func_name)
        a = RestClient(rooturl)
        url = csurl + '756585727382392833'
        res = a.request(url=url, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)

    @allure.story("目标模块字段搜索过滤映射")
    def test006_targetField_screen_merge(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('merge.yaml', func_name)
        data= {"pageIndex":1,"pageSize":10,"sourceModuleId":"756585727382392832","sourceFieldId":"756585730700087298"}
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, json=data, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("删除映射")
    def test007_delete_merge(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('merge.yaml', func_name)
        a = RestClient(rooturl)
        merge_id = rd.load_yaml_value(yaml_path,'variable','merge_id')
        url = csurl + merge_id
        res = a.request(url=url, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)