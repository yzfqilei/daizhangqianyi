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
@allure.feature("指定字段值")
class TestAssignFieldValues(object):
    @allure.story("指定字段值新增（订单 -- 备注）")
    def test01(self):
        """指定字段值新增（订单 -- 备注）"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("assign-field-values.yaml",
                                                                               "指定字段值新增（订单 -- 备注）")
        r = a.request(csurl, method, json=yamlvalue['data'], headers=head)
        setattr(result, 'module_dingdan', json.loads(r.text)['data']['id'])
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("指定字段值目标模块查询")
    def test02(self):
        """指定字段值目标模块查询"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("assign-field-values.yaml",
                                                                               "指定字段值目标模块查询")
        r = a.request(csurl, method, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("指定字段值数据分页查询")
    def test03(self):
        """指定字段值数据分页查询"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("assign-field-values.yaml",
                                                                               "指定字段值数据分页查询")
        r = a.request(csurl, method, params=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("指定字段值目标模块查询（开票申请）")
    def test04(self):
        """指定字段值目标模块查询（开票申请）"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("assign-field-values.yaml",
                                                                               "指定字段值目标模块查询（开票申请）")
        r = a.request(csurl, method, params=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("指定字段值目标模块字段查询（开票申请 -- 开票金额）")
    def test05(self):
        """指定字段值目标模块字段查询（开票申请 -- 开票金额）"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("assign-field-values.yaml",
                                                                               "指定字段值目标模块字段查询（开票申请 -- 开票金额）")
        r = a.request(csurl, method, params=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("指定字段值目标模块详情（开票申请）")
    def test06(self):
        """指定字段值目标模块详情（开票申请）"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("assign-field-values.yaml",
                                                                               "指定字段值目标模块详情（开票申请）")
        r = a.request(csurl, method, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("指定字段值目标模块删除（订单）")
    def test07(self):
        """指定字段值目标模块删除（订单）"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("assign-field-values.yaml",
                                                                               "指定字段值目标模块删除（订单）")
        module_id = getattr(result, 'module_dingdan')
        data1 = [module_id]
        r = a.request(csurl, method, json=data1, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)

    @allure.story("指定字段值触发条件修改（开票申请）")
    def test08(self):
        """指定字段值触发条件修改（开票申请）"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("assign-field-values.yaml",
                                                                               "指定字段值触发条件修改（开票申请）")
        r = a.request(csurl, method, json=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)
