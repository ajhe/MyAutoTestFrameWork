# coding=utf-8

from Utils.Decorator import logger_browser
from Utils.ParseConfig import parseConfig
from Utils.Paths import RESULT_SCREENSHOTS_DIR
from selenium.webdriver.support.wait import WebDriverWait
import time
import os


WAIT_UNTIL_TIMEOUT = parseConfig.time_config('WaitUntilTimeout')
WAIT_FREQUENCY = parseConfig.time_config('WaitFrequency')

class MetaDecorator(type):
    """
    元类自动装饰,一定要注意是否已被装饰过了，如果装饰顺序不对
    就没有效果
    """
    def __new__(mcs, cls_name, supers, cls_dict):
        for attr, val in cls_dict.items():
            if val.__class__.__name__ == 'function':
                #列表中方法的日志不在这记录的，所以为了避免重复记日志，将其排除
                if attr not in ['__init__', '_get_element', '_get_elements']:
                    cls_dict[attr] = logger_browser()(val)
        return type.__new__(mcs, cls_name, supers, cls_dict)


class Browser(metaclass=MetaDecorator):
    """封装selenium的WebDriver类"""
    def __init__(self, driver):
        self.driver = driver

    def _get_element(self, lecator):
        """该方法专门给Element封装用的，所以写成私有方法，平时不调用"""
        return self.driver.find_element(by=lecator[0], value=lecator[1])

    def _get_elements(self, lecator):
        """该方法专门给Element封装用的，所以写成私有方法，平时不调用"""
        return  self.driver.find_elements(by=lecator[0], value=lecator[1])

    #定位元素
    def get_element(self, lecator, timeout=WAIT_UNTIL_TIMEOUT, frequency= WAIT_FREQUENCY):
        """
        通过定位器获取页面元素，每一段时间尝试获取一次，获取成功后返回获取的页面元素，获取失败后抛出 NoSuchElement 异常
        locator: 定位器，包含定位方式和定位表达式的元组，如("id", "username")
        timeout: 超时时间，默认为30秒
        frequency: 获取频率，默认为0.5秒
        :param lecator:
        :param timeout:
        :param frequency:
        :return:
        """
        # 之所以使用lambda表达式是因为util接收的参数是method而不是element，所以不能显式调用find_element方法，
        # 而是将find_element方法作为参数传给until。同时method的参数是driver，所以这里lambda表达式接收的参数也是driver。
        # until 也可以使用expected_conditions，EC所有的类都是期望场景，实例方法__call__里接收参数driver。
        element = WebDriverWait(self.driver, timeout, frequency).until(
            lambda _driver : _driver.find_element(by=lecator[0], value=lecator[1]), str(lecator))
        return element

    # 定位元素组
    def get_elements(self, lecator, timeout=WAIT_UNTIL_TIMEOUT, frequency= WAIT_FREQUENCY):
        elements = WebDriverWait(self.driver, timeout, frequency).until(
            lambda _driver : _driver.find_element(by=lecator[0], value=lecator[1]), str(lecator))
        return elements

    #获取页面源码
    def get_page_source(self):
        return self.driver.page_source

    #获取页面标题title
    def get_title(self):
        return self.driver.title

    #获取当前页面地址URL
    def get_url(self):
        return self.driver.current_url

    #获取当前浏览器
    def get_driver(self):
        return self.driver

    #打开网页
    def navigate_to(self, url):
        self.driver.get(url)

    #前进操作
    def forward(self):
        self.driver.forward()

    #后退操作
    def back(self):
        self.driver.back()
