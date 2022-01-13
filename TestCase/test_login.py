#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import pytest
import allure
import time
from utils.logger import log
from common.readconfig import ini
from page_object.loginpage import LoginPage


@allure.feature("测试用户登录")
class TestLogin:
    @pytest.fixture(scope='function', autouse=True)
    def open_system(self, drivers):
        """打开系统"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("登录测试用例")
    def test_001(self, drivers):
        """登录"""
        login = LoginPage(drivers)
        login.input_username("chener")
        login.click_login()
  #      login.click_login()
  #      login.input_password("admin123")
  #      login.click_login()
  #      result = re.search(r'selenium', login.get_source)
  #      log.info(result)
  #      assert result

  #  @allure.story("测试搜索候选用例")
  #  def test_002(self, drivers):
  #      """测试搜索候选"""
  #      search = LoginPage(drivers)
  #      search.input_search("selenium")
  #      log.info(list(search.imagine))
  #      assert all(["selenium" in i for i in search.imagine])


if __name__ == '__main__':
    pytest.main(['TestCase/test_login.py'])
# if __name__ == '__main__':
# 下面的代码使用pycharm运行可能会没有生成报告，建议使用vscode执行
#     import os
#     pytest.main(['TestCase/test_search.py', '--alluredir', './allure'])
#     os.system('allure serve allure')
