#!/usr/bin/python
# coding:utf-8


import json
import allure
import pytest
from common import path_conf
from core import result_base
from common import get_root_url
from common.utils import get_current_time
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
@allure.feature("权限管理")
class TestPermissionManage(object):
    @allure.story("部门列表搜索")
    def test01(self):
        """部门列表搜索"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("permission_manage.yaml", "部门列表搜索")
        r = a.request(csurl, method, json=yamlvalue['data'], headers=head)
        setattr(result, 'parent_dept_id', json.loads(r.text)['data']['list'][0]['_id'])
        setattr(result, 'system_role_id', json.loads(r.text)['data']['list'][0]['_principalReference']['roleIds'][0])
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("部门列表新增下级")
    def test02(self):
        """部门列表新增下级"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("permission_manage.yaml", "部门列表新增下级")
        yamlvalue['data']['parentId'] = getattr(result, 'parent_dept_id')
        r = a.request(csurl, method, json=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        setattr(result, 'dept_id', json.loads(r.text)['data']['_id'])
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("部门编辑下级")
    def test03(self):
        """部门编辑下级"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("permission_manage.yaml", "部门编辑下级")
        yamlvalue['data']['_id'] = getattr(result, 'dept_id')
        r = a.request(csurl, method, json=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("新增人员表单查询")
    def test04(self):
        """新增人员表单查询"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("permission_manage.yaml", "新增人员表单查询")
        r = a.request(csurl, method, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        setattr(result, 'username_fieldId', json.loads(r.text)['data'][0]['children'][0]['id'])
        setattr(result, 'phone_fieldId', json.loads(r.text)['data'][1]['children'][2]['id'])
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("人员字段重复性检查")
    def test05(self):
        """人员字段重复性检查"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("permission_manage.yaml", "人员字段重复性检查")
        data = [{"fieldId": "%s" % getattr(result, 'username_fieldId'), "value": "scx_11"},
                {"fieldId": "%s" % getattr(result, 'phone_fieldId'), "value": "18005162887"}]
        r = a.request(csurl, method, params=data, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("新增人员")
    def test06(self):
        """新增人员"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("permission_manage.yaml", "新增人员")
        n = get_current_time(4)
        data = {"username": "cs_" + n, "password": "a111111", "status": "正常", "truename": "测试cs", "sex": "男",
                "phone": "18005162887", "youxiang": "", "deptIds": "%s" % getattr(result, 'dept_id'),
                "identity": "普通员工",
                "roleIds": ["%s" % getattr(result, 'system_role_id')]}
        r = a.request(csurl, method, json=data, headers=head)
        setattr(result, 'ceshi_user_id', json.loads(r.text)['data']['_id'])
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("人员列表展示")
    def test07(self):
        """人员列表展示"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("permission_manage.yaml", "人员列表展示")
        yamlvalue['data']['conditions']['deptIds'] = getattr(result, 'dept_id')
        r = a.request(csurl, method, json=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("查看人员表单查询")
    def test08(self):
        """查看人员表单查询"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("permission_manage.yaml", "查看人员表单查询")
        r = a.request(csurl, method, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("修改人员表单查询")
    def test09(self):
        """修改人员表单查询"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("permission_manage.yaml", "修改人员表单查询")
        r = a.request(csurl, method, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("人员列表展示字段")
    def test10(self):
        """人员列表展示字段"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("permission_manage.yaml", "人员列表展示字段")
        r = a.request(csurl, method, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("人员列表搜索展示")
    def test11(self):
        """人员列表搜索展示"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("permission_manage.yaml", "人员列表搜索展示")
        yamlvalue['data']['conditions'][1]['value'] = getattr(result, 'dept_id')
        r = a.request(csurl, method, json=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("修改人员部门")
    def test12(self):
        """修改人员部门"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("permission_manage.yaml", "修改人员部门")
        yamlvalue['data'][0]['deptIds'] = getattr(result, 'dept_id')
        yamlvalue['data'][0]['_id'] = getattr(result, 'ceshi_user_id')
        r = a.request(csurl, method, json=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)

    @allure.story("修改人员状态")
    def test13(self):
        """修改人员状态"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("permission_manage.yaml", "修改人员状态")
        yamlvalue['data'][0]['_id'] = getattr(result, 'ceshi_user_id')
        r = a.request(csurl, method, json=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("导出系统管理员")
    def test14(self):
        """导出系统管理员"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("permission_manage.yaml", "导出系统管理员")
        yamlvalue['data']['ids'] = getattr(result, 'ceshi_user_id')
        r = a.request(csurl, method, params=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)

    @allure.story("角色校验")
    def test15(self):
        """角色校验"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("permission_manage.yaml", "角色校验")
        r = a.request(csurl, method, json=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("添加角色")
    def test16(self):
        """添加角色"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("permission_manage.yaml", "添加角色")
        r = a.request(csurl, method, json=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        setattr(result, 'ceshi_role_id', json.loads(r.text)['data']['_id'])
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("角色复制")
    def test17(self):
        """角色复制"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("permission_manage.yaml", "角色复制")
        r = a.request(csurl + getattr(result, 'ceshi_role_id') + '/' + getattr(result, 'system_role_id'), method,
                      headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("角色详细")
    def test18(self):
        """角色详细"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("permission_manage.yaml", "角色详细")
        yamlvalue['data']['roleId'] = getattr(result, 'ceshi_role_id')
        r = a.request(csurl, method, params=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("角色校验（重复）")
    def test19(self):
        """角色校验（重复）"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("permission_manage.yaml", "角色校验（重复）")
        r = a.request(csurl, method, json=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("搜索角色")
    def test20(self):
        """搜索角色"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("permission_manage.yaml", "搜索角色")
        r = a.request(csurl, method, json=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("角色编辑重命名")
    def test21(self):
        """角色编辑重命名"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("permission_manage.yaml", "角色编辑重命名")
        yamlvalue['data']['_id'] = getattr(result, 'ceshi_role_id')
        r = a.request(csurl, method, json=yamlvalue['data'], headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("角色详情修改")
    def test22(self):
        """角色详情修改"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("permission_manage.yaml", "角色详情修改")
        data = {"roleFuncVoList": [
            {"idKey": "-6", "moduleCode": "task", "moduleFuncCode": None, "moduleFuncId": None, "moduleId": "-6",
             "name": "任务", "type": 1, "parentId": None},
            {"idKey": "-10018", "moduleCode": "task", "moduleFuncCode": "/task/listAll", "moduleFuncId": "-10018",
             "moduleId": "-6", "name": "全部任务", "type": 2, "parentId": "-6"}],
            "roleId": "%s" % getattr(result, 'ceshi_role_id')}
        r = a.request(csurl, method, json=data, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("角色添加人员")
    def test23(self):
        """角色添加人员"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("permission_manage.yaml", "角色添加人员")
        data = {"roleId": "%s" % getattr(result, 'ceshi_role_id'), "userIds": ["%s" % getattr(result, 'ceshi_user_id')]}
        r = a.request(csurl, method, json=data, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        # check_datas(r, yamlvalue)

    @allure.story("角色修改人员--测试人员修改为系统管理员角色")
    def test24(self):
        """角色修改人员"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("permission_manage.yaml", "角色修改人员")
        data = [{"roleIds": ["%s" % getattr(result, 'system_role_id')], "_id": "%s" % getattr(result, 'ceshi_user_id')}]
        r = a.request(csurl, method, json=data, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)

    # @allure.story("角色移除人员")
    # def test25(self):
    #     """角色移除人员"""
    #     csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("permission_manage.yaml", "角色移除人员")
    #     data = {"roleId": "%s" % getattr(result, 'system_role_id'), "userIds": ["%s" % getattr(result, 'ceshi_user_id')]}
    #     r = a.request(csurl, method, json=data, headers=head)
    #     convert_json_to_yaml(r.text, yaml_path, mainkey)
    # check_codes_msg(r, yamlvalue, mainkey)
    # check_datas(r, yamlvalue)

    @allure.story("删除测试角色")
    def test26(self):
        """删除测试角色"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("permission_manage.yaml", "删除测试角色")
        r = a.request(csurl + getattr(result, 'ceshi_role_id'), method, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("删除测试人员")
    def test27(self):
        """删除测试人员"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("permission_manage.yaml", "删除测试人员")
        r = a.request(csurl + getattr(result, 'ceshi_user_id'), method, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)

    @allure.story("删除测试部门")
    def test28(self):
        """删除测试部门"""
        csurl, method, head, yamlvalue, yaml_path, mainkey = get_common_params("permission_manage.yaml", "删除测试部门")
        r = a.request(csurl + getattr(result, 'dept_id'), method, headers=head)
        # convert_json_to_yaml(r.text, yaml_path, mainkey)
        check_codes_msg(r, yamlvalue, mainkey)
        check_datas(r, yamlvalue)
