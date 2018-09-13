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
                # 列表中方法的日志不在这记录的，所以为了避免重复记日志，将其排除
                if attr not in ['__init__', '_get_element', '_get_elements']:
                    cls_dict[attr] = logger_browser()(val)
        return type.__new__(mcs, cls_name, supers, cls_dict)


__metaclass__ = MetaDecorator

class Browser(object):
    """封装selenium的WebDriver类"""
    def __init__(self, driver):
        self.driver = driver

    def _get_element(self, locator):
        """该方法专门给Element封装用的，所以写成私有方法，平时不调用"""
        return self.driver.find_element(by=locator[0], value=locator[1])

    def _get_elements(self, locator):
        """该方法专门给Element封装用的，所以写成私有方法，平时不调用"""
        return self.driver.find_elements(by=locator[0], value=locator[1])

    # 定位元素
    def get_element(self, locator, timeout=WAIT_UNTIL_TIMEOUT, frequency=WAIT_FREQUENCY):
        """
        通过定位器获取页面元素，每一段时间尝试获取一次，获取成功后返回获取的页面元素，获取失败后抛出 NoSuchElement 异常
        locator: 定位器，包含定位方式和定位表达式的元组，如("id", "username")
        timeout: 超时时间，默认为30秒
        frequency: 获取频率，默认为0.5秒
        :param locator:
        :param timeout:
        :param frequency:
        :return:
        """
        # 之所以使用lambda表达式是因为util接收的参数是method而不是element，所以不能显式调用find_element方法，
        # 而是将find_element方法作为参数传给until。同时method的参数是driver，所以这里lambda表达式接收的参数也是driver。
        # until 也可以使用expected_conditions，EC所有的类都是期望场景，实例方法__call__里接收参数driver。
        element = WebDriverWait(self.driver, timeout, frequency).until(
            lambda _driver: _driver.find_element(by=locator[0], value=locator[1]), str(locator))
        return element

    # 定位元素组
    def get_elements(self, locator, timeout=WAIT_UNTIL_TIMEOUT, frequency=WAIT_FREQUENCY):
        elements = WebDriverWait(self.driver, timeout, frequency).until(
            lambda _driver : _driver.find_element(by=locator[0], value=locator[1]), str(locator))
        return elements

    # 获取页面源码
    def get_page_source(self):
        return self.driver.page_source

    # 获取页面标题title
    def get_title(self):
        return self.driver.title

    # 获取当前页面地址URL
    def get_url(self):
        return self.driver.current_url

    # 获取当前浏览器
    def get_driver(self):
        return self.driver

    # 打开网页
    def navigate_to(self, url):
        self.driver.get(url)

    # 前进操作
    def forward(self):
        self.driver.forward()

    # 后退操作
    def back(self):
        self.driver.back()

    # 关闭页面
    def close(self):
        self.driver.close()

    # 刷新页面
    def refresh(self):
        self.driver.refresh()

    # 关闭浏览器
    def quit(self):
        self.driver.quit()

    # 返回父frame，适用于多个frame嵌套
    def switch_to_parent_frame(self):
        self.driver.switch_to.parent_frame()
        time.sleep(2)

    # 返回主frame文档,最上层的frame
    def switch_to_default_frame(self):
        self.driver.switch_to.default_content()
        time.sleep(2)

    # 获取弹框文字内容
    def get_alert_text(self):
        text = self.driver.switch_to.alert.text
        return text

    # 接受弹框
    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    # 取消/关闭弹框
    def dismiss_alert(self):
        self.driver.switch_to.alert.dismiss()

    # 弹框输入值
    def send_alert_keys(self, value):
        self.driver.switch_to.send_keys(value)

    # 设置浏览器大小
    def set_window_size(self, x, y):
        self.driver.set_window_size(x, y)

    # 最大化浏览器
    def maximize_window(self):
        self.driver.maximize_window()

    # 最小化浏览器
    def minimize_window(self):
        self.driver.minimize_window()

    # 新开一个浏览器窗口
    def new_window(self, url):
        js = 'window.open({0});'.format(url)
        self.driver.execute_script(js)

    # 打开选择第一个浏览器标签页窗口
    def switch_to_frist_window(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[0])

    # 选择最后一个浏览器标签页窗口
    def switch_to_last_window(self):
         windows = self.driver.window_handles
         self.driver.switch_to.window(windows[-1])

    # 选择特定的第X个标签页窗口
    def switch_to_specific_window(self, window_index):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[window_index - 1])

    # 获取cookies
    def get_cookies(self):
        self.driver.get_cookies()

    # 获取特定cookie
    def get_cookie(self, cookie_name):
        self.driver.get_cookie(cookie_name)

    # 删除cookies
    def delete_cookies(self):
        self.driver.delete_all_cookies()

    # 删除特定cookie
    def delete_cookie(self, name, option_string):
        self.driver.delete_cookie(name, option_string)

    # 增加cookie
    def add_cookie(self, cookie_dict):
        self.driver.add_cookie(cookie_dict)

    # 截图
    def take_screenshot(self, filename):
        now_time = time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
        _filename = '{0}_{1}.png'.format(now_time, filename)
        if not os.path.exists(RESULT_SCREENSHOTS_DIR):
            os.makedirs(RESULT_SCREENSHOTS_DIR)
        filepath = os.path.join(RESULT_SCREENSHOTS_DIR, _filename)
        self.driver.get_screenshot_as_file(filepath)


