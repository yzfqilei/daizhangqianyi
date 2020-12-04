#!/usr/bin/python
# coding:utf-8


import json
import allure
import pytest
import arrow
from common import path_conf
from core import result_base
from common import get_root_url
from core.rest_client import RestClient
from common.write_data import WriteFileData
from common.convert import convert_json_to_yaml
from core.common_params import get_common_params
from core.checkresult import check_codes_msg, check_datas

#由于大数据没有实时推送每个月数据，该用例暂时搁置

reportpath = path_conf.REPORT_PATH
wd = WriteFileData()
result = result_base.ResultBase()
rooturl = get_root_url.get_root_urls()
a = RestClient(rooturl)
nowt = arrow.now()


@pytest.mark.usefixtures('is_login')
@pytest.mark.usefixtures('pre_company_data')
@allure.feature("模块管理")
class TestCompanyDatas(object):
    @allure.story("查询上个自然月客户数量")
    def test01(self):
        """查询上个自然月客户数量"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("company_datas.yaml", "查询上个自然月客户数量")
        r = a.request(csurl, method, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("查询历史年月客户数量")
    def test02(self):
        """查询历史年月客户数量"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("company_datas.yaml", "查询历史年月客户数量")
        r = a.request(csurl, method, params=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        # check_datas(r, yamlvalue)

    @allure.story("查询当前自然月流失客户明细")
    def test03(self):
        """查询当前自然月流失客户明细"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("company_datas.yaml", "查询当前自然月流失客户明细")
        yamlvalue['data']['date'] = nowt.format("YYYYMM")
        r = a.request(csurl, method, json=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("查询当前自然月流失客户占比")
    def test04(self):
        """查询当前自然月流失客户占比"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("company_datas.yaml", "查询当前自然月流失客户占比")
        yamlvalue['data']['date'] = nowt.format("YYYYMM")
        r = a.request(csurl, method, params=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("查询当前自然月员工价值权重设置")
    def test05(self):
        """查询当前自然月员工价值权重设置"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("company_datas.yaml", "查询当前自然月员工价值权重设置")
        r = a.request(csurl, method, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("判断当前自然月员工价值权重是否提醒维护薪资区间")
    def test06(self):
        """判断当前自然月员工价值权重是否提醒维护薪资区间"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("company_datas.yaml", "判断当前自然月员工价值权重是否提醒维护薪资区间")
        r = a.request(csurl, method, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("保存当前自然月员工价值权重设置")
    def test07(self):
        """保存当前自然月员工价值权重设置"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("company_datas.yaml", "保存当前自然月员工价值权重设置")
        r = a.request(csurl, method, json=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("评估员工价值")
    def test08(self):
        """评估员工价值"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("company_datas.yaml", "评估员工价值")
        r = a.request(csurl, method, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        # check_datas(r, yamlvalue)

    @allure.story("查询评估员工价值列表")
    def test09(self):
        """查询评估员工价值列表"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("company_datas.yaml", "查询评估员工价值列表")
        lnow = nowt.shift(months=-1)
        yamlvalue['data']['evaDate'] = lnow.format("YYYYMM")
        r = a.request(csurl, method, json=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)
