# coding=utf-8

from Page.NavigateBar import NavigateBar
from Page.HomePage import HomePage
from Utils.Paths import FIREFOX_DRIVER_DIR
from Src.PUnittest import PUnittest
from Utils.Logger import testLogger
from Utils.Decorator import my_testcase
from selenium import webdriver
from Utils.ParseConfig import parseConfig
import time

SCREENSHOT_SWICTH = parseConfig.screenshot_config('ScreenShotSwitch')
# print SCREENSHOT_SWICTH

class TestSubPageTitle(PUnittest):

    driver = webdriver.Firefox(executable_path=FIREFOX_DRIVER_DIR)
    homePage = HomePage(driver)
    navigateBar = NavigateBar(driver)

    @classmethod
    def setUpClass(cls):
        cls.homePage.browser.navigate_to('https://www.utest.com1')

    @classmethod
    def tearDownClass(cls):
        cls.homePage.browser.quit()

    def setUp(self):
        testLogger.info(self._testMethodName.center(100, '*'))

    def tearDown(self):
        testLogger.info('*' * 100 + '\n')

    @my_testcase
    def test_articles_title(self):
        navigate_bar_visible = self.navigateBar.navigate_bar().is_displayed()
        if not navigate_bar_visible:
            self.homePage.expand_navigate_button().click()
        article_button_text = self.navigateBar.articles_button().get_text()
        self.assertTrue(article_button_text == 'xxxxxxx')
        self.navigateBar.articles_button().click()
        time.sleep(2)
        title_label_text = self.homePage.title_label().get_text()
        self.assertEqual(title_label_text, 'uuuuuu')
