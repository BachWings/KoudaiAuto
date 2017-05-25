__author__ = 'Bach'

import time

from Public.BasePage import BasePage
from Public.Decorator import teststep
from Public.Decorator import testcase

from PocketWallet.PageObject.PocketWalletHomePage import PocketWalletHomePage



class WizardPage(BasePage):
    @teststep
    def wait_page(self):
        """以Wizard中图片的class name为依据"""
        self.driver \
            .wait_for_element_by_class_name('android.widget.ImageView')

    @teststep
    def skip(self):
        """以Wizard中图片的class name为依据"""
        for i in range(3):
            self.swipe_left(steps=3)
            time.sleep(1)

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
    # home_page.handle_alert()
    assert home_page.wait_page()





