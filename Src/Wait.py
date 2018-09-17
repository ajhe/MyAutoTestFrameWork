# coding=utf-8

from Utils.ParseConfig import parseConfig
from Utils.Decorator import logger_wait
from Utils.Decorator import my_logger_wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

WAIT_IMPLICITY_TIMEOUT = parseConfig.time_config('ImplicityWaitTime')
WAIT_UNTIL_TIMEOUT = parseConfig.time_config('WaitUntilTimeout')
WAIT_UNTIL_NOT_TIMEOUT = parseConfig.time_config('WaitUntilNotTimeout')
WAIT_FREQUENCY = parseConfig.time_config('WaitFrequency')

class MetaDecorator(type):
    def __init__(cls, cls_name, supers, cls_dict):
        for attr, val in cls_dict.items():
            if val.__class__.__name__ == 'function':
                if attr not in ['__init__']:
                    cls_dict[attr] = logger_wait()(val)
        type.__init__(cls, cls_name, supers, cls_dict)


class Wait(object):
    """封装selenium的WebDriverWait类"""

    # __metaclass__ = MetaDecorator
    # 之前元类定义是__new__,返回的是一个对象，所以会报错，现在使用__init__,是初始化一个实例

    def __init__(self, driver):
        self.driver = driver

    @my_logger_wait
    def set_implicitly_wait(self, timeout=WAIT_IMPLICITY_TIMEOUT):
        self.driver.implicitly_wait(timeout)

    # 判断传入的title是否存在当前的driver.title
    @my_logger_wait
    def title_is(self, title, timeout=WAIT_UNTIL_TIMEOUT, frequency=WAIT_FREQUENCY):
        result = WebDriverWait(self.driver, timeout, frequency).until(
            ec.title_is(title), 'Wait title is {0}'.format(title))
        return result

    # 判断传入的title是否存在当前的driver.title
    @my_logger_wait
    def title_is_not(self, title, timeout=WAIT_UNTIL_NOT_TIMEOUT, frequency=WAIT_FREQUENCY):
        result = WebDriverWait(self.driver, timeout, frequency).until_not(
            ec.title_is(title), 'Wait title is not {0}'.format(title))
        return result

    # 判断传入的title是否存在当前的driver.title
    @my_logger_wait
    def title_contains(self, title, timeout=WAIT_UNTIL_TIMEOUT, frequency=WAIT_FREQUENCY):
        result = WebDriverWait(self.driver, timeout, frequency).until(
            ec.title_contains(title), 'Wait title contains {0}'.format(title)
        )
        return result

    # 判断传入的title是否存在当前的driver.title
    @my_logger_wait
    def title_not_contains(self, title, timeout=WAIT_UNTIL_NOT_TIMEOUT, frequency=WAIT_FREQUENCY):
        result = WebDriverWait(self.driver, timeout, frequency).until_not(
            ec.title_contains(title), 'Wait title not contains {0}'.format(title)
        )
        return result

    # 判断传入的元素是否出现，
    @my_logger_wait
    def element_present(self, locator, timeout=WAIT_UNTIL_TIMEOUT, frequency=WAIT_FREQUENCY):
        result = WebDriverWait(self.driver, timeout, frequency).until(
            ec.presence_of_element_located(locator), 'Wait element {0} presents'.format(locator)
        )
        return result

    # 判断传入的元素是否出现
    @my_logger_wait
    def element_not_present(self, locator, timeout=WAIT_UNTIL_NOT_TIMEOUT, frequency=WAIT_FREQUENCY):
        result = WebDriverWait(self.driver, timeout, frequency).until_not(
            ec.presence_of_element_located(locator), 'Wait element {0} not presents'.format(locator)
        )
        return result

    # 判断传入的元素是否可点击
    @my_logger_wait
    def element_clickable(self, locator, timeout=WAIT_UNTIL_TIMEOUT, frequency=WAIT_FREQUENCY):
        result = WebDriverWait(self.driver, timeout, frequency).until(
            ec.element_to_be_clickable(locator), 'Wait element {0} clickable'.format(locator))
        #print result
        return result

    # 判断传入的元素是否可点击
    @my_logger_wait
    def element_not_clickable(self, locator, timeout=WAIT_UNTIL_NOT_TIMEOUT, frequency=WAIT_FREQUENCY):
        result = WebDriverWait(self.driver, timeout, frequency).until_not(
            ec.element_to_be_clickable(locator), 'Wait element {0} not clickable'.format(locator)
        )
        return result

    # 验证传入元素是否可见
    @my_logger_wait
    def element_visible(self, locator, timeout=WAIT_UNTIL_TIMEOUT, frequency=WAIT_FREQUENCY):
        result = WebDriverWait(self.driver, timeout, frequency).until(
            ec.visibility_of_element_located(locator), 'Wait element {0} visible'.format(locator)
        )
        return result

    # 验证传入元素是否可见
    @my_logger_wait
    def element_not_visible(self, locator, timeout=WAIT_UNTIL_NOT_TIMEOUT, frequency=WAIT_FREQUENCY):
        result = WebDriverWait(self.driver, timeout, frequency).until_not(
            ec.visibility_of_element_located(locator), 'Wait element {0} visible'.format(locator)
        )
        return result

    # 验证传入的元素的frame是否可切入
    @my_logger_wait
    def frame_switchable(self, locator, timeout=WAIT_UNTIL_TIMEOUT, frequency=WAIT_FREQUENCY):
        result = WebDriverWait(self.driver, timeout, frequency).until(
            ec.frame_to_be_available_and_switch_to_it(locator), 'Wait frame {0} switchable'.format(locator)
        )
        return result

    # 验证传入的元素的frame是否可切入
    @my_logger_wait
    def frame_not_switchable(self, locator, timeout=WAIT_UNTIL_NOT_TIMEOUT, frequency=WAIT_FREQUENCY):
        result = WebDriverWait(self.driver, timeout, frequency).until_not(
            ec.frame_to_be_available_and_switch_to_it(locator), 'Wait frame {0} not switchable'.format(locator)
        )
        return result

    # 判断是否有弹框alert出现
    @my_logger_wait
    def alert_present(self, timeout=WAIT_UNTIL_TIMEOUT, frequency=WAIT_FREQUENCY):
        result = WebDriverWait(self.driver, timeout, frequency).until(
            ec.alert_is_present(), 'Wait alert visiable')
        return result

    # 判断是否有弹框alert出现
    @my_logger_wait
    def alert_not_present(self, timeout=WAIT_UNTIL_NOT_TIMEOUT, frequency=WAIT_FREQUENCY):
        result = WebDriverWait(self.driver, timeout, frequency).until_not(
            ec.alert_is_present(), 'Wait alert not visiable')
        return result

