# coding=utf-8

from Src.Browser import Browser
from Src.Wait import Wait
from Src.Element import Element
from selenium import webdriver
from Utils.Paths import FIREFOX_DRIVER_DIR
import inspect
from Utils.ParseLocator import ParseLocator

class BasePage(object):
    """页面基类"""
    def __init__(self, driver):
        self.driver = driver
        self.browser = Browser(self.driver)
        self.wait = Wait(self.driver)

    def _define_element(self, get_locator=False):
        """inspect.stack()[1][3]是获取当前运行类的函数名"""
        element_path = '{0}.{1}'.format(self.__class__.__name__, inspect.stack()[1][3])
        parse_locator = ParseLocator()
        locator = parse_locator.get_locator(element_path)
        if get_locator:
            return locator
        else:
            return Element(self.driver, element_path, locator)


if __name__ == '__main__':
    pass