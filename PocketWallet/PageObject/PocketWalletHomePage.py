__author__ = 'Bach'

import time

from macaca import WebDriverException
from Public.BasePage import BasePage
from Public.Decorator import teststep

# from Public.Decorator import teststeps

'''from App.PageObject.WebViewPage import WebViewPage
from App.PageObject.InviteFriendsPage import InviteFriendsPage
from App.PageObject.LoginPage import LoginPage
# from App.PageObject.MsgCenterPage import MsgCenterPage'''


class PocketWalletHomePage(BasePage):
    @teststep
    def handle_alert(self):

        if self.driver.element_if_exists('id', 'com.android.packageinstaller:id/permission_allow_button'):
            self.driver.element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
            time.sleep(1)
            self.handle_alert()
        else:
            pass

    @teststep
    def wait_page(self, timeout=10000):
        """以“信用付”的xpath为标志"""

        try:
            self.driver \
                .wait_for_element_by_xpath("//android.widget.TextView[@text='信用付']", timeout=timeout)
            return True
        except WebDriverException:
            return False
