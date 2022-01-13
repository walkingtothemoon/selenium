#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element

loginpage = Element('loginpage')


class LoginPage(WebPage):
    """登录类"""

    def input_username(self, content):
        """输入搜索"""
        self.input_text(loginpage['用户名框'], txt=content)
        sleep()

    @property
    def imagine(self):
        """搜索联想"""
        return [x.text for x in self.find_elements(loginpage['用户名候选'])]

    def click_login(self):
        """点击登录"""
        self.is_click(loginpage['登录按钮'])


if __name__ == '__main__':
    pass
