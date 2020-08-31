#!/usr/bin/python
# coding:utf-8

import requests, urllib3
from urllib3 import encode_multipart_formdata
from common.logger import logger


class RunMethod(object):
    """
    request
    """
    urllib3.disable_warnings()

    def post_main(self, url, data, header, file=None):
        """
        post请求
        :param url:
        :param data:
        :param header:
        :param file:
        :return:
        """
        res = None
        if file != None:
            res = requests.post(url=url, json=data, headers=header, verify=False)
        else:
            res = requests.post(url=url, json=data, headers=header, files=file, verify=False)  # json=等于json.dumps
        return res.json()

    def get_main(self, url, header, param=None):
        """
        get请求
        :param url:
        :param header:
        :param param:
        :return:
        """
        res = None
        if param == None:
            res = requests.get(url=url, headers=header, verify=False)
        else:
            res = requests.get(url=url, headers=header, json=param, verify=False)
        return res.json()

    def request_log(self, url, method, data=None, json=None, params=None, headers=None, files=None, cookies=None,
                    **kwargs):
        logger.info("接口请求地址 ==>> {}".format(url))
        logger.info("接口请求方式 ==>> {}".format(method))
        # Python3中，json在做dumps操作时，会将中文转换成unicode编码，因此设置 ensure_ascii=False
        logger.info("接口请求头 ==>> {}".format(json.dumps(headers, indent=4, ensure_ascii=False)))
        logger.info("接口请求 params 参数 ==>> {}".format(json.dumps(params, indent=4, ensure_ascii=False)))
        logger.info("接口请求体 data 参数 ==>> {}".format(json.dumps(data, indent=4, ensure_ascii=False)))
        logger.info("接口请求体 json 参数 ==>> {}".format(json.dumps(json, indent=4, ensure_ascii=False)))
        logger.info("接口上传附件 files 参数 ==>> {}".format(files))
        logger.info("接口 cookies 参数 ==>> {}".format(json.dumps(cookies, indent=4, ensure_ascii=False)))


    def run_main(self, method, url, header, data=None, file=None):
        """
        被调用主request
        :param method:
        :param url:
        :param header:
        :param data:
        :return:
        """
        try:
            res = None
            self.request_log(method,url,header,data)
            if method == 'post' or method == 'POST' or method == 'Post':
                res = self.post_main(url, data, header, file=None)
            elif method == 'get' or method == 'GET' or method == 'Get':
                res = self.get_main(url, header, param=None)
            else:
                return "request传参错误"
            return res
        except Exception as e:
            logger.error("请求方法报错{}".format(e))


if __name__ == '__main__':
    a = RunMethod()
    hd = {"Content-Type": "application/json"}
    data = {'account': 'anhui2020', 'grant_type': 'password', 'password': 'a111111', 'type': 'account'}
    res = a.run_main('post', 'http://crm.yunzhangfang.com/apis/login', hd)
    print(res.text())
