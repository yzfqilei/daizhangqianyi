#!/usr/bin/python
# coding:utf-8

import os

# 项目目录
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# 测试用例
DATA_DIR = os.path.join(BASE_DIR, 'apidata\\')

# 日志目录
LOG_PATH = os.path.join(BASE_DIR, 'log\\')

# 报告目录
REPORT_PATH = os.path.join(BASE_DIR, 'report\\')

if __name__ == "__main__":
    print(BASE_DIR)