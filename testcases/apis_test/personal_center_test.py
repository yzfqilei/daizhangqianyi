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
@allure.feature("模块管理")
class TestPersonalCenter(object):
    @allure.story("test_company_infor001")
    def test01(self):
        """test_company_infor001"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("personal_center.yaml", "test_company_infor001")
        r = a.request(csurl, method, headers=head)
        convert_json_to_yaml(r.text, yaml_path, mainkey)
        # check_codes_msg(r, yamlvalue, mainkey)
        # check_datas(r, yamlvalue)

    @allure.story("test_user_infor002")
    def test02(self):
        """test_user_infor002"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("personal_center.yaml", "test_user_infor002")
        r = a.request(csurl, method, headers=head)
        convert_json_to_yaml(r.text, yaml_path, mainkey)
        # check_codes_msg(r, yamlvalue, mainkey)
        # check_datas(r, yamlvalue)

    @allure.story("test_modify_password003")
    def test03(self):
        """test_modify_password003"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("personal_center.yaml", "test_modify_password003")
        r = a.request(csurl, method, json=yamlvalue['data'], headers=head)
        convert_json_to_yaml(r.text, yaml_path, mainkey)
        # check_codes_msg(r, yamlvalue, mainkey)

    @allure.story("test_modify_password003")
    def test03(self):
        """test_modify_password003"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("personal_center.yaml", "test_modify_password003")
        r = a.request(csurl, method, json=yamlvalue['data'], headers=head)
        convert_json_to_yaml(r.text, yaml_path, mainkey)
        # check_codes_msg(r, yamlvalue, mainkey)
