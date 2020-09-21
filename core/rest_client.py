import requests
import json as complexjson
from common.logger import logger

"""
请求方法封装
"""


class RestClient:

    def __init__(self, api_root_url):
        self.api_root_url = api_root_url
        self.session = requests.session()

    def get(self, url, **kwargs):
        return self.request(url, "GET", **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.request(url, "POST", data, json, **kwargs)

    def put(self, url, data=None, **kwargs):
        return self.request(url, "PUT", data, **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url, "DELETE", **kwargs)

    def patch(self, url, data=None, **kwargs):
        return self.request(url, "PATCH", data, **kwargs)

    def request(self, url, method, data=None, json=None, **kwargs):
        url = self.api_root_url + url
        headers = dict(**kwargs).get("headers")
        params = dict(**kwargs).get("params")
        files = dict(**kwargs).get("params")
        cookies = dict(**kwargs).get("params")
        self.request_log(url, method, data, json, params, headers, files, cookies)
        if method == 'get' or method == 'GET' or method == 'Get':
            return self.session.get(url, **kwargs)
        if method == 'post' or method == 'POST' or method == 'Post':
            return requests.post(url, data, json, **kwargs)
        if method == "put" or method == 'PUT' or method == 'Put':
            if json:
                # PUT 和 PATCH 中没有提供直接使用json参数的方法，因此需要用data来传入
                data = complexjson.dumps(json)
            return self.session.put(url, data, **kwargs)
        if method == "delete" or method == 'DELETE' or method == 'Delete':
            return self.session.delete(url, **kwargs)
        if method == "patch" or method == 'PATCH' or method == 'Patch':
            if json:
                data = complexjson.dumps(json)
            return self.session.patch(url, data, **kwargs)

    def request_log(self, url, method, data=None, json=None, params=None, headers=None, files=None, cookies=None,
                    **kwargs):
        logger.info("接口请求地址 ==>> {}".format(url))
        logger.info("接口请求方式 ==>> {}".format(method))
        # Python3中，json在做dumps操作时，会将中文转换成unicode编码，因此设置 ensure_ascii=False
        logger.info("接口请求头 ==>> {}".format(complexjson.dumps(headers, indent=4, ensure_ascii=False)))
        logger.info("接口请求 params 参数 ==>> {}".format(complexjson.dumps(params, indent=4, ensure_ascii=False)))
        logger.info("接口请求体 data 参数 ==>> {}".format(complexjson.dumps(data, indent=4, ensure_ascii=False)))
        logger.info("接口请求体 json 参数 ==>> {}".format(complexjson.dumps(json, indent=4, ensure_ascii=False)))
        logger.info("接口上传附件 files 参数 ==>> {}".format(files))
        logger.info("接口 cookies 参数 ==>> {}".format(complexjson.dumps(cookies, indent=4, ensure_ascii=False)))

    def elapsed_time(res, fixed: str = 's'):
        """
        用时函数
        :param func: response实例
        :param fixed: 1或1000 秒或毫秒
        :return:
        """
        try:
            if fixed.lower() == 's':
                second = res.elapsed.total_seconds()
            elif fixed.lower() == 'ms':
                second = res.elapsed.total_seconds() * 1000
            else:
                raise ValueError("{} not in ['s'，'ms']".format(fixed))
            return second
        except Exception as e:
            logger.info(e)


if __name__ == '__main__':
    a = RestClient("")
    hd = {"Content-Type": "application/json"}
    data = {'account': 'anhui2020', 'grant_type': 'password', 'password': 'a111111', 'type': 'account'}
    re = a.request("http://crm.yunzhangfang.com/apis/login", "POST",json=data,headers=hd)
    print(re.status_code)
