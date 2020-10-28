#!/usr/bin/python
# coding:utf-8

# 获取jenkins构建信息和本次报告地址
import os
import jenkins
import json
import urllib3
from common.read_data import ReadFileData
from common.path_conf import BASE_DIR

data = ReadFileData()
ini_pt = os.path.join(BASE_DIR, 'config/')  # linux目录
# win_ini_pt = os.path.join(BASE_DIR, 'config\\')  # windows目录
jk_ini = data.load_ini(ini_pt + 'setting.ini')['jenkins']
# jenkins登录地址
jenkins_url = jk_ini['jenkins_url']
# 获取jenkins对象
server = jenkins.Jenkins(jenkins_url, username=jk_ini['username'], password=jk_ini['password'])
# job名称
job_name = jk_ini['job_name']
# job的url地址
job_url = jenkins_url + job_name
# 获取最后一次构建
job_last_build_url = server.get_info(job_name)['lastBuild']['url']
# 报告地址
report_url = jk_ini['report_url']

'''
钉钉推送方法：
读取report文件中"prometheusData.txt"，循环遍历获取需要的值。
使用钉钉机器人的接口，拼接后推送text
'''


def DingTalkSend():
    d = {}
    # 获取项目绝对路径
    path = os.path.abspath(os.path.dirname(__file__))
    # 打开prometheusData 获取需要发送的信息
    linuxpath = path + '/allure-report/export/prometheusData.txt'
    windowspath = path + r'\allure-report\export\prometheusData.txt'
    f = open(linuxpath, 'r')
    for lines in f:
        for c in lines:
            launch_name = lines.strip('\n').split(' ')[0]
            num = lines.strip('\n').split(' ')[1]
            d.update({launch_name: num})
    print(d)
    f.close()
    retries_run = d.get('launch_retries_run')  # 运行总数
    print('运行总数：{}'.format(retries_run))
    status_passed = d.get('launch_status_passed')  # 通过数量
    print('通过数量：{}'.format(status_passed))
    status_failed = d.get('launch_status_failed')  # 不通过数量
    print('通过数量：{}'.format(status_failed))
    pass_percent = '{:.2%}'.format(int(status_passed) / (int(status_passed) + int(status_failed)))  # 通过率
    print('通过率：{}'.format(pass_percent))
    run_time = d.get('launch_time_duration')  # 执行时间
    ms = str(run_time)[-3:]
    s = str(run_time)[:-3]
    run_time_for = '{}s{}ms'.format(s, ms)
    print('执行时间：{}s{}ms'.format(s, ms))

    # 钉钉推送
    webhook = data.load_ini(ini_pt + 'setting.ini')['dingding']['webhook']
    url = webhook  # webhook
    con = {"msgtype": "text",
           "text": {
               "content": "CRM接口自动化脚本执行完成。"
                          "\n测试概述："
                          "\n运行总数：" + retries_run +
                          "\n通过数量：" + status_passed +
                          "\n失败数量：" + status_failed +
                          "\n通过率：" + pass_percent +
                          "\n执行时间：" + run_time_for +
                          "\n构建地址：\n" + job_url +
                          "\n报告地址：\n" + report_url
           }
           }
    urllib3.disable_warnings()
    http = urllib3.PoolManager()
    jd = json.dumps(con)
    jd = bytes(jd, 'utf-8')
    http.request('POST', url, body=jd, headers={'Content-Type': 'application/json'})


if __name__ == '__main__':
    DingTalkSend()
