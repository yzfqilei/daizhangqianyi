# apistest

接口自动化
构造用例步骤：
1.在apidata目录下，编写数据源（yaml）文件，expectresult下数据不需要书写
2.在common目录执行create_test_file脚本，生成测试用例文件
3.检查测试文件请求方法、参数、请求头等是否正确
4.在api_test目录下执行测试文件
5.根据比对字段的需要，修改数据源文件字段数据
6.将测试文件的convert_json_to_yaml(r.text, yaml_path, mainkey)行注释
7.将测试文件的比对脚本行注释放开即可。

