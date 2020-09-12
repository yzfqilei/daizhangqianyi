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

reportpath = path_conf.REPORT_PATH
wd = WriteFileData()
rooturl = get_root_url.get_root_urls()
result = result_base.ResultBase()


@pytest.mark.usefixtures('is_login')
@allure.feature("导航菜单测试用例")
class TestNavigation(object):
    @allure.story("导航菜单内-自定义菜单为空")
    def test01(self, is_login):
        """导航菜单内-自定义菜单为空"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("navigation_menu.yaml",
                                                                               "导航菜单内-自定义菜单为空")
        a = RestClient(rooturl)
        r = a.request(csurl, method, headers=head)
        token = is_login[0]
        token1 = is_login[1]  # token获取
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("导航菜单外-自定义菜单为空")
    def test02(self):
        """导航菜单外-自定义菜单为空"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("navigation_menu.yaml",
                                                                               "导航菜单外-自定义菜单为空")
        a = RestClient(rooturl)
        r = a.request(csurl, method, headers=head)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("新增导航菜单(关联模块，范围全部)")
    def test03(self):
        """新增导航菜单(关联模块，范围全部)"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("navigation_menu.yaml",
                                                                               "新增导航菜单(关联模块，范围全部)")
        a = RestClient(rooturl)
        r = a.request(csurl, method, json=yamlvalue['data'], headers=head)
        dataid = json.loads(r.text)['data']
        check_codes_msg(r, yamlvalue, mainkey)
        wd.write_yaml(yaml_path, "删除导航菜单(关联模块，范围全部)", "data", dataid)  # 新增模块id写入删除用例参数中
        wd.write_yaml(yaml_path, "导航菜单详情查看(关联模块，范围全部)", "data", {"menuId": '%s' % dataid})  # 新增模块id写入导航详情参数中

    @allure.story("新增重复的导航菜单(关联模块，范围全部)")
    def test04(self):
        """新增重复的导航菜单(关联模块，范围全部)"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("navigation_menu.yaml",
                                                                               "新增重复的导航菜单(关联模块，范围全部)")
        a = RestClient(rooturl)
        r = a.request(csurl, method, json=yamlvalue['data'], headers=head)
        check_codes_msg(r, yamlvalue, mainkey)

    @allure.story("导航菜单内-自定义菜单展示(关联模块，范围全部)")
    def test05(self):
        """导航菜单内-自定义菜单展示(关联模块，范围全部)"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("navigation_menu.yaml",
                                                                               "导航菜单内-自定义菜单展示(关联模块，范围全部)")
        a = RestClient(rooturl)
        r = a.request(csurl, method, headers=head)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("导航菜单外-自定义菜单展示(关联模块，范围全部)")
    def test06(self):
        """导航菜单外-自定义菜单展示(关联模块，范围全部)"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("navigation_menu.yaml",
                                                                               "导航菜单外-自定义菜单展示(关联模块，范围全部)")
        a = RestClient(rooturl)
        r = a.request(csurl, method, headers=head)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("导航菜单详情查看(关联模块，范围全部)")
    def test07(self):
        """导航菜单详情查看(关联模块，范围全部)"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("navigation_menu.yaml",
                                                                               "导航菜单详情查看(关联模块，范围全部)")
        a = RestClient(rooturl)
        r = a.request(csurl, method, params=yamlvalue['data'], headers=head)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("删除导航菜单(关联模块，范围全部)")
    def test08(self):
        """删除导航菜单(关联模块，范围全部)"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("navigation_menu.yaml",
                                                                               "删除导航菜单(关联模块，范围全部)")
        a = RestClient(rooturl)
        r = a.request(csurl + yamlvalue['data'], method, headers=head)
        check_codes_msg(r, yamlvalue, mainkey)


if __name__ == '__main__':
    pytest.main(['-v', 'navigation_test.py::TestNavigation::test01'])
