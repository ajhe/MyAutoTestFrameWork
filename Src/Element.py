# coding=utf-8

from Src.Browser import Browser
from Src.Wait import Wait
from Utils.Decorator import logger_element
from Utils.ParseConfig import parseConfig
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

WAIT_UNTIL_TIMEOUT = parseConfig.time_config('WaitUntilTimeout')
WAIT_FREQUENCY = parseConfig.time_config('WaitFrequency')

class MetaDecorator(type):

    def __init__(cls, cls_name, supers, cls_dict):
        for attr, val in cls_dict.items():
            if val.__class__.__name__ == 'function':
                if attr not in ['__init__']:
                    cls_dict[attr] = logger_element()(val)
        type.__init__(cls, cls_name, supers, cls_dict)

__metaclass__ = MetaDecorator

class Element(object):
    """封装Selenium里的Element操作"""
    def __init__(self, driver, name, locator):
        self.driver = driver
        self.name = name
        self.locator = locator

    # 点击操作
    def click(self, timeout=WAIT_UNTIL_TIMEOUT, frequency=WAIT_FREQUENCY):
        Wait(self.driver).element_clickable(self.locator, timeout, frequency)
        Browser(self.driver)._get_element(self.locator).click()

    # 清空文本框
    def clear(self, timeout=WAIT_UNTIL_TIMEOUT, frequency=WAIT_FREQUENCY):
        Wait(self.driver).element_clickable(self.locator, timeout, frequency)
        Browser(self.driver)._get_element(self.locator).clear()

    # 输入文字内容
    def send_keys(self, value, timeout= WAIT_UNTIL_TIMEOUT, frequency=WAIT_FREQUENCY):
        Wait(self.driver).element_clickable(self.locator, timeout, frequency)
        Browser(self.driver)._get_element(self.locator).send_keys(value)

    # 提交
    def submit(self, timeout=WAIT_UNTIL_TIMEOUT, frequency= WAIT_FREQUENCY):
        Wait(self.driver).element_clickable(self.locator, timeout, frequency)
        Browser(self.driver)._get_element(self.locator).submit()

    # 获取文本框内容
    def get_text(self, timeout=WAIT_UNTIL_TIMEOUT, frequency= WAIT_FREQUENCY):
        Wait(self.driver).element_visible(self.locator, timeout, frequency)
        text = Browser(self.driver)._get_elements(self.locator).text
        return text

    # 获取元素大小
    def get_size(self, timeout=WAIT_UNTIL_TIMEOUT, frequency= WAIT_FREQUENCY):
        Wait(self.driver).element_clickable(self.locator, timeout, frequency)
        size =Browser(self.driver)._get_element(self.locator).size
        return size

    # 获取属性值
    def get_attribute(self, attribute, timeout=WAIT_UNTIL_TIMEOUT, frequency= WAIT_FREQUENCY):
        Wait(self.driver).element_present(self.locator, timeout, frequency)
        value = Browser(self.driver)._get_element(self.locator).get_attribute(attribute)
        return value

    # 判断是否可见
    def is_displayed(self, timeout=WAIT_UNTIL_TIMEOUT, frequency= WAIT_FREQUENCY):
        try:
            Wait(self.driver).element_visible(self.locator, timeout, frequency)
            Browser(self.driver)._get_element(self.locator).is_displayed()
            return True
        except (TimeoutException,NoSuchElementException):
            return False

    # 验证元素是否允许用户输入
    def is_enable(self, timeout=WAIT_UNTIL_TIMEOUT, frequency= WAIT_FREQUENCY):
        try:
            Wait(self.driver).element_visible(self.locator, timeout, frequency)
            Browser(self.driver)._get_element(self.locator).is_enable()
            return True
        except (TimeoutException,NoSuchElementException):
            return False

    # 验证元素是否可选择
    def is_selected(self, timeout=WAIT_UNTIL_TIMEOUT, frequency= WAIT_FREQUENCY):
        try:
            Wait(self.driver).element_visible(self.locator, timeout, frequency)
            Browser(self.driver)._get_element(self.locator).is_selected()
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    # 定位选择frame
    def switch_to_frame(self, timeout=WAIT_UNTIL_TIMEOUT, frequency= WAIT_FREQUENCY):
        result = Wait(self.driver).frame_switchable(self.locator, timeout, frequency)
        time.sleep(2)
        return result


