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
result = result_base.ResultBase()
rooturl = get_root_url.get_root_urls()


@allure.feature("首页面板及图表测试用例")
class TestPanel(object):
    @pytest.mark.aaa
    @allure.story("首页新增面板")
    def test01(self):
        """首页新增面板"""
        csurl, method, head, yamlvalue, yaml_path, check_keys = get_common_params("panel.yaml", "首页新增面板")
        a = RestClient(rooturl)
        r = a.request(csurl, method, json=yamlvalue['data'], headers=head)
        check_codes_msg(r, yamlvalue)
        check_datas(r, yamlvalue, check_keys)

    @pytest.mark.aaa
    @allure.story("首页查看面板")
    def test02(self):
        """首页查看面板"""
        csurl, method, head, yamlvalue, yaml_path, check_keys = get_common_params("panel.yaml", "首页查看面板")
        a = RestClient(rooturl)
        r = a.request(csurl, method, headers=head)
        rjson = json.loads(r.text)
        panelid = rjson['data'][0]['id']
        setattr(result, 'panelid', panelid)
        wd.write_yaml(yaml_path, "首页修改面板", "data", {
            "crmPanelAddOrEditDtoList": [{"id": "%s" % panelid, "panelName": "测试面板", "sequence": 0}]})
        wd.write_yaml(yaml_path, "首页删除面板", "data", panelid)
        check_codes_msg(r, yamlvalue)
        check_datas(r, yamlvalue, check_keys)

    @pytest.mark.aaa
    @allure.story("首页新增卡片")
    def test03(self,renyuan_moduleid):
        """首页新增卡片"""
        csurl, method, head, yamlvalue, yaml_path, check_keys = get_common_params("component.yaml", "首页新增卡片")
        a = RestClient(rooturl)
        data = {"from": 1, "id": 0, "panelId": "%s" % getattr(result, 'panelid'), "panelLocation": 0,
                "componentType": 1,
                "componentName": "测试卡片", "conditionType": 1, "dataModuleName": "人员", "dataModuleCode": "sysUser",
                "dataModuleId": "%s" % renyuan_moduleid, "conditions": [],
                "statisticsFields": [{"aggregator": "count", "moduleFieldCode": ""}]}
        r = a.request(csurl, method, json=data, headers=head)
        check_codes_msg(r, yamlvalue)
        setattr(result, 'component_id_kp', json.loads(r.text)['data'])

    @allure.story("首页查看卡片")
    def test04(self):
        """首页查看卡片"""
        csurl, method, head, yamlvalue, yaml_path, check_keys = get_common_params("component.yaml", "首页查看卡片")
        a = RestClient(rooturl)
        data = {"componentId": "%s" % getattr(result, 'component_id_kp'), "from": 1,
                "panelId": "%s" % getattr(result, 'panelid')}
        r = a.request(csurl, method, json=data, headers=head)
        check_codes_msg(r, yamlvalue)
        check_datas(r, yamlvalue, check_keys)

    @allure.story("首页修改面板")
    def test05(self):
        """首页修改面板"""
        csurl, method, head, yamlvalue, yaml_path, check_keys = get_common_params("panel.yaml", "首页修改面板")
        a = RestClient(rooturl)
        r = a.request(csurl, method, json=yamlvalue['data'], headers=head)
        check_codes_msg(r, yamlvalue)
        check_datas(r, yamlvalue, check_keys)

    @allure.story("首页删除卡片")
    def test06(self):
        """首页删除卡片"""
        csurl, method, head, yamlvalue, yaml_path, check_keys = get_common_params("component.yaml", "首页删除卡片")
        a = RestClient(rooturl)
        param = {"componentId": getattr(result, 'component_id_kp'), "location": 0, "panelId": getattr(result,
                                                                                                      'panelid')}
        r = a.request(csurl, method, params=param, headers=head)
        check_codes_msg(r, yamlvalue)

    @allure.story("首页新增图表")
    def test07(self,renyuan_moduleid):
        """首页新增图表"""
        csurl, method, head, yamlvalue, yaml_path, check_keys = get_common_params("component.yaml", "首页新增图表")
        a = RestClient(rooturl)
        data = {"from": 1, "id": 0, "panelId": "%s" % getattr(result, 'panelid'), "panelLocation": 8,
                "componentType": 2,
                "dataModuleCode": "sysUser", "componentName": "人员",
                "dataModuleId": "%s" % renyuan_moduleid}
        r = a.request(csurl, method, json=data, headers=head)
        check_codes_msg(r, yamlvalue)
        setattr(result, 'component_id_tb', json.loads(r.text)['data'])

    @allure.story("首页查看图表")
    def test08(self):
        """首页查看图表"""
        csurl, method, head, yamlvalue, yaml_path, check_keys = get_common_params("component.yaml", "首页查看图表")
        a = RestClient(rooturl)
        r = a.request(csurl + '%s' % getattr(result, 'component_id_tb'), method, headers=head)
        check_codes_msg(r, yamlvalue)
        check_datas(r, yamlvalue, check_keys)

    @allure.story("首页删除图表")
    def test09(self):
        """首页删除图表"""
        csurl, method, head, yamlvalue, yaml_path, check_keys = get_common_params("component.yaml", "首页删除图表")
        a = RestClient(rooturl)
        param = {"componentId": getattr(result, 'component_id_kp'), "location": 8, "panelId": getattr(result,
                                                                                                      'panelid')}
        r = a.request(csurl, method, params=param, headers=head)
        check_codes_msg(r, yamlvalue)

    @allure.story("首页删除面板")
    def test10(self):
        """首页删除面板"""
        csurl, method, head, yamlvalue, yaml_path, check_keys = get_common_params("panel.yaml", "首页删除面板")
        a = RestClient(rooturl)
        r = a.request(csurl + yamlvalue['data'], method, headers=head)
        check_codes_msg(r, yamlvalue)


if __name__ == '__main__':
    pytest.main(["-s", "panel_component_test.py"])
