#!/usr/bin/python
# coding:utf-8

import pytest

if __name__ == '__main__':
    pytest.main(['-s','-q','testcases','--alluredir','./allure-results,'--clean-alluredir','--html=./report/report.html','--self-contained-html'])
