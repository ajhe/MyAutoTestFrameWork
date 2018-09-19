# coding=utf-8

from Page.BasePage import BasePage
from Src.Element import Element

class HomePage(BasePage):

    def expand_navigate_button_no_json(self):
        return Element(self.driver, 'homepage.expand_navigate_button', ("class name", "hamburger"))

    def title_label_no_json(self):
        return Element(self.driver, 'homepage.title_label', ("class name", "section-title"))

    def expand_navigate_button(self, get_locator=False):
        return self._define_element(get_locator=get_locator)

    def title_label(self, get_locator=False):
        return self._define_element(get_locator=get_locator)

if __name__ == '__main__':
    pass
