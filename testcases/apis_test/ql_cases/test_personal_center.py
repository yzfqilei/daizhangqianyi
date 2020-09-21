#!/usr/bin/python
# coding:utf-8
from core.checkresult import check_codes_msg, check_datas
from core.rest_client import RestClient
from common.write_data import WriteFileData
from core.common_params import get_common_params
import json,sys,time,random
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
class Testpersonal_center():
    def test_company_infor001(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('personal_center.yaml',func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl,method=method,headers=headers)
        print(res.text)
        check_codes_msg(res,yamlvalue, mainkey)
        check_datas(res,yamlvalue)

    def test_user_infor002(self):
        #传入用例名称获取yaml数据字典
        func_name=sys._getframe().f_code.co_name
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('personal_center.yaml',func_name)
        a = RestClient(rooturl)
        res = a.request(csurl, method,headers=headers)
        print(res.text)
        check_codes_msg(res,yamlvalue, mainkey)
        check_datas(res,yamlvalue)

    def test_modify_password003(self):
        #传入用例名称获取yaml数据字典
        func_name=sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('personal_center.yaml',func_name)
        a = RestClient(rooturl)
        res = a.request(csurl, method, json=yamlvalue['data1'], headers=headers)
        check_codes_msg(res,yamlvalue, mainkey)

        #调换新旧密码值，将密码改回
        res = a.request(csurl, method, json=yamlvalue['data2'], headers=headers)
        check_codes_msg(res,yamlvalue, mainkey)

    def test_modify_user_info004(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('personal_center.yaml', func_name)
        r = RestClient(rooturl)
        res = r.request(csurl, method, json=yamlvalue['data1'], headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)
        print('-------企业信息已修改成功-------')
        res = r.request(csurl, method, json=yamlvalue['data2'], headers=headers)
        # check_codes_msg(res, yamlvalue,mainkey)
        res_dir=json.loads(res.text)
        pytest.assume(res_dir['data']['username'],yamlvalue['expectresult_renew']['data']['username'])
        pytest.assume(res_dir['data']['truename'],yamlvalue['expectresult_renew']['data']['truename'])
        pytest.assume(res_dir['data']['sex'],yamlvalue['expectresult_renew']['data']['sex'])
        print('-------企业信息修改已复原-------')

    def test_modify_conpany_info005(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey= get_common_params('personal_center.yaml', func_name)
        r = RestClient(rooturl)
        res = r.request(csurl, method, json=yamlvalue['data'], headers=headers)

        check_codes_msg(res, yamlvalue,mainkey)
        check_datas(res, yamlvalue)

    def test_change_phone_number006(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('personal_center.yaml',func_name)
        r = RestClient(rooturl)
        res = r.requ.est(csurl, method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    def test_read_notice007(self):
        #数据库插入消息
        self.create_time=str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        self.data=''.join(random.sample(['n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 7))
        self.id=random.randint(100000000,999999999)
        self.notice_id=random.randint(1000000000,9999999999)
        db.execute_db(f"INSERT INTO yzf_crm_notice.notice (id,type,msg,`data`,creator,create_time) VALUES ( '{self.notice_id}','1','a_test_message','{self.data}','631126109332017152','{self.create_time}');")
        db.execute_db(f"INSERT INTO yzf_crm_notice.user_notice (id,user_id,notice_id,read_flag,read_time,deleted) VALUES ( '{self.id}','631126109332017152','{self.notice_id}','0','{self.create_time}','0');")
        #将notice_id写入yaml的预期结果里
        func_name = sys._getframe().f_code.co_name
        data={'id':self.notice_id,'type': '1','msg':'a_test_message','data':self.data,'receiver':None,'readFlag':True,'creator':'631126109332017152'}
        expectresult={'code':0,'msg':None,'data':data}
        wd.write_yaml('..\\..\\..\\apidata\\personal_center.yaml',func_name,'expectresult',expectresult)

        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('personal_center.yaml',func_name)
        r = RestClient(rooturl)
        csurl=csurl+str(self.notice_id)+'/read-flag'
        res = r.request(csurl, method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)
