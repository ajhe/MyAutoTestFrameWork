# coding=utf-8

from Utils.Logger import testLogger
from Utils.ParseConfig import parseConfig
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
import sys

SCREENSHOT_SWICTH = parseConfig.screenshot_config('ScreenShotSwitch')
RERUN_SWICTH = parseConfig.rerun_config('ReRunSwitch')
RERUN_TIME = parseConfig.rerun_config('ReRunTime')

def logger_callar(cls):
    """装饰类，添加日志，记录的调用方法"""
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)

        def __getattr__(self, attr):
            # print testLogger
            testLogger.debug('Call: {0} >> {1}'.format(cls.__name__, attr))
            method = getattr(self.wrapped, attr)
            return method
    return Wrapper


def logger_browser(exc=WebDriverException):
    """
    装饰Browser类中的实例方法，添加日志，记录调用的方法和调用的结果
    如果是指定异常，则不抛出错误只记录日志，否则抛出
    无法装饰静态方法和类方法，因为类名是从*args中取的第一个参数
    :param exc:
    :return:
    """
    def wrapper(func):
        def on_call(*args, **kwargs):
            _cls_name = args[0].__class__.__name__
            _met_name = func.__name__
            try:
                result = func(*args, **kwargs)
                if result is not None:
                    testLogger.debug('[Call]: {0} >> {1} [Return]: {2}'.format(_cls_name, _met_name, result))
                else:
                    testLogger.debug('[Call]: {0} >> {1}'.format(_cls_name, _met_name))
                return result
            except exc as e:
                exc_type, _, _ = sys.exc_info()
                testLogger.warning('[{0}]: {1}'.format(exc_type.__name__, e).rstrip())
            except Exception:
                testLogger.exception('[UnwantedException]:')
                raise
            return on_call
    return wrapper

def my_logger_browser(func):
    def wrapper(self, *args, **kwargs):
        _met_name = func.__name__
        _cls_name = self.__class__.__name__
        try:
            result = func(self, *args, **kwargs)
            if result is not None:
                testLogger.debug('[Call]: {0} >> {1} [Return]: {2}'.format(_cls_name, _met_name, result))
            else:
                testLogger.debug('[Call]: {0} >> {1}'.format(_cls_name, _met_name))
            return result
        except WebDriverException as e:
            exc_type, _, _ = sys.exc_info()
            testLogger.warning('[{0}]: {1}'.format(exc_type.__name__, e).rstrip())
        except Exception:
            testLogger.exception('[UnwantedException]:')
            raise
    return wrapper


def logger_wait(exc=WebDriverException):
    """专门用来装饰Src文件下的Wait类"""
    def wrapper(func):
        def on_call(*args, **kwargs):
            _cls_name = args[0].__class__.__name__
            _met_name = func.__name__
            try:
                result = func(*args, **kwargs)
                _result = True if result else False
                testLogger.debug('[Call]: {0} >> {1} [Return]: {2}'.format(_cls_name,_met_name,_result))
                return result
            except exc as e:
                exc_type, _, _ = sys.exc_info()
                testLogger.warning('[{0}]: {1}'.format(_cls_name,_met_name))
            except Exception:
                testLogger.exception('[UnwantedException]:')
                raise
        return on_call
    return wrapper

def my_logger_wait(func):
    def wrapper(self, *args, **kwargs):
        _met_name = func.__name__
        _cls_name = self.__class__.__name__
        try:
            result = func(self, *args, **kwargs)
            _result = True if result else False
            testLogger.debug('[Call]: {0} >> {1} [Return]: {2}'.format(_cls_name, _met_name, _result))
            return result
        except TimeoutException as e:
            testLogger.warning('[TimeoutException]: {0}'.format(e).rstrip())
        except WebDriverException as e:
            exc_type, _, _ = sys.exc_info()
            testLogger.error('[{0}]: {1}'.format(exc_type.__name__, e).rstrip())
            raise
        except Exception:
            testLogger.exception('[UnwantedException]:')
            raise
    return wrapper

def logger_element(exc=WebDriverException):
    """专门装饰Src文件夹里的Element类"""
    def wrapper(func):
        def on_call(*args, **kwargs):
            _cls_name = args[0].__class__.__name__
            _met_name = func.__name__
            _element_name = args[0].name
            try:
                result = func(*args, **kwargs)
                if result is not None:
                    testLogger.debug('[Call]: {0} >> {1} >> {2} [Return]: {3}'.format(_cls_name, _met_name, _element_name, result))
                else:
                    testLogger.debug('[Call]: {0} >> {1} >> {2}'.format(_cls_name,_met_name,_element_name))
            except TimeoutException:
                testLogger.warning('[TimeoutException]: Fail to locate element {0}'.format(_element_name))
            except exc as e:
                exc_type, _, _ = sys.exc_info()
                testLogger.warning('[{0}]: {1}'.format(exc_type.__name__, e).rstrip())
            except Exception:
                testLogger.exception('[UnwantedException]:')
                raise
        return on_call
    return wrapper


def my_logger_element(func):
    def wrapper(self, *args, **kwargs):
        _met_name = func.__name__
        _cls_name = self.__class__.__name__
        _ele_name = self.name
        try:
            result = func(self, *args, **kwargs)
            if result is not None:
                testLogger.debug('[Call]: {0} >> {1} >> {2} [Return]: {3}'.format(_cls_name, _met_name, _ele_name, result))
            else:
                testLogger.debug('[Call]: {0} >> {1} >> {2}'.format(_cls_name, _met_name, _ele_name))
            return result
        except TimeoutException:
            testLogger.warning('[TimeoutException]: Fail to locate element {0}'.format(_ele_name))
        except WebDriverException as e:
            exc_type, _, _ = sys.exc_info()
            testLogger.warning('[{0}]: {1}'.format(exc_type.__name__, e).rstrip())
        except Exception:
            testLogger.exception('[UnwantedException]:')
            raise
    return wrapper

def my_unittest_assertion(func):
    """装饰断言类函数"""
    def wrapper(self, *args, **kwargs):
        try:
            testLogger.debug('[Assert]: {0} >> {1}'.format(func.__name__, format(args[:])))
            return func(self, *args, **kwargs)
        except AssertionError as e:
            self.Exc_Stack.append(e)
    return wrapper

def my_testcase(func, screen_shot = SCREENSHOT_SWICTH, rerun=RERUN_SWICTH):
    def wrapper(self, *args, **kwargs):
        if rerun is False:
            rerun_time = 1
        elif rerun is True:
            rerun_time = RERUN_TIME
        elif isinstance(rerun, int):                                   # 这里是因为isinstance(True, int)也为真，所以分开判断
            rerun_time = rerun
        else:
            rerun_time = RERUN_TIME
        _testcase_name = self._testMethodName
        _testclass_name = self.__class__.__name__

        # _browser是获取测试用例实例browser属性，因为跨越了多个页面类属性层，因此用到循环
        _browser = None
        for attr in dir(self):
            if hasattr(getattr(self, attr), 'browser'):
                _browser = getattr(getattr(self, attr), 'browser')
                break

        # 循环执行用例
        _rerun_time = rerun_time
        while rerun_time > 0:
            try:
                testLogger.info(('TestRun {0} times'.format(_rerun_time - rerun_time + 1)).center(80,'-'))
                result = func(self, *args, **kwargs)
                # 执行完用例后，调用PUintest中的raise_exc()函数抛出所有异常
                self.raise_exc()
                testLogger.info(' TestResult: '.center(80, '-'))
                testLogger.info('[TestSuccess]: {0} >> {1}'.format(_testclass_name, _testcase_name))
                return result
            except Exception:
                if screen_shot:
                    _filename = 'Error' + _testcase_name
                    _browser.take_screenshot(_filename)
                rerun_time -= 1
                if rerun_time == 0:
                    exc_type, exc_msg, _ = sys.exc_info()
                    testLogger.info(' TestResult: '.center(80, '-'))
                    testLogger.error('[TestFail]: {0} >> {1}'.format(exc_type.__name__, exc_msg))
                    raise
    return wrapper




if __name__ == '__main__':
    pass