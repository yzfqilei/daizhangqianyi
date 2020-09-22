#!/usr/bin/python
# coding:utf-8
from core.checkresult import check_codes_msg, check_datas
from core.rest_client import RestClient
from common.write_data import WriteFileData
from core.common_params import get_common_params
import json, sys, time, random, os
import allure
import pytest
from common import path_conf
from core import result_base
from common import get_root_url
from common.mysql_operate import db

reportpath = path_conf.REPORT_PATH
wd = WriteFileData()
rooturl = get_root_url.get_root_urls()
result = result_base.ResultBase()
a = RestClient(rooturl)


@pytest.mark.usefixtures("is_login")
@allure.feature("个人中心测试用例")
class Test_personal_center():
    @allure.story("查看企业信息")
    def test_company_infor001(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('personal_center.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, headers=headers)
        print(res.text)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("查看个人信息")
    def test_user_infor002(self):
        # 传入用例名称获取yaml数据字典
        func_name = sys._getframe().f_code.co_name
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('personal_center.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(csurl, method, headers=headers)
        # print(res.text)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("修改密码")
    def test_modify_password003(self):
        # 传入用例名称获取yaml数据字典
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('personal_center.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(csurl, method, json=yamlvalue['data1'], headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)

        # 调换新旧密码值，将密码改回
        res = a.request(csurl, method, json=yamlvalue['data2'], headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)

    @allure.story("修改个人信息")
    def test_modify_user_info004(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('personal_center.yaml', func_name)
        r = RestClient(rooturl)
        res = r.request(csurl, method, json=yamlvalue['data1'], headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)
        print('-------企业信息已修改成功-------')
        res = r.request(csurl, method, json=yamlvalue['data2'], headers=headers)
        check_codes_msg(res, yamlvalue,mainkey)
        res_dir = json.loads(res.text)
        pytest.assume(res_dir['data']['username'], yamlvalue['expectresult_renew']['data']['username'])
        pytest.assume(res_dir['data']['truename'], yamlvalue['expectresult_renew']['data']['truename'])
        pytest.assume(res_dir['data']['sex'], yamlvalue['expectresult_renew']['data']['sex'])
        print('-------企业信息修改已复原-------')

    @allure.story("修改企业信息")
    def test_modify_conpany_info005(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('personal_center.yaml', func_name)
        r = RestClient(rooturl)
        res = r.request(csurl, method, json=yamlvalue['data'], headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("修改手机号码")
    def test_change_phone_number006(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('personal_center.yaml', func_name)
        r = RestClient(rooturl)
        res = r.request(csurl, method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("查看消息")
    def test_read_notice007(self):
        # 数据库插入消息
        create_time = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        header_data = ''.join(random.sample(['n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'], 7))
        id = random.randint(100000000, 999999999)
        notice_id = random.randint(1000000000, 9999999999)
        db.execute_db(
            f"INSERT INTO yzf_crm_notice.notice (id,type,msg,`data`,creator,create_time) VALUES ( '{notice_id}','1', 'a_test_message','{header_data}','756574317326995456','{create_time}');")
        db.execute_db(
            f"INSERT INTO yzf_crm_notice.user_notice (id,user_id,notice_id,read_flag,read_time,deleted) VALUES ( '{id}','756574317326995456','{notice_id}','0','{create_time}','0');")
        # 将notice_id写入yaml的预期结果里
        func_name = sys._getframe().f_code.co_name
        data = {'id': str(notice_id), 'type': 1, 'msg': 'a_test_message', 'data': header_data, 'receiver': None,
                'readFlag': True, 'creator': '756574317326995456'}
        expectresult = {'code': 0, 'msg': None, 'data': data}
        yaml_path = os.path.join(path_conf.BASE_DIR, "apidata", 'personal_center.yaml')
        wd.write_yaml(yaml_path, func_name, 'expectresult', expectresult)

        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('personal_center.yaml', func_name)
        r = RestClient(rooturl)
        csurl = csurl + str(notice_id) + '/read-flag'
        res = r.request(csurl, method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("设置所有消息为已读")
    def test_set_notice_read008(self):
        # 数据库插入消息
        create_time = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        data = ''.join(random.sample(['n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'], 7))
        id = random.randint(100000000, 999999999)
        notice_id = random.randint(1000000000, 9999999999)
        db.execute_db(
            f"INSERT INTO yzf_crm_notice.notice (id,type,msg,`data`,creator,create_time) VALUES ( '{notice_id}','1', 'a_test_message','{data}','756574317326995456','{create_time}');")
        db.execute_db(
            f"INSERT INTO yzf_crm_notice.user_notice (id,user_id,notice_id,read_flag,read_time,deleted) VALUES ( '{id}','756574317326995456','{notice_id}','0','{create_time}','0');")
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('personal_center.yaml', func_name)
        r = RestClient(rooturl)
        res = r.request(csurl, method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("清除所有消息")
    def test_clean_all_notice009(self):
        #该用例依赖test_set_notice_read008产生的notice数据，不可单独运行调试；
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('personal_center.yaml', func_name)
        r = RestClient(rooturl)
        res = r.request(csurl, method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)





