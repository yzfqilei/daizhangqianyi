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
@pytest.mark.usefixtures('insert_module_data')
@allure.feature("模块数据详细")
class TestModuleDataDetails(object):
    @allure.story("字段排序查询")
    def test01(self):
        """字段排序查询"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_data_details.yaml", "字段排序查询")
        r = a.request(csurl, method, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("字段排序修改保存")
    def test02(self):
        """字段排序修改保存"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_data_details.yaml", "字段排序修改保存")
        r = a.request(csurl, method, json=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("数据列表分页查询（100页）")
    def test03(self):
        """数据列表分页查询（100页）"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_data_details.yaml",
                                                                               "数据列表分页查询（100页）")
        r = a.request(csurl, method, json=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("模块id查询（跟进记录）")
    def test04(self):
        """模块id查询（跟进记录）"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_data_details.yaml",
                                                                               "模块id查询（跟进记录）")
        r = a.request(csurl, method, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("模块数据权限查询（新增、查看）")
    def test05(self):
        """模块数据权限查询（新增、查看）"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_data_details.yaml",
                                                                               "模块数据权限查询（新增、查看）")
        r = a.request(csurl, method, params=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        # check_datas(r, yamlvalue)

    @allure.story("第一条数据流程id查询")
    def test06(self, insert_module_data):
        """第一条数据流程id查询"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_data_details.yaml",
                                                                               "第一条数据流程id查询")
        r = a.request(csurl + insert_module_data[0], method, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("表单查看布局查询")
    def test07(self):
        """表单查看布局查询"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_data_details.yaml", "表单查看布局查询")
        r = a.request(csurl, method, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("表单第一条数据各字段值查询")
    def test08(self, insert_module_data):
        """表单第一条数据各字段值查询"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_data_details.yaml",
                                                                               "表单第一条数据各字段值查询")
        r = a.request(csurl + insert_module_data[0], method, params=yamlvalue, headers=head)
        setattr(result, 'module_data', json.loads(r.text)['data'])
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("表单编辑布局查询")
    def test09(self):
        """表单编辑布局查询"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_data_details.yaml", "表单编辑布局查询")
        r = a.request(csurl, method, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("第一条数据编辑保存")
    def test10(self):
        """第一条数据编辑保存"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_data_details.yaml", "第一条数据编辑保存")
        jdata = getattr(result, 'module_data')
        jdata['lianxiren'] = '张三1'  # 修改联系人字段并保存
        r = a.request(csurl, method, json=jdata, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("第一条数据的流程状态查询")
    def test11(self, insert_module_data):
        """第一条数据的流程状态查询"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_data_details.yaml",
                                                                               "第一条数据的流程状态查询")
        r = a.request(csurl + insert_module_data[0], method, headers=head)
        setattr(result, 'procCode', json.loads(r.text)['data'][0]['procCode'])
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("第一条数据发起流程")
    def test12(self, insert_module_data):
        """第一条数据发起流程"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_data_details.yaml", "第一条数据发起流程")
        yamlvalue['data']['businessId'] = insert_module_data[0]
        yamlvalue['data']['procDefId'] = getattr(result, 'procCode')
        r = a.request(csurl, method, json=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        # check_datas(r, yamlvalue)

    @allure.story("第一条数据的流程状态id查询")
    def test13(self, insert_module_data):
        """第一条数据的流程状态id查询"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_data_details.yaml",
                                                                               "第一条数据的流程状态id查询")
        r = a.request(csurl + insert_module_data[0], method, headers=head)
        setattr(result, 'proc_datas', json.loads(r.text)['data'][0])
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("第一条数据的第一个流程状态详细")
    def test14(self):
        """第一条数据的第一个流程状态详细"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_data_details.yaml",
                                                                               "第一条数据的第一个流程状态详细")
        procInstId = getattr(result, 'proc_datas')['procInstId']
        r = a.request(csurl + procInstId, method, headers=head)
        setattr(result, 'taskId_first', json.loads(r.text)['data']['list'][0]['taskId'])
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("第一条数据的第一个流程流程转办taskid查询")
    def test15(self):
        """第一条数据的第一个流程流程转办taskid查询"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_data_details.yaml",
                                                                               "第一条数据的第一个流程流程转办taskid查询")
        taskId_first = getattr(result, 'taskId_first')
        pdata = [taskId_first]
        r = a.request(csurl, method, json=pdata, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("第一条数据的第一个流程流程转办（给测试人员）")
    def test16(self):
        """第一条数据的第一个流程流程转办（给测试人员）"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_data_details.yaml",
                                                                               "第一条数据的第一个流程流程转办（给测试人员）")
        yamlvalue['data'][0]['taskId'] = getattr(result, 'taskId_first')
        r = a.request(csurl, method, json=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        # check_datas(r, yamlvalue)

    @allure.story("第一条数据的第一个流程流程终止")
    def test17(self):
        """第一条数据的第一个流程流程终止"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_data_details.yaml",
                                                                               "第一条数据的第一个流程流程终止")
        yamlvalue['data']['procInstId'] = getattr(result, 'proc_datas')['procInstId']
        r = a.request(csurl, method, json=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        # check_datas(r, yamlvalue)

    @allure.story("第一条数据的数据分配（分配给测试人员）")
    def test18(self, insert_module_data):
        """第一条数据的数据分配（分配给测试人员）"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_data_details.yaml",
                                                                               "第一条数据的数据分配（分配给测试人员）")
        yamlvalue['data']['ids'].append(insert_module_data[0])
        r = a.request(csurl, method, json=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        # check_datas(r, yamlvalue)

    @allure.story("第一条数据的分配发送消息")
    def test19(self):
        """第一条数据的分配发送消息"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_data_details.yaml",
                                                                               "第一条数据的分配发送消息")
        yamlvalue['data']['businessId'] = getattr(result, 'proc_datas')['businessId']
        yamlvalue['data']['proDefId'] = getattr(result, 'proc_datas')['procDefId']
        r = a.request(csurl, method, params=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        # check_datas(r, yamlvalue)

    @allure.story("流程终止并且分配给别人后查询第一条数据列表")
    def test20(self, insert_module_data):
        """流程终止并且分配给别人后查询第一条数据列表"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_data_details.yaml",
                                                                               "流程终止并且分配给别人后查询第一条数据列表")
        r = a.request(csurl + insert_module_data[0], method, params=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("删除第二条表单数据")
    def test21(self, insert_module_data):
        """删除第二条表单数据"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_data_details.yaml", "删除第二条表单数据")
        r = a.request(csurl + insert_module_data[1], method, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)

    @allure.story("第三条数据添加团队成员")
    def test22(self, insert_module_data):
        """第三条数据添加团队成员"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_data_details.yaml",
                                                                               "第三条数据添加团队成员")
        url1 = insert_module_data[2] + "/team-member/add"
        r = a.request(csurl + url1, method, json=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        # check_datas(r, yamlvalue)

    @allure.story("第三条数据删除添加的团队成员")
    def test23(self, insert_module_data):
        """第三条数据删除添加的团队成员"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_data_details.yaml",
                                                                               "第三条数据删除添加的团队成员")
        url1 = insert_module_data[2] + "/team-member/remove"
        r = a.request(csurl + url1, method, params=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        # check_datas(r, yamlvalue)

    @allure.story("第三条数据查询团队成员添加结果")
    def test24(self, insert_module_data):
        """第三条数据查询团队成员添加结果"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_data_details.yaml",
                                                                               "第三条数据查询团队成员添加结果")
        r = a.request(csurl + insert_module_data[2], method, params=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("结束再查询一次表单数据")
    def test25(self):
        """结束再查询一次表单数据"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("module_data_details.yaml",
                                                                               "结束再查询一次表单数据")
        r = a.request(csurl, method, json=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)
