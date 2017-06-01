__author__ = 'Bach'
__time__ = '2017/5/31'

import time
from macaca import WebDriverException

from Public.BasePage import BasePage
from Public.Decorator import teststep
from Public.Decorator import teststeps
from Public.ConfigParser import getConfig

class MyPage(BasePage):
    @teststep
    def wait_page(self, timeout = 10000):
        """以设置按钮的ID为依据"""
        self.driver \
            .wait_element_by_id()
