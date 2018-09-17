# coding=utf-8

# 这是一个项目所有文件路径的集合文件
import os
#ROOT DIR
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))                   #项目根目录

# CONFIG DIR
CONFIG_DIR = os.path.join(ROOT_DIR, "Config")
FRAME_CONFIG_FILE_PATH = os.path.join(CONFIG_DIR, 'FrameConfig.ini')
ELEMENT_LOCATOR_FILE_PATH = os.path.join(CONFIG_DIR, 'ElementLocator.json')

# RESULT DIR
RESULT_DIR = os.path.join(ROOT_DIR, 'Results')                     #保存结果的文件夹路径
RESULT_LOGS_DIR = os.path.join(RESULT_DIR, 'Logs')                 #保存日志的文件夹路径
RESULT_REPORTS_DIR = os.path.join(RESULT_DIR,'Reports')            #保存报告的文件夹路径
RESULT_SCREENSHOTS_DIR = os.path.join(RESULT_DIR, 'Screenshots')   #保存截图的文件夹路径

# DRIVERS DIR
DRIVERS_DIR = os.path.join(ROOT_DIR, 'Drivers')
CHROME_DRIVER_DIR = os.path.join(DRIVERS_DIR, 'Chrome', 'chromedriver.exe')
FIREFOX_DRIVER_DIR = os.path.join(DRIVERS_DIR, 'Firefox', 'geckodriver.exe')


