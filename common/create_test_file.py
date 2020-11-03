# !/usr/bin/python
# coding:utf-8

import os
from common.path_conf import TEST_PATH, DATA_DIR
from common.read_data import ReadFileData
from common.case_template import Case_Templates
from common.utils import create_file, write_file


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
    try:
        rd = ReadFileData()
        yaml_all = rd.load_yaml(os.path.join(DATA_DIR, yaml_name))
        all_api_items = yaml_all.items()
        n = 0
        for k, v in all_api_items:
            n = n + 1
            yaml_title = k
            method = v['method']
            yaml_data = v['data']
            num = str(n).zfill(2)
            commoncase = ct.case_templates_common(yaml_title, method, yaml_data, num)
            write_file(test_path, commoncase)
        print('文件生成完毕')
    except Exception as e:
        print(e)
        os.remove(test_path)  # 如果有异常，删除之前创建的文件
        print('文件生成失败，已自动删除')


if __name__ == '__main__':
    generate_case('模块管理', 'company_datas.yaml')
