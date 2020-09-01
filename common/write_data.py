import yaml
import json
from configparser import ConfigParser
from common.logger import logger


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

    # def __init__(self):
    #     pass

    def write_yaml(self, file_path, key_testcase, key, value):  # 目前只支持写入data中，key_testcase为函数名
        with open(file_path, 'r', encoding='utf-8') as f:
            content = yaml.load(f, Loader=yaml.FullLoader)
        content[key_testcase][key]['name'] = value
        with open(file_path, 'w', encoding="utf-8") as nf:
            yaml.dump(content, nf)

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
    data.write_yaml('D:\\PycharmProjects\\crm_apitest\\apidata\\modules.yaml', 'test_creat_module001', 'data', 'qwer')
