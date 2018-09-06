# coding=utf-8

from Utils.Logger import Logger

testMyLogger = Logger("testMyLogger")
mylogger = testMyLogger.get_logger()

if __name__ == '__main__':
    mylogger.info("hello")