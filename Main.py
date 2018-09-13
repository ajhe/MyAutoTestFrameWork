# coding=utf-8

from Src.Browser import Browser
from Src.Element import Element
from Src.Wait import Wait
from Utils.Paths import FIREFOX_DRIVER_DIR
from selenium import webdriver
from Utils.Logger import testLogger

try:
    print FIREFOX_DRIVER_DIR
    driver = webdriver.Firefox()
    browser = Browser(driver)
    browser.navigate_to("http://www.zhihu.com")
    title = browser.get_title()
    print title

    locator = ('xpath', "//input[@placeholder='手机号']")
    Element(driver, 'mobilephone_textbox', locator).click()
    Element(driver, 'mobilephone_textbox', locator).send_keys('123456798')
    Element(driver, 'mobilephone_textbox', locator).clear()

    locator = ('xpath', "//input[@placeholder='123']")
    Wait(driver).element_not_visible(locator)
    Element(driver, 'mobilephone_textbox', locator).click()

except Exception as e:
    testLogger.error(e)
finally:
    browser.quit()


