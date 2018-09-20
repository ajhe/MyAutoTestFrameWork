# coding=utf-8

from Utils.Paths import FRAME_CONFIG_FILE_PATH
from Utils.Logger import testLogger
from ConfigParser import ConfigParser

class ParseConfig(object):
    def __init__(self):
        self.config = ConfigParser()
        self.config.read(FRAME_CONFIG_FILE_PATH)

    def log_config(self, setting_name):
        try:
            return self.config.get('LogConfig', setting_name)
        except Exception as e:
            testLogger.exception('[Exception]:', exc_info=True)
            raise e

    def time_config(self, setting_name):
        try:
            value = self.config.get('TimeConfig', setting_name)
            return float(value)
        except Exception as e:
            testLogger.exception('[Exception]:', exc_info=True)
            raise e

    def screenshot_config(self, setting_name):
        try:
            result = self.config.get('ScreenShotConfig', setting_name)
            if result == 'True':
                return True
            else:
                return False
        except Exception as e:
            testLogger.exception('[Exception]:', exc_info=True)
            raise e

    def rerun_config(self, setting_name):
        try:
            result = self.config.get('ReRunConfig', setting_name)
            if result == 'False':
                return False
            elif result.isdigit():
                return int(result)
            else:
                return True
        except Exception as e:
            testLogger.exception('[Exception]: ', exc_info=True)
            raise e

    def browser_type_config(self):
        try:
            value = self.config.get('BrowserEngine', 'BrowserType')
            return value
        except Exception as e:
            testLogger.exception('[Exception]: ', exc_info=True)
            raise e

    def browser_window_size(self):
        try:
            value = self.config.get('BrowserEngine', 'WindowSize')
            return value
        except Exception as e:
            testLogger.exception('[Exception]: ', exc_info=True)
            raise e


parseConfig = ParseConfig()
if __name__ == '__main__':
    print(parseConfig.time_config('ImplicityWaitTime'))