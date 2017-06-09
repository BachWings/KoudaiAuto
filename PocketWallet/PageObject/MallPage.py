__author__ = 'Bach'
__time__ = '2017/6/9'

import time
from macaca import WebDriverException

from Public.BasePage import BasePage
from Public.Decorator import teststep
from Public.Decorator import teststeps
from Public.ConfigParser import getConfig

class MallPage(BasePage):
    @teststep
    def wait_page(self, timeout=10000):
        """以充值Button的xpath为依据"""
        try:
            self.driver\
                .wait_for_element_by_xpath(getConfig('MallPage', 'recharge'), timeout=timeout)
            return True
        except WebDriverException:
            return False