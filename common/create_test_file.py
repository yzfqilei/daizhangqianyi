# !/usr/bin/python
# coding:utf-8

import os
from common.path_conf import TEST_PATH, DATA_DIR
from common.read_data import ReadFileData
from common.case_template import Case_Templates
from common.utils import create_file,write_file


def generate_case(feature, yaml_name):
    ct = Case_Templates(feature, yaml_name)

    maincase = ct.case_templates_main()

    # 创建用例文件，写入用例头内容
    yaml_name1 = yaml_name.split(".")[0]
    test_path = os.path.join(TEST_PATH, "{}_test.py".format(yaml_name1))
    create_file(test_path, maincase)

    # 创建模块目录
    # feature_path = os.path.join(case_path(), feature)
    # mkdir(feature_path)

    # 读取yaml文件,写入用例方法内容
    rd = ReadFileData()
    yaml_all = rd.load_yaml(os.path.join(DATA_DIR, yaml_name))
    all_api_items = yaml_all.items()
    n = 0
    for k, v in all_api_items:
        n = n + 1
        yaml_title = k
        method = v['method']
        yaml_expect = v['expectresult']['data']
        commoncase = ct.case_templates_common(yaml_title, method, yaml_expect, n)
        write_file(test_path, commoncase)
    print('文件生成完毕')


if __name__ == '__main__':
    generate_case('首页卡片测试', 'component.yaml')
