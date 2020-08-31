#!/usr/bin/python
# coding:utf-8

import re
import pytest
import allure
from requests import Response
from common.logger import logger


def check_results(r: Response, case_info):
    """检查运行结果"""
    with allure.step("校验返回响应码"):
        allure.attach(name='预期响应码', body=str(case_info['expectcode']))
        allure.attach(name='实际响应码', body=str(r.status_code))
    pytest.assume(case_info['expectcode'] == r.status_code)
    logger.info("expect:" + str(case_info['expectcode']) + "," + "actual:" + str(r.status_code))
    if case_info['expectresult']:
        with allure.step("校验响应预期值"):
            allure.attach(name='预期值', body=str(case_info['expectresult']))
            allure.attach(name='实际值', body=r.text)
        pytest.assume(case_info['expectresult'] == r.text)
        logger.info("expect:" + str(case_info['expectresult']) + "," + "actual:" + str(r.text))
