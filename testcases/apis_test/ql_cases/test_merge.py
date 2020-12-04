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
ids = {'order':[],'huikuanjilu': []}

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
        #获取映射id
        dict = json.loads(res.text)
        data = dict['data']
        merge_id = data['id']
        wd.write_yaml(yaml_path, 'variable', 'merge_id', merge_id)

    @allure.story("源模块搜索过滤归集")
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


    @allure.story("源模块字段搜索过滤归集")
    def test004_sourceField_screen_merge(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('merge.yaml', func_name)
        data = {"pageIndex": 1, "pageSize": 10, "sourceModuleId": "756585727382392832", "sourceFieldId": "756585730700087298"}
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, json=data, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("目标模块搜索过滤归集")
    def test005_target_screen_merge(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('merge.yaml', func_name)
        a = RestClient(rooturl)
        url = csurl + '756585727382392833'
        res = a.request(url=url, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)

    @allure.story("目标模块字段搜索过滤归集")
    def test006_targetField_screen_merge(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('merge.yaml', func_name)
        data= {"pageIndex":1,"pageSize":10,"sourceModuleId":"756585727382392832","sourceFieldId":"756585730700087298"}
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, json=data, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)


    @allure.story("删除归集")
    def test007_delete_merge(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('merge.yaml', func_name)
        a = RestClient(rooturl)
        merge_id = rd.load_yaml_value(yaml_path,'variable','merge_id')
        url = csurl + merge_id
        res = a.request(url=url, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)


#基于预置归集测试以下功能
    #公共方法
        #订单中预置1条数据
    def insert_order_data(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('merge.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method,json=yamlvalue['data'], headers=headers)
        res_json = json.loads(res.text)
        order_id = res_json['data']['_id']
        order_id_list = [order_id]
        # update_list = rd.load_yaml_value(yaml_path,'ids','order')
        # update_list.append(order_id)
        wd.write_yaml(yaml_path,'ids','order',order_id_list)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)
        return order_id

        #回款记录中预置若干条数据
    def insert_huikuanjilu_data(self,order_id):
        func_name = sys._getframe().f_code.co_name
        i = 3    #加几条数据
        for i in range(0,i):
            f_list=list(func_name)
            f_list+=str(i)
            func_names = "".join(f_list)
            csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('merge.yaml', func_names)
            a = RestClient(rooturl)
            data = yamlvalue['data']
            data['dingdanmingcheng']=order_id
            res = a.request(url=csurl, method=method, json = data, headers=headers)
            res_json = json.loads(res.text)
            huikuanjilu_id = res_json['data']['_id']
            update_list = rd.load_yaml_value(yaml_path, 'ids', 'huikuanjilu')
            update_list.append(huikuanjilu_id)
            wd.write_yaml(yaml_path, 'ids', 'huikuanjilu', update_list)
            check_codes_msg(res, yamlvalue, mainkey)
            check_datas(res, yamlvalue)



    @allure.story("归集增加源过滤条件")
    def test008_add_source_condition(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('merge.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, json=yamlvalue['data'], headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)


    @allure.story("归集增加目标过滤条件")
    def test009_add_target_condition(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('merge.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, json=yamlvalue['data'], headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("归集求和立即执行")
    def test010_merge_sum(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('merge.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, json=yamlvalue['data'], headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)
        Test_merge.insert_order_data(self)
        order_list = rd.load_yaml_value(yaml_path, 'ids', 'order')
        order_id = order_list[0]
        Test_merge.insert_huikuanjilu_data(self,order_id)

    @allure.story("核实归集结果")
    def test011_merge_result(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('merge.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, json=yamlvalue['data'], headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        pytest.assume('"yihuikuanjine":"77"' in res.text)

    def delete_datas(self,module_name,id):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('merge.yaml', func_name)
        a = RestClient(rooturl)
        csurl = f'{csurl}/{module_name}/{id}'
        res = a.request(url=csurl, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)

    def test_012_delete_all_datas(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('merge.yaml', func_name)
        delete_data_id = rd.load_yaml_value(yaml_path, 'ids', 'order')
        for a in delete_data_id:
            Test_merge.delete_datas(self,'order',a)
        delete_data_id = rd.load_yaml_value(yaml_path, 'ids', 'huikuanjilu')
        for a in delete_data_id:
            Test_merge.delete_datas(self,'huikuanjilu',a)

        #清空删除id数据，方便下次写入
        wd.write_yaml(yaml_path, 'ids', 'order', [])
        wd.write_yaml(yaml_path, 'ids', 'huikuanjilu', [])