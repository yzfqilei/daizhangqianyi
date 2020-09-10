#!/usr/bin/python
# coding:utf-8

import re
import pytest
import allure
from requests import Response
from common.logger import logger
import json
import jsonpath


def check_codes_msg(r: Response, case_info):
    """检查运行结果"""
    with allure.step("校验返回响应码"):
        allure.attach(name='预期响应码', body=str(case_info['expectcode']))
        allure.attach(name='实际响应码', body=str(r.status_code))
    pytest.assume(case_info['expectcode'] == r.status_code)
    logger.info("expect:" + str(case_info['expectcode']) + "," + "actual:" + str(r.status_code))
    rjson = json.loads(r.text)
    if case_info['expectresult']:
        with allure.step("校验响应code和全量msg"):
            allure.attach(name='预期值', body=str(case_info['expectresult']))
            allure.attach(name='实际值', body=r.text)
        pytest.assume(str(case_info['expectresult']['code']) == str(rjson['code']))
        pytest.assume(str(case_info['expectresult']['msg']) == str(rjson['msg']))
        logger.info("expect:" + str(case_info['expectresult']) + "," + "actual:" + str(r.text))


def check_datas(r, case_info, listname=None):
    case_info_data = case_info['expectresult']['data']
    rjson = json.loads(r.text)
    with allure.step("检验响应单个msg"):
        if listname:
            if isinstance(rjson['data'], list):
                for listdata in rjson['data']:
                    for ss in listname:
                        try:
                            pytest.assume(str(case_info_data[ss]) == str(listdata[ss]))
                            logger.info("expectdata:" + str(case_info_data[ss]) + "," + "actualdata:" + str(listdata[ss]))
                        except:
                            allure.attach(name="'%s'字段预期值" % ss, body=str(case_info_data[ss]))
                            allure.attach(name="'%s'字段实际值" % ss, body=str(listdata[ss]))
            else:
                for ss in listname:
                    try:
                        pytest.assume(str(case_info_data[ss]) == str(rjson['data'][ss]))
                        logger.info("expectdata:" + str(case_info_data[ss]) + "," + "actualdata:" + str(rjson['data'][ss]))
                    except:
                        allure.attach(name="'%s'字段预期值" % ss, body=str(case_info_data[ss]))
                        allure.attach(name="'%s'字段实际值" % ss, body=str(rjson['data'][ss]))
        else:
            try:
                pytest.assume(str(case_info_data) == str(rjson['data']))
            except:
                allure.attach(name="data字段预期值", body=str(case_info_data))
                allure.attach(name="data字段实际值", body=str(rjson['data']))
