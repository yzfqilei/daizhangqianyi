#!/usr/bin/python
# coding:utf-8

import re
import pytest
import allure
from requests import Response
from common.logger import logger
import json
import traceback


def check_codes_msg(r: Response, case_info, mainkey=None):
    """检查运行结果"""
    with allure.step("校验返回响应码"):
        allure.attach(name='预期响应码', body=str(case_info['expectcode']))
        allure.attach(name='实际响应码', body=str(r.status_code))
    if mainkey is not None:
        print(">>> casename : '%s' start " % mainkey)
        logger.info(">>> casename : '%s' start " % mainkey)
    pytest.assume(case_info['expectcode'] == r.status_code)
    logger.info(">>> expect:" + str(case_info['expectcode']) + "," + "actual:" + str(r.status_code))
    rjson = json.loads(r.text)
    if case_info['expectresult']:
        with allure.step("校验返回结果code和msg"):
            allure.attach(name='预期值code', body=str(case_info['expectresult']['code']))
            allure.attach(name='实际值code', body=str(rjson['code']))
            allure.attach(name='预期值msg', body=str(case_info['expectresult']['msg']))
            allure.attach(name='实际值msg', body=str(rjson['msg']))
        pytest.assume(str(case_info['expectresult']['code']) == str(rjson['code']))
        pytest.assume(str(case_info['expectresult']['msg']) == str(rjson['msg']))
        logger.info(">>> expect_code:" + str(case_info['expectresult']['code']) + "," + "actual_code:" + str(rjson['code']))
        logger.info(">>> expect_msg:" + str(case_info['expectresult']['msg']) + "," + "actual_msg:" + str(rjson['msg']))


def check_datas(r, case_info):
    expect_data = case_info['expectresult']['data']
    actual_data = json.loads(r.text)['data']
    with allure.step("校验返回结果data"):
        allure.attach(name='预期值data', body=str(expect_data))
        allure.attach(name='实际值data', body=str(actual_data))
    try:
        print('>>> actual_data:{}'.format(actual_data))
        print('>>> expect_data:{}'.format(expect_data))
        logger.info('>>> actual_data:{}'.format(actual_data))
        logger.info('>>> expect_data:{}'.format(expect_data))
        if isinstance(actual_data, list) and actual_data:
            actual_data = actual_data[0]
        _check_dict(actual_data, expect_data)
    except Exception as e1:
        print(traceback.format_exc())
        logger.info(traceback.format_exc())
        raise e1


def _check_dict(dt, de):
    if dt and not de:
        raise AssertionError('>>> Data matching failed')
    if not de or isinstance(de, int) or isinstance(de, str):
        try:
            assert de == dt
        except:
            print('>>> data field values do not match.actual_value: %s;expect_value: %s' % (dt, de))
            logger.info('>>> data field values do not match.actual_value: %s;expect_value: %s' % (dt, de))
            raise AssertionError
    else:
        keys = (dt.keys(), de.keys())
        el = [x for x in keys[1] if x[0] != '*']
        for j in el:
            if j in keys[0]:
                dt_value, de_value = dt[j], de[j]
                try:
                    assert (dt_value == de_value)
                    continue
                except:
                    if not isinstance(de_value, (dict, list)):
                        try:
                            assert (dt_value == de_value)
                            continue
                        except:
                            print('>>> %s field values do not match.actual_value: %s;expect_value: %s' % (
                                str(j), dt_value, de_value))
                            logger.info('>>> %s field values do not match.actual_value: %s;expect_value: %s' % (
                                str(j), dt_value, de_value))
                            raise AssertionError
                    if isinstance(de_value, dict):
                        try:
                            assert (dt_value == de_value)
                            continue
                        except:
                            _check_dict(dt_value, de_value)
                            # logger.info(traceback.format_exc())
                    if isinstance(de_value, list):
                        try:
                            assert (dt_value == de_value)
                            continue
                        except:
                            for i in range(0, len(de_value)):
                                _check_dict(dt_value[i], de_value[i])
                            # logger.info(traceback.format_exc())
            else:
                print('>>> There is no %s field in the actual return parameter' % str(j))
                logger.info('>>> There is no %s field in the actual return parameter' % str(j))
                raise AssertionError()
