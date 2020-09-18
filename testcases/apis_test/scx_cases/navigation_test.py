#!/usr/bin/python
# coding:utf-8

from core.checkresult import check_codes_msg, check_datas
from core.rest_client import RestClient
from common.write_data import WriteFileData
from core.common_params import get_common_params
import json
import allure
import pytest
from common import path_conf
from core import result_base
from common import get_root_url
from common.convert import convert_json_to_yaml


reportpath = path_conf.REPORT_PATH
wd = WriteFileData()
rooturl = get_root_url.get_root_urls()
result = result_base.ResultBase()
a = RestClient(rooturl)


@pytest.mark.usefixtures('is_login')
@allure.feature("导航菜单测试用例")
class TestNavigation(object):
    @allure.story("新增导航菜单(关联模块，范围全部)")
    def test01(self, customer_moduleid):
        """新增导航菜单(关联模块，范围全部)"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("navigation_menu.yaml",
                                                                               "新增导航菜单(关联模块，范围全部)")
        data = {"parentId": "0", "scopeType": 0, "menuName": "测试", "menuType": 0, "moduleId": "%s" % customer_moduleid,
                "moduleCode": "customer"}
        r = a.request(csurl, method, json=data, headers=head)
        setattr(result, 'menuid', json.loads(r.text)['data'])
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)

    @allure.story("新增重复的导航菜单(关联模块，范围全部)")
    def test02(self, customer_moduleid):
        """新增重复的导航菜单(关联模块，范围全部)"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("navigation_menu.yaml",
                                                                               "新增重复的导航菜单(关联模块，范围全部)")
        data = {"parentId": "0", "scopeType": 0, "menuName": "测试", "menuType": 0, "moduleId": "%s" % customer_moduleid,
                "moduleCode": "customer"}
        r = a.request(csurl, method, json=data, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)

    @allure.story("导航菜单内-自定义菜单展示(关联模块，范围全部)")
    def test03(self):
        """导航菜单内-自定义菜单展示(关联模块，范围全部)"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("navigation_menu.yaml",
                                                                               "导航菜单内-自定义菜单展示(关联模块，范围全部)")
        r = a.request(csurl, method, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("导航菜单外-自定义菜单展示(关联模块，范围全部)")
    def test04(self):
        """导航菜单外-自定义菜单展示(关联模块，范围全部)"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("navigation_menu.yaml",
                                                                               "导航菜单外-自定义菜单展示(关联模块，范围全部)")
        r = a.request(csurl, method, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("导航菜单详情查看(关联模块，范围全部)")
    def test05(self):
        """导航菜单详情查看(关联模块，范围全部)"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("navigation_menu.yaml",
                                                                               "导航菜单详情查看(关联模块，范围全部)")
        data = {'menuId': getattr(result, 'menuid')}
        r = a.request(csurl, method, params=data, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("删除导航菜单(关联模块，范围全部)")
    def test06(self):
        """删除导航菜单(关联模块，范围全部)"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("navigation_menu.yaml",
                                                                               "删除导航菜单(关联模块，范围全部)")
        r = a.request(csurl + getattr(result, 'menuid'), method, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)


if __name__ == '__main__':
    pytest.main(['-v', 'navigation_test.py::TestNavigation::test01'])
