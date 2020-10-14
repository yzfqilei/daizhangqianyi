#!/usr/bin/python
# coding:utf-8


import json
import allure
import pytest
from common import path_conf
from core import result_base
from common import get_root_url
from core.rest_client import RestClient
from common.write_data import WriteFileData
from common.convert import convert_json_to_yaml
from core.common_params import get_common_params
from core.checkresult import check_codes_msg, check_datas

reportpath = path_conf.REPORT_PATH
wd = WriteFileData()
result = result_base.ResultBase()
rooturl = get_root_url.get_root_urls()
a = RestClient(rooturl)


@pytest.mark.usefixtures('is_login')
@allure.feature("设置关联模块")
class TestAssociation(object):
    @allure.story("查询关联模块（客户模块 -- 测试用户）")
    def test01(self):
        """查询关联模块（客户模块 -- 测试用户）"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("association.yaml",
                                                                               "查询关联模块（客户模块 -- 测试用户）")
        r = a.request(csurl, method, params=yamlvalue['data'], headers=head)
        setattr(result, 'association_data', json.loads(r.text)['data'])
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("添加关联模块显示（跟进记录）")
    def test02(self):
        """添加关联模块显示（跟进记录）"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("association.yaml", "添加关联模块显示（跟进记录）")
        association_d = getattr(result, 'association_data')
        association_d[0]['checked'] = 1
        association_d[0]['value'] = "跟进记录"
        association_d[1]['value'] = "订单"
        association_d[2]['value'] = "工商注册"
        association_d[3]['value'] = "代理记账"
        association_d[4]['value'] = "回款记录"
        association_d[5]['value'] = "开票申请"
        association_d[6]['value'] = "联系人"
        r = a.request(csurl, method, json=association_d, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        # check_datas(r, yamlvalue)

    @allure.story("取消关联模块显示（跟进记录）")
    def test03(self):
        """取消关联模块显示（跟进记录）"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("association.yaml", "取消关联模块显示（跟进记录）")
        association_d = getattr(result, 'association_data')
        association_d[0]['checked'] = 0
        association_d[0]['value'] = "跟进记录"
        association_d[1]['value'] = "订单"
        association_d[2]['value'] = "工商注册"
        association_d[3]['value'] = "代理记账"
        association_d[4]['value'] = "回款记录"
        association_d[5]['value'] = "开票申请"
        association_d[6]['value'] = "联系人"
        r = a.request(csurl, method,json=association_d, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        # check_datas(r, yamlvalue)

    @allure.story("再次查询关联模块（客户模块 -- 测试用户）")
    def test04(self):
        """再次查询关联模块（客户模块 -- 测试用户）"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("association.yaml",
                                                                               "再次查询关联模块（客户模块 -- 测试用户）")
        r = a.request(csurl, method, params=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)
