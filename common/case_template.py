#!/usr/bin/python
# coding:utf-8

from common.convert import convert_str_to_hump


class Case_Templates:
    def __init__(self, feature, yaml_name):
        self.feature = feature
        self.yaml_name = yaml_name

    def case_templates_main(self):
        main_case = f"""
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
rooturl = get_root_url


@pytest.mark.usefixtures('is_login')
@allure.feature("{self.feature}")
class Test{convert_str_to_hump(self.yaml_name.split(".")[0])}(object):"""
        return main_case

    def case_templates_common(self, yaml_title, method, yaml_expect, n):
        global common_case
        if method == 'POST' and yaml_expect is not None:
            common_case = f"""
    @allure.story("{yaml_title}")
    def test{n}(self):
        \"""{yaml_title}\"""
        csurl, method, head, yamlvalue, yaml_path, check_keys = get_common_params("{self.yaml_name}", "{yaml_title}")
        a = RestClient(rooturl)
        r = a.request(csurl, method, json=yamlvalue['data'], headers=head)
        check_codes_msg(r, yamlvalue)
        check_datas(r, yamlvalue, check_keys)
            """
        elif method == 'GET' and yaml_expect is not None:
            common_case = f"""
    @allure.story("{yaml_title}")
    def test{n}(self):
        \"""{yaml_title}\"""
        csurl, method, head, yamlvalue, yaml_path, check_keys = get_common_params("{self.yaml_name}", "{yaml_title}")
        a = RestClient(rooturl)
        r = a.request(csurl, method, headers=head)
        check_codes_msg(r, yamlvalue)
        check_datas(r, yamlvalue, check_keys)
            """
        elif method == 'DELETE' and yaml_expect is not None:
            common_case = f"""
    @allure.story("{yaml_title}")
    def test{n}(self):
        \"""{yaml_title}\"""
        csurl, method, head, yamlvalue, yaml_path, check_keys = get_common_params("{self.yaml_name}", "{yaml_title}")
        a = RestClient(rooturl)
        r = a.request(csurl + yamlvalue['data'], method, headers=head)
        check_codes_msg(r, yamlvalue)
        check_datas(r, yamlvalue, check_keys)
            """
        elif method == 'POST' and yaml_expect is None:
            common_case = f"""
    @allure.story("{yaml_title}")
    def test{n}(self):
        \"""{yaml_title}\"""
        csurl, method, head, yamlvalue, yaml_path, check_keys = get_common_params("{self.yaml_name}", "{yaml_title}")
        a = RestClient(rooturl)
        r = a.request(csurl, method, json=yamlvalue['data'], headers=head)
        check_codes_msg(r, yamlvalue)
            """
        elif method == 'GET' and yaml_expect is None:
            common_case = f"""
    @allure.story("{yaml_title}")
    def test{n}(self):
        \"""{yaml_title}\"""
        csurl, method, head, yamlvalue, yaml_path, check_keys = get_common_params("{self.yaml_name}", "{yaml_title}")
        a = RestClient(rooturl)
        r = a.request(csurl, method, headers=head)
        check_codes_msg(r, yamlvalue)
            """
        elif method == 'DELETE' and yaml_expect is None:
            common_case = f"""
    @allure.story("{yaml_title}")
    def test{n}(self):
        \"""{yaml_title}\"""
        csurl, method, head, yamlvalue, yaml_path, check_keys = get_common_params("{self.yaml_name}", "{yaml_title}")
        a = RestClient(rooturl)
        r = a.request(csurl + yamlvalue['data'], method, headers=head)
        check_codes_msg(r, yamlvalue)
        """
        else:
            print("没有匹配到请求方法或模板！")
        return common_case
