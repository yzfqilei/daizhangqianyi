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
class TestModuleManage(object):
    @allure.story("添加模块")
    def test01(self):
        """添加模块"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_manage.yaml", "添加模块")
        r = a.request(csurl, method, json=yamlvalue['data'], headers=head)
        setattr(result, 'update_dict', json.loads(r.text)['data'])
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    def test02(self):
        """修改模块名称（测试模块1）"""
        data = getattr(result, 'update_dict')
        data['name'] = '测试模块1'
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_manage.yaml", "修改模块名称（测试模块1）")
        r = a.request(csurl, method, json=data, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)

    @allure.story("查看模块列表")
    def test03(self):
        """查看模块列表"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_manage.yaml", "查看模块列表")
        r = a.request(csurl, method, params=yamlvalue['data'], headers=head)
        setattr(result, 'id', json.loads(r.text)['data'][-1]['id'])
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("查看模块详情")
    def test04(self):
        """查看模块详情"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_manage.yaml", "查看模块详情")
        id = {'id': getattr(result, 'id')}
        r = a.request(csurl, method, params=id, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("添加功能")
    def test05(self):
        """添加功能"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_manage.yaml", "添加功能")
        data = {"moduleId": "%s" % getattr(result, 'id'), "name": "测试功能", "id": None}
        r = a.request(csurl, method, json=data, headers=head)
        setattr(result, 'funcid', json.loads(r.text)['data']['id'])
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("查看功能列表")
    def test06(self):
        """查看功能列表"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_manage.yaml", "查看功能列表")
        id = {"moduleId": getattr(result, 'id')}
        r = a.request(csurl, method, params=id, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("修改功能名称")
    def test07(self):
        """修改功能名称"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_manage.yaml", "修改功能名称")
        data = {"moduleId": "%s" % getattr(result, 'id'), "name": "测试功能1", "id": "%s" % getattr(result, 'funcid')}
        r = a.request(csurl, method, json=data, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("添加字段（单行文本）")
    def test08(self):
        """添加字段（单行文本）"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_manage.yaml", "添加字段（单行文本）")
        data = {"moduleId": "%s" % getattr(result, 'id'), "name": "单行文本", "code": "", "type": 0, "componentId": 1,
                "placeholder": "", "description": "", "layout": 0, "required": False, "repeated": False,
                "sequence": 104, "extendJson": {"default": "", "length": 18}, "onlyRead": 0}
        r = a.request(csurl, method, json=data, headers=head)
        setattr(result, 'ziduanxinxi', json.loads(r.text)['data'])
        setattr(result, 'fieldid', json.loads(r.text)['data']['id'])
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("查看字段列表")
    def test09(self):
        """查看字段列表"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_manage.yaml", "查看字段列表")
        data = {'moduleId': getattr(result, 'id')}
        r = a.request(csurl, method, params=data, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("保存字段布局")
    def test10(self):
        """保存字段布局"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_manage.yaml", "保存字段布局")
        fielfinfo = getattr(result, 'ziduanxinxi')
        fielfinfo1 = json.dumps(fielfinfo, ensure_ascii=False)
        data1 = {"funcId": "%s" % getattr(result, 'funcid'),
                 "pageLayout": "[{\"title\":\"11\",\"expend\":true,\"children\":[%s]}]" % fielfinfo1}
        r = a.request(csurl, method, json=data1, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        # check_datas(r, yamlvalue)

    @allure.story("删除字段布局")
    def test11(self):
        """删除字段布局"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_manage.yaml", "删除字段布局")
        data1 = {"funcId": "%s" % getattr(result, 'funcid'),
                 "pageLayout": "[{\"title\":\"11\",\"expend\":true,\"children\":[]}]"}
        r = a.request(csurl, method, json=data1, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        # check_datas(r, yamlvalue)

    @allure.story("删除新增字段（单行文本）")
    def test12(self):
        """删除新增字段（单行文本）"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_manage.yaml", "删除新增字段（单行文本）")
        fieldid = getattr(result, 'fieldid')
        r = a.request(csurl + fieldid, method, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("删除新增功能（测试功能）")
    def test13(self):
        """删除新增功能（测试功能）"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_manage.yaml", "删除新增功能（测试功能）")
        data = {"id": "%s" % getattr(result, 'funcid'), "moduleId": "%s" % getattr(result, 'id'), "name": ""}
        r = a.request(csurl, method, json=data, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        # check_datas(r, yamlvalue)

    @allure.story("删除新增模块（测试模块1）")
    def test14(self):
        """删除新增模块（测试模块1）"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_manage.yaml", "删除新增模块（测试模块1）")
        mid = getattr(result, 'id')
        r = a.request(csurl + mid, method, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("查看模块列表（tree）")
    def test15(self):
        """查看模块列表（tree）"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_manage.yaml", "查看模块列表（tree）")
        r = a.request(csurl, method, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)


