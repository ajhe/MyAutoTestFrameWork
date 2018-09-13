# coding=utf-8

from Utils.Paths import RESULT_LOGS_DIR, FRAME_CONFIG_FILE_PATH
from logging.handlers import TimedRotatingFileHandler
import ConfigParser
import logging
import time
import os

try:
    config = ConfigParser.ConfigParser()
    config.read(FRAME_CONFIG_FILE_PATH)
    _config_switch = config.get('LogConfig', 'ConsoleSwitch')
    ConsoleSwitch = True if _config_switch != "False" else False
    _file_switch = config.get('LogConfig', 'FileSwitch')
    FileSwitch = True if _file_switch != "False" else False
    ConsoleLevel = config.get('LogConfig', 'ConsoleLevel')
    FileLevel = config.get('LogConfig', 'FileLevel')
except Exception as e:
    print ('[FrameConfig.ini] read error:'.format(e))
    ConsoleSwitch = True           # 日志开关
    FileSwitch = True              # 文件日志开关
    ConsoleLevel = 'INFO'           # 日志输出级别
    FileLevel = 'DEBUG'              # 文件日志输出级别

class Logger(object):

    def __init__(self, logger):
        """
        定义构造函数，主要是定义了日志类的一些属性，包括日志名，存放地址，日志格式，输出级别
        :param logger:
        """
        self.logger = logging.getLogger(logger)
        logging.root.setLevel(logging.NOTSET)
        now_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        self.log_file_name = '{0}.log'.format(now_time)
        if not os.path.exists(RESULT_LOGS_DIR):
            os.makedirs(RESULT_LOGS_DIR)
        self.log_file_path = os.path.join(RESULT_LOGS_DIR, self.log_file_name)
        self.formatter = logging.Formatter('[%(asctime)s][%(levelname)s][%(module)s][%(funcName)s]:%(message)s')
        self.console_output_level = ConsoleLevel
        self.file_output_level = FileLevel
        self.backup_count = 20


    def get_logger(self, console_switch=ConsoleSwitch, file_switch=FileSwitch):
        """
        在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回
        :param console_switch:
        :param file_switch:
        :return self.logger:
        """

        if not self.logger.handlers:
            if console_switch:
                console_handler = logging.StreamHandler()
                console_handler.setLevel(self.console_output_level)
                console_handler.setFormatter(self.formatter)
                self.logger.addHandler(console_handler)
            if file_switch:
                # file_handler = logging.FileHandler(self.log_file_name)
                # 下面使用TimedRotatingFileHandler，是带时间回滚的日志形式
                file_handler = TimedRotatingFileHandler(filename=self.log_file_path, when='D',
                                                        interval=1, backupCount=self.backup_count, delay=True,
                                                        encoding='utf-8')
                file_handler.setLevel(self.file_output_level)
                file_handler.setFormatter(self.formatter)
                self.logger.addHandler(file_handler)
        return self.logger

testLogger = Logger('MyTestLogger').get_logger()

if __name__ == '__main__':
    testLogger.info("Hello World")
