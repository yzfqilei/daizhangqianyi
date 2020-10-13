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
@allure.feature("客户数据同步")
class TestSyncCustomer(object):
    @allure.story("客户数据同步")
    def test01(self):
        """客户数据同步"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("sync_customer.yaml", "客户数据同步")
        r = a.request(csurl, method, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        # check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("客户数据查询")
    def test02(self):
        """客户数据查询"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("sync_customer.yaml", "客户数据查询")
        r = a.request(csurl, method, json=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)
