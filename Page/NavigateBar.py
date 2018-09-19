# coding=utf-8

from Page.BasePage import BasePage
from Src.Element import Element

class NavigateBar(BasePage):

    def navigate_bar_no_json(self):
        return Element(self.driver, 'homepage.navigate_bar', ('css seletor', '.nav-menu-open'))

    def utest_button_no_json(self):
        return Element(self.driver, 'homepage.utest_button', ("xpath", "//img[@src='assets/images/uTestLogoNav.svg']"))

    def articles_button_no_json(self):
        return Element(self.driver, 'homepage.articles_button', ("xpath", "//a[@ui-sref='article']"))

    def training_button_no_json(self):
        return Element(self.driver, 'homepage.training_button', ("xpath", "//a[@ui-sref='course({track: 1})']"))

    def forums_button_no_json(self):
        return Element(self.driver, 'homepage.forums_button', ("link text", "Forums"))

    def tools_button_no_json(self):
        return Element(self.driver, 'homepage.tools_button', ("xpath", "//a[@ui-sref='tool']"))

    def projects_button_no_json(self):
        return Element(self.driver, 'homepage.projects_button', ("xpath", "//a[@ui-sref='project']"))

    def navigate_bar(self, get_locator=False):
        return self._define_element(get_locator=get_locator)

    def utest_button(self, get_locator=False):
        return self._define_element(get_locator=get_locator)

    def articles_button(self, get_locator=False):
        return self._define_element(get_locator=get_locator)

    def training_button(self, get_locator=False):
        return self._define_element(get_locator=get_locator)

    def forums_button(self, get_locator=False):
        return self._define_element(get_locator=get_locator)

    def tools_button(self, get_locator=False):
        return self._define_element(get_locator=get_locator)

    def projects_button(self, get_locator=False):
        return self._define_element(get_locator=get_locator)