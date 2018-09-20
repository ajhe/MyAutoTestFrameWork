# coding=utf-8

from Utils.ParseConfig import parseConfig
from Utils.Paths import FIREFOX_DRIVER_DIR, CHROME_DRIVER_DIR
from selenium import webdriver
from Utils.Logger import testLogger
from selenium.common.exceptions import WebDriverException


WAIT_IMPLICITY_TIME = parseConfig.time_config('ImplicityWaitTime')
BROWSER_TYPE = parseConfig.browser_type_config()
BROWSER_WINDOW_SIZE = parseConfig.browser_window_size()

class BrowserEngine(object):

    def __init__(self):
        self.driver = None

    def launch_local_browser(self, launch_browser_type=BROWSER_TYPE, window_size=BROWSER_WINDOW_SIZE,
                             implicity_wait_timeout=WAIT_IMPLICITY_TIME):
        """启动本地浏览器"""
        try:
            # 初始化浏览器
            if launch_browser_type in ['FireFox', 'Firefox', 'FIREFOX', 'firefox']:
                self.driver = webdriver.Firefox(executable_path=FIREFOX_DRIVER_DIR)
                testLogger.info('Launch {0} browser'.format(launch_browser_type))
            elif launch_browser_type in ['Chrome', 'chrome', 'CHROME']:
                self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_DIR)
                testLogger.info('Launch {0} browser'.format(launch_browser_type))
            elif launch_browser_type in ['IE', 'Ie', 'ie']:
                self.driver = webdriver.Ie()
                testLogger.info('Launch {0} browser'.format(launch_browser_type))
            else:
                raise NameError
            '''
            # 设定浏览器尺寸
            if window_size in ['MAX', 'Max', 'max']:
                testLogger.info("Maximize Browser")
                self.driver.maximize_window()
            elif window_size in ['min', 'Min', 'MIN']:
                testLogger.info("Minimize Browser")
                self.driver.minimize_window()
            '''
            # 设定隐式等待时间
            testLogger.info('Set implicitly wait time to {0}'.format(str(implicity_wait_timeout)))
            self.driver.implicitly_wait(implicity_wait_timeout)
            return self.driver
        except NameError:
            testLogger.error('Fail to launch the {0} browser'.format(BROWSER_TYPE))
            raise
        except WebDriverException as e:
            testLogger.error('Fail to launch browser with {0}'.format(e))
            raise e
        except Exception:
            testLogger.exception("Fail to launch browser", exc_info=True)
            raise

    # 获得driver
    def get_driver(self):
        testLogger.info('Get current driver, ID: {0}, Driver: {1}'.format(id(self.driver), self.driver))
        return self.driver

    def quit_browser(self):
        testLogger.info('Quit browser and release current driver')
        self.driver.quit()

browserEngine = BrowserEngine()

if __name__ == '__main__':
    browser_engine = BrowserEngine()
    driver = browser_engine.launch_local_browser()
    import time
    time.sleep(5)
    print ('{0} >>>>>>>> {1}'.format(id(driver), driver))
    browser_engine.quit_browser()



