import json
from configparser import ConfigParser
from common.logger import logger
from ruamel import yaml


class MyConfigParser(ConfigParser):
    # 重写 configparser 中的 optionxform 函数，解决 .ini 文件中的键option 自动转为小写的问题
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr

    def as_dict(self):
        d = dict(self._sections)
        for k in d:
            d[k] = dict(d[k])
        return d


class WriteFileData:
    def write_yaml(self, file_path, key_testcase, key1, value):
        with open(file_path, encoding="utf-8") as f:
            content = yaml.load(f, Loader=yaml.RoundTripLoader)
            # 修改yml文件中的参数
            content[key_testcase][key1] = value
        with open(file_path, 'w', encoding="utf-8") as nf:
            yaml.dump(content, nf, Dumper=yaml.RoundTripDumper, allow_unicode=True, width=1000)

    def write_ini(self, file_path, section, option, value):
        logger.info(f'加载 {file_path}文件......')
        conf = ConfigParser()
        conf.read(file_path, encoding="utf-8")
        conf.set(section, option, value)
        with open(file_path, "w", encoding="utf-8") as f:
            conf.write(f)
            logger.info(f'section{section},option{option},value{value}---写入成功')


if __name__ == '__main__':
    data = WriteFileData()
    data11 = 1123
    data.write_yaml('D:\\apistest_crm\\apidata\\123.yaml', '删除导航菜单(关联模块，范围全部)',  'data', {'menuid':444})
