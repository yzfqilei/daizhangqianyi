# !/usr/bin/python
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
a = RestClient(rooturl)


@allure.feature("统计模块测试")
class TestStatistics(object):
    @allure.story("新增统计目录")
    def test01(self):
        """新增统计目录"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("statistics.yaml", "新增统计目录")
        r = a.request(csurl, method, json=yamlvalue['data'], headers=head)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("查看统计目录")
    def test02(self):
        """查看统计目录"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("statistics.yaml", "查看统计目录")
        r = a.request(csurl, method, headers=head)
        setattr(result, 'menuid', json.loads(r.text)['data'][0]['id'])
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("新增环形图")
    def test03(self, renyuan_moduleid):
        """新增环形图"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("statistics.yaml", "新增环形图")
        data = {"statisticsMenuId": "%s" % getattr(result, 'menuid'), "componentName": "环形图",
                "dataModuleCode": "sysUser",
                "componentType": 3, "statisticsMeasure0": ["人员.用户名", "用户名", "username", "sysUser", 1],
                "fields": ["人员.总数,总数,sysUser,人员,sysUser"], "statisticsFields": [
                {"aggregator": "count", "moduleFieldCode": "", "moduleFieldName": "", "moduleCode": "sysUser"}],
                "statisticsMeasure": [
                    {"moduleCode": "sysUser", "moduleFieldName": "用户名", "moduleFieldCode": "username", "fieldType": 1,
                     "subjectLevel": ""}], "conditionType": 1, "conditions": [], "from": 0,
                "dataModuleId": "%s" % renyuan_moduleid, "relatedDataModuleId": "", "panelId": "", "panelLocation": "",
                "id": ""}
        r = a.request(csurl, method, json=data, headers=head)
        setattr(result, 'huanxingid', json.loads(r.text)['data'])
        check_codes_msg(r, yamlvalue, mainkey)

    @allure.story("环形图预览")
    def test04(self, renyuan_moduleid):
        """环形图预览"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("statistics.yaml", "环形图预览")
        data = {"statisticsMenuId": "%s" % getattr(result, 'menuid'), "componentName": "环形图",
                "dataModuleCode": "sysUser",
                "componentType": 3, "statisticsMeasure0": ["人员.用户名", "用户名", "username", "sysUser", 1],
                "fields": ["人员.总数,总数,sysUser,人员,sysUser"], "statisticsFields": [
                {"aggregator": "count", "moduleFieldCode": "", "moduleFieldName": "", "moduleCode": "sysUser"}],
                "statisticsMeasure": [
                    {"moduleCode": "sysUser", "moduleFieldName": "用户名", "moduleFieldCode": "username", "fieldType": 1,
                     "subjectLevel": ""}], "conditionType": 1, "conditions": [], "from": 0,
                "dataModuleId": "%s" % renyuan_moduleid, "relatedDataModuleId": "", "panelId": "", "panelLocation": "",
                "id": ""}
        r = a.request(csurl, method, json=data, headers=head)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("查看环形图")
    def test05(self):
        """查看环形图"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("statistics.yaml", "查看环形图")
        data = {"componentId": "%s" % getattr(result, 'huanxingid')}
        r = a.request(csurl, method, json=data, headers=head)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("图形列表")
    def test06(self):
        """图形列表"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("statistics.yaml", "图形列表")
        r = a.request(csurl, method, headers=head)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("删除环形图")
    def test07(self):
        """删除环形图"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("statistics.yaml", "删除环形图")
        r = a.request(csurl + getattr(result, 'menuid') + '/' + getattr(result, 'huanxingid') + '/false', method,
                      headers=head)
        check_codes_msg(r, yamlvalue, mainkey)

    @allure.story("新增柱状图")
    def test08(self, renyuan_moduleid):
        """新增柱状图"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("statistics.yaml", "新增柱状图")
        data = {"statisticsMenuId": "%s" % getattr(result, 'menuid'), "componentName": "柱状图",
                "dataModuleCode": "sysUser",
                "relatedDataModuleCode": "", "componentType": 4, "statisticsLevelSort": 1,
                "statisticsMeasure1": ["人员.用户名", "用户名", "username", "sysUser", 1],
                "fields": ["人员.总数,总数,sysUser,人员,sysUser"], "statisticsFields": [
                {"aggregator": "count", "moduleFieldCode": "", "moduleFieldName": "", "moduleCode": "sysUser"}],
                "statisticsMeasure": [
                    {"moduleCode": "sysUser", "moduleFieldName": "用户名", "moduleFieldCode": "username", "fieldType": 1,
                     "subjectLevel": 0}], "conditionType": 1, "conditions": [], "from": 0,
                "dataModuleId": "%s" % renyuan_moduleid, "relatedDataModuleId": "", "panelId": "", "panelLocation": "",
                "id": ""}
        r = a.request(csurl, method, json=data, headers=head)
        setattr(result, 'zhuzhuangid', json.loads(r.text)['data'])
        check_codes_msg(r, yamlvalue, mainkey)

    @allure.story("柱状图预览")
    def test09(self, renyuan_moduleid):
        """柱状图预览"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("statistics.yaml", "柱状图预览")
        data = {"statisticsMenuId": "%s" % getattr(result, 'menuid'), "componentName": "柱状图",
                "dataModuleCode": "sysUser",
                "relatedDataModuleCode": "", "componentType": 4, "statisticsLevelSort": 1,
                "statisticsMeasure1": ["人员.用户名", "用户名", "username", "sysUser", 1],
                "fields": ["人员.总数,总数,sysUser,人员,sysUser"], "statisticsFields": [
                {"aggregator": "count", "moduleFieldCode": "", "moduleFieldName": "", "moduleCode": "sysUser"}],
                "statisticsMeasure": [
                    {"moduleCode": "sysUser", "moduleFieldName": "用户名", "moduleFieldCode": "username", "fieldType": 1,
                     "subjectLevel": 0}], "conditionType": 1, "conditions": [], "from": 0,
                "dataModuleId": "%s" % renyuan_moduleid, "relatedDataModuleId": "", "panelId": "", "panelLocation": "",
                "id": ""}
        r = a.request(csurl, method, json=data, headers=head)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("查看柱状图")
    def test10(self):
        """查看柱状图"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("statistics.yaml", "查看柱状图")
        data = {"componentId": "%s" % getattr(result, 'zhuzhuangid')}
        r = a.request(csurl, method, json=data, headers=head)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("删除柱状图")
    def test11(self):
        """删除柱状图"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("statistics.yaml", "删除柱状图")
        r = a.request(csurl + getattr(result, 'menuid') + '/' + getattr(result, 'zhuzhuangid') + '/false', method,
                      headers=head)
        check_codes_msg(r, yamlvalue, mainkey)

    @allure.story("新增线性图")
    def test12(self, renyuan_moduleid):
        """新增线性图"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("statistics.yaml", "新增线性图")
        data = {"statisticsMenuId": "%s" % getattr(result, 'menuid'), "componentName": "线性图",
                "dataModuleCode": "sysUser",
                "componentType": 5, "statisticsMeasure0": ["人员.用户名", "用户名", "username", "sysUser", 1],
                "fields": ["人员.总数,总数,sysUser,人员,sysUser"], "statisticsFields": [
                {"aggregator": "count", "moduleFieldCode": "", "moduleFieldName": "", "moduleCode": "sysUser"}],
                "statisticsMeasure": [
                    {"moduleCode": "sysUser", "moduleFieldName": "用户名", "moduleFieldCode": "username", "fieldType": 1,
                     "subjectLevel": ""}], "conditionType": 1, "conditions": [], "from": 0,
                "dataModuleId": "%s" % renyuan_moduleid, "relatedDataModuleId": "", "panelId": "", "panelLocation": "",
                "id": ""}
        r = a.request(csurl, method, json=data, headers=head)
        setattr(result, 'xianxingid', json.loads(r.text)['data'])
        check_codes_msg(r, yamlvalue, mainkey)

    @allure.story("线性图预览")
    def test13(self, renyuan_moduleid):
        """线性图预览"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("statistics.yaml", "线性图预览")
        data = {"statisticsMenuId": "%s" % getattr(result, 'menuid'), "componentName": "线性图",
                "dataModuleCode": "sysUser",
                "componentType": 5, "statisticsMeasure0": ["人员.用户名", "用户名", "username", "sysUser", 1],
                "fields": ["人员.总数,总数,sysUser,人员,sysUser"], "statisticsFields": [
                {"aggregator": "count", "moduleFieldCode": "", "moduleFieldName": "", "moduleCode": "sysUser"}],
                "statisticsMeasure": [
                    {"moduleCode": "sysUser", "moduleFieldName": "用户名", "moduleFieldCode": "username", "fieldType": 1,
                     "subjectLevel": ""}], "conditionType": 1, "conditions": [], "from": 0,
                "dataModuleId": "%s" % renyuan_moduleid, "relatedDataModuleId": "", "panelId": "", "panelLocation": "",
                "id": ""}
        r = a.request(csurl, method, json=data, headers=head)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("查看线性图")
    def test14(self):
        """查看线性图"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("statistics.yaml", "查看线性图")
        data = {"componentId": "%s" % getattr(result, 'xianxingid')}
        r = a.request(csurl, method, json=data, headers=head)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("删除线性图")
    def test15(self):
        """删除线性图"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("statistics.yaml", "删除线性图")
        r = a.request(csurl + getattr(result, 'menuid') + '/' + getattr(result, 'xianxingid') + '/false', method,
                      headers=head)
        check_codes_msg(r, yamlvalue, mainkey)

    @allure.story("删除统计目录")
    def test16(self):
        """删除目统计目录"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("statistics.yaml", "删除统计目录")
        r = a.request(csurl + getattr(result, 'menuid'), method, headers=head)
        check_codes_msg(r, yamlvalue, mainkey)
