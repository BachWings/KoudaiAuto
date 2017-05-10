__author__ = 'Bach'

import time

from Public.BasePage import BasePage
from Public.Decorator import teststep
from Public.Decorator import testcase

from PocketWallet.PageObject.PocketWalletHomePage import PocketWalletHomePage



class WizardPage(BasePage):

    """@teststep
    def evn_select(self):
        '''选择环境'''
        self.find_element_on_vertical('id', 'cn.pocketwallet.pocketwallet:id/test_server_yun')
        self.driver \
            .element_by_id('cn.pocketwallet.pocketwallet:id/test_server_yun').click()"""

    '''@teststep
    def enter_evn(self):
        # self.find_element_on_vertical('id', 'cn.pocketwallet.pocketwallet:id/btn_launch_activity', steps=5)
        self.driver \
            .element_by_id('cn.pocketwallet.pocketwallet:id/btn_launch_activity').click()'''

    @teststep
    def wait_page(self):
        """以Wizard中图片的class name为依据"""
        self.driver \
            .wait_for_element_by_class_name('android.widget.ImageView')

    @teststep
    def skip(self):
        """以Wizard中图片的class name为依据"""
        for i in range(3):
            self.swipe_left(steps=5)

            time.sleep(3)

        self.driver \
            .element_by_xpath('//android.widget.ImageView').click()


@testcase
def skip_wizard_to_home():
    """在App启动页面，跳过Wizard进入到App首页"""
    wizard = WizardPage()
    # wizard.evn_select()
    # wizard.enter_evn()
    wizard.wait_page()
    wizard.skip()

    home_page = PocketWalletHomePage()
    home_page.handle_alert()
    assert home_page.wait_page()





