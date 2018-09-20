# coding=utf-8

from Page.NavigateBar import NavigateBar
from Page.HomePage import HomePage
from Utils.Paths import FIREFOX_DRIVER_DIR
from Src.PUnittest import PUnittest
from Utils.Logger import testLogger
from Utils.Decorator import my_testcase
from selenium import webdriver
from Utils.ParseConfig import parseConfig
import unittest
import time

SCREENSHOT_SWICTH = parseConfig.screenshot_config('ScreenShotSwitch')

class TestSubPageTitle(PUnittest):

    driver = webdriver.Firefox(executable_path=FIREFOX_DRIVER_DIR)
    homePage = HomePage(driver)
    navigateBar = NavigateBar(driver)

    @classmethod
    def setUpClass(cls):
        cls.homePage.browser.navigate_to('https://www.utest.com')

    @classmethod
    def tearDownClass(cls):
        cls.homePage.browser.quit()

    def setUp(self):
        testLogger.info(' {0} >> {1} '.format(self.__class__.__name__, self._testMethodName).center(80, '*'))

    def tearDown(self):
        testLogger.info('-' * 80 + '\n')

    @my_testcase
    def test_articles_title(self):
        navigate_bar_visible = self.navigateBar.navigate_bar().is_displayed()
        if not navigate_bar_visible:
            self.homePage.expand_navigate_button().click()
        self.navigateBar.articles_button().click()
        time.sleep(2)
        title_label_text = self.homePage.title_label().get_text()
        self.assertEqual(title_label_text, 'Software Testing Articles')

    @my_testcase
    def test_training_title(self):
        navigate_bar_visible = self.navigateBar.navigate_bar().is_displayed()
        if not navigate_bar_visible:
            self.homePage.expand_navigate_button().click()
        self.navigateBar.training_button().click()
        time.sleep(2)
        title_label_text = self.homePage.title_label().get_text()
        self.assertEqual(title_label_text, 'Software Testing Courses')

    @my_testcase
    def test_tools_title(self):
        navigate_bar_visible = self.navigateBar.navigate_bar().is_displayed()
        if not navigate_bar_visible:
            self.homePage.expand_navigate_button().click()
        self.navigateBar.tools_button().click()
        time.sleep(2)
        title_label_text = self.homePage.title_label().get_text()
        self.assertEqual(title_label_text, 'uxuxuxuxuxuxu')

    @my_testcase
    def test_formus_title(self):
        navigate_bar_visible = self.navigateBar.navigate_bar().is_displayed()
        if not navigate_bar_visible:
            self.homePage.expand_navigate_button().click()
        self.navigateBar.forums_button().click()
        time.sleep(2)
        title_label_text = self.homePage.title_label().get_text()
        self.assertEqual(title_label_text, 'Software Testing Forums')

    @my_testcase
    def test_projects_title(self):
        navigate_bar_visible = self.navigateBar.navigate_bar().is_displayed()
        if not navigate_bar_visible:
            self.homePage.expand_navigate_button().click()
        self.navigateBar.projects_button().click()
        time.sleep(2)
        title_label_text = self.homePage.title_label().get_text()
        self.assertEqual(title_label_text, 'xxxxxxxxxxx')

if __name__ == '__main__':
    unittest.main()
