#!/usr/bin/python
# coding:utf-8
from core.checkresult import check_codes_msg, check_datas
from core.rest_client import RestClient
from common.write_data import WriteFileData
from core.common_params import get_common_params
import json,sys,random
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

@pytest.mark.usefixtures('is_login')
@allure.feature("模块管理测试用例")
class Test_module_manage():
    def test_creat_module001(self):
        #创建模块名，写入yaml
        func_name = sys._getframe().f_code.co_name
        module_name='module'+str(random.randint(1,1000))
        wd.write_yaml('D:\\PycharmProjects\\apistest_crm\\apidata\\module.yaml',func_name,'data',{'code':'','flowType':1,'id': 0,'mainFieldId': 0,'name': module_name})
        wd.write_yaml('D:\\PycharmProjects\\apistest_crm\\apidata\\module.yaml',func_name,'expectresult',{'code': 0,'msg':None,'data':{"tenantId": "10447", "name":module_name}})
        rooturl, csurl, method, headers, yamlvalue, yaml_path, mainkey=get_common_params('module.yaml',func_name)
        a = RestClient(rooturl)
        res = a.request(csurl, method, json=yamlvalue['data'], headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue, ['tenantId','name'])
        #返回模块名称和id用于删除等操作
        res_dir=json.loads(res.text)
        id=res_dir['data']['id']
        return module_name,id

    def test_delete_module002(self):
        #创建模块后返回模块名称和id
        module_name, id=Test_module_manage.test_creat_module001(self)
        func_name = sys._getframe().f_code.co_name
        rooturl, csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('module.yaml', func_name)
        csurl=csurl+id
        a = RestClient(rooturl)
        res = a.request(csurl, method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

