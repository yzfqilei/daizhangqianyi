#!/usr/bin/python
# coding:utf-8

from core.checkresult import check_codes_msg,check_datas
from core.rest_client import RestClient
from common.read_data import ReadFileData
from common import path_conf
import allure
import pytest
import os

data = ReadFileData()
yaml_path = os.path.join(path_conf.BASE_DIR, "apidata", "login.yaml")
yaml_data = data.load_yaml(yaml_path)
ini_path = os.path.join(path_conf.BASE_DIR, "config", "setting.ini")
ini_data = data.load_ini(ini_path)
reportpath = path_conf.REPORT_PATH


@allure.feature("登陆测试用例")
class TestLogin(object):
    @allure.story("登陆测试case")
    @pytest.mark.parametrize("case", yaml_data.values(), ids=yaml_data.keys())
    def testlogin(self, case):
        """
        登陆测试
        """
        rooturl = ini_data['host']['api_root_url']
        loginurl = case['route']
        method = case['method']
        data = case['data']
        hd = case['headers']
        a = RestClient(rooturl)
        r = a.request(loginurl, method, json=data, headers=hd)
        check_codes_msg(r, case)



if __name__ == '__main__':
    pytest.main(["login_test.py", "--html=" + reportpath + "report.html", "--self-contained-html"])
